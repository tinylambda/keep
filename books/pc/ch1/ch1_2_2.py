import math


def avg(grades):
    return sum(grades) / len(grades)


def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)


record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print(phone_numbers)

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

