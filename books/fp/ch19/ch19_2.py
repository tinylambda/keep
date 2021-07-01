import keyword
from collections import abc

from ch19_1 import load


class FrozenJson:
    def __init__(self, mapping):
        self.__data = dict()
        for k, v in mapping.items():
            if keyword.iskeyword(k):
                k += '_'
            self.__data[k] = v

    def __getattr__(self, item):
        if hasattr(self.__data, item):
            return getattr(self.__data, item)
        else:
            return FrozenJson.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


if __name__ == '__main__':
    raw_feed = load()
    feed = FrozenJson(raw_feed)
    print(
        len(feed.Schedule.speakers)
    )
    print(
        sorted(feed.Schedule.keys())
    )

    for key, value in sorted(feed.Schedule.items()):
        print('{:3} {}'.format(len(value), key))

    print(
        feed.Schedule
    )

    print(
        feed.Schedule.speakers[-1].name
    )

    talk = feed.Schedule.events[40]
    print(
        talk.name
    )

    print(talk.speakers)
    print(talk.flavor)
