import argparse
import datetime
import json
import math
import struct
import happybase
from thriftpy2.transport import TTransportException

HBASE_THRIFT_HOST = "hbase_thrift_server_host"
HBASE_THRIFT_PORT = 9099
HBASE_THRIFT_TRANSPORT = "buffered"
HBASE_THRIFT_PROTOCOL = "binary"
HBASE_TABLE_NAME = "net_status_ttl"


class SubjectTTLExtractor:
    KEY_SEP = "-"
    KEY_NAMES = [
        "dummy",
        "subject_id",
        "user_type",
        "user_id",
        "media_type",
        "timestamp",
    ]
    KEY_LEN = len(KEY_NAMES)
    ENCODING_MAP = {
        "cf:intervalSeconds": lambda v: struct.unpack(">I", v)[0],
        "cf:mediaType": lambda v: v.decode()[0],
        "cf:subjectId": lambda v: struct.unpack(">I", v)[0],
        "cf:timeStamp": lambda v: struct.unpack(">I", v)[0],
        "cf:userId": lambda v: struct.unpack(">I", v)[0],
        "cf:userType": lambda v: struct.unpack(">I", v)[0],
        "cf:rtt": lambda v: struct.unpack(">I", v)[0],
        "cf:bitRate": lambda v: struct.unpack(">I", v)[0],
        "cf:lostRate": lambda v: struct.unpack(">d", v)[0],
        "recv:bitRate": lambda v: struct.unpack(">I", v)[0],
        "recv:lostRate": lambda v: struct.unpack(">d", v)[0],
    }

    def __init__(self):
        self.connection = None
        self.table: happybase.Table = None
        self.init_extractor()

    def init_extractor(self):
        try:
            self.connection = happybase.Connection(
                HBASE_THRIFT_HOST,
                port=HBASE_THRIFT_PORT,
                transport=HBASE_THRIFT_TRANSPORT,
                protocol=HBASE_THRIFT_PROTOCOL,
            )
            self.table = self.connection.table(HBASE_TABLE_NAME)
        except TTransportException:
            self.connection = None

    def serialize_one_record(self, key, data):
        key = key.decode()
        key_values = key.split(self.KEY_SEP)
        assert len(key_values) == self.KEY_LEN
        record_dict = dict(zip(self.KEY_NAMES, key_values))

        for item in data:
            item_decoded = item.decode()
            value_decoder = self.ENCODING_MAP.get(item_decoded)
            if value_decoder:
                value = value_decoder(data[item])
                if type(value) is float and math.isnan(value) or math.isinf(value):
                    value = None
                record_dict.update({item_decoded.replace(":", "_"): value})
            else:
                print(item, "========", data[item])

        record_json = json.dumps(record_dict)
        return record_json

    def extract(self, subject_id):
        subject_id_int = int(subject_id)
        dummy = subject_id_int % 10
        row_start = f"{dummy}-{subject_id}-"
        row_stop = f"{dummy}-{subject_id}."
        scan_result_g = self.table.scan(row_start=row_start, row_stop=row_stop)
        return scan_result_g


if __name__ == "__main__":
    now_time = datetime.datetime.now()
    one_day_ago_time = now_time + datetime.timedelta(days=-1)

    one_day_ago_date_str = one_day_ago_time.strftime("%Y-%m-%d %H:%M:%S")
    default_filename_str = f"net_status_ttl_{one_day_ago_date_str}.log"

    parser = argparse.ArgumentParser(
        description="SubjectTTLExtractor to copy data from HBase to a local file"
    )
    parser.add_argument(
        "--date", action="store", dest="date", default=one_day_ago_date_str
    )
    parser.add_argument(
        "--filename", action="store", dest="filename", default=default_filename_str
    )
    args = parser.parse_args()

    ste = SubjectTTLExtractor()
    date = "2020-03-10"
    filename = args.filename
    subject_ids = [
        "26347420",
        # '27875044',
        # '27540530',
    ]

    with open(filename, "w") as f:
        for sid in subject_ids:
            for key, data in ste.extract(subject_id=sid):
                record_json = ste.serialize_one_record(key, data)
                f.write(record_json + "\n")
