from turtle import *


def star(side_length=100):
    move_angle = 180 / 5 * 4
    for i in range(5):
        forward(side_length)
        right(move_angle)


def star_spiral(n=60):
    side_length = 100
    for i in range(n):
        star(side_length)
        right(5)
        side_length += 5


star_spiral(60)
speed(0.2)
mainloop()
