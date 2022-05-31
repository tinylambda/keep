import base64
import hashlib
import urllib.parse


if __name__ == "__main__":
    enc_key = "a0e6aae84de17fc5b9cc27cb2a8ccbcc"
    query_string = "dataSourceId=12345678&operateDateStart=2018-06-25&operateDateEnd=2018-06-27&operateType=2"
    query_string = urllib.parse.quote(query_string)
    print(query_string)
    x = hashlib.md5(query_string.encode("utf-8"))
    sig = x.hexdigest()
    r = [ord(a) ^ ord(b) for a, b in zip(sig, enc_key)]
    r = [chr(item) for item in r]
    r = "".join(r)
    r = base64.b64encode(r.encode())
    print(r)
