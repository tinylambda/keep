import warnings
import inspect
import shelve

from ch19_1 import load


DB_NAME = "data/schedule2_db"
CONFERENCE = "conference.115"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class MissingDatabaseError(RuntimeError):
    pass


class DbRecord(Record):
    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}'.set_db(my_db)"
                raise MissingDatabaseError(msg)
            else:
                raise

    def __repr__(self):
        if hasattr(self, "serial"):
            cls_name = self.__class__.__name__
            return "<{} serial={!r}>".format(cls_name, self.serial)
        else:
            return super(DbRecord, self).__repr__()


class Event(DbRecord):
    @property
    def venue(self):
        key = "venue.{}".format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, "_speaker_objs"):
            spkr_serials = self.__dict__["speakers"]
            fetch = self.__class__.fetch
            self._speaker_objs = [
                fetch("speaker.{}".format(key)) for key in spkr_serials
            ]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, "name"):
            cls_name = self.__class__.__name__
            return "<{} {!r}>".format(cls_name, self.name)
        else:
            return super().__repr__()


def load_db(db):
    raw_data = load()
    warnings.warn("loading " + DB_NAME)
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)

        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord

        for record in rec_list:
            key = "{}.{}".format(record_type, record["serial"])
            record["serial"] = key
            db[key] = factory(**record)


if __name__ == "__main__":
    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        load_db(db)
    DbRecord.set_db(db)
    event = DbRecord.fetch("event.33950")
    print(event)
    print(event.venue)
    print(event.venue.name)
    for spkr in event.speakers:
        print("{0.serial}: {0.name}".format(spkr))
