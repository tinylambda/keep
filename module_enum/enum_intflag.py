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

    zero_type = WorkType(0)
    print(zero_type)

    zero_type |= WorkType.Design
    print(zero_type)

    zero_type |= WorkType.Construction
    print(zero_type)

    print(type(zero_type))

    # This works too
    all_types = WorkType(7)
    print(WorkType.Design in all_types)
    print(WorkType.Construction in all_types)
    print(WorkType.Others in all_types)
