from turtle import *


def polygon(side_num=3, side_length=100):
    move_angle = 2 * (180 / side_num)
    for i in range(side_num):
        forward(side_length)
        right(move_angle)


polygon()
polygon(side_num=8)
mainloop()
