import enum


class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1
    # Enum members with the same value are tracked as alias references to the same member object
    by_design = 4
    closed = 1


# Aliases do not cause repeated values to be present in the iterator for the Enum
# The canonical name for a member is the first name attached to the value
for status in BugStatus:
    print("{:15} = {}".format(status.name, status.value))


print("\nSame: by_design is wont_fix: ", BugStatus.by_design is BugStatus.wont_fix)
print("Same: closed is fix_released: ", BugStatus.closed is BugStatus.fix_released)
