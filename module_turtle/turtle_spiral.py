from turtle import *


def square(side_length=100):
    for i in range(4):
        forward(side_length)
        right(90)


def spiral(n=60):
    side_length = 10
    for i in range(n):
        square(side_length)
        right(5)
        side_length += 5


spiral()
mainloop()
