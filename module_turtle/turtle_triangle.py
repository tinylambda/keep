from turtle import *


def triangle(side_length=100):
    for i in range(3):
        forward(side_length)
        right(120)


triangle(700)
mainloop()
