from turtle import *


def square(side_length=100):
    for i in range(4):
        forward(side_length)
        right(90)


def multi_squares(n=60):
    for i in range(n):
        square()
        right(5)


multi_squares()
mainloop()
