import enum


class WorkType(enum.IntFlag):
    Design = 1
    Construction = 2
    Others = 4


if __name__ == "__main__":
    print(repr(WorkType.Design | WorkType.Construction))
    print(WorkType.Design + WorkType.Construction)

    types = WorkType.Design | WorkType.Construction
    print(WorkType.Design in types)
