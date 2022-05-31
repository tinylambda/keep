import turtle

turtle.shape("turtle")
turtle.home()
print(turtle.position())


def draw_turtle(side_num=30, side_length=100):
    move_angle = 2 * (180 / side_num)

    sides_draw = 0
    foot_step = side_num // 4
    for i in range(side_num):
        if i == 0 or i == side_num // 2:
            turtle.circle(10)

        if (
            i == foot_step
            or i == foot_step * 2
            or i == foot_step * 3
            or i == foot_step * 4
        ):
            turtle.circle(20)

        turtle.forward(side_length)
        turtle.right(move_angle)


draw_turtle(side_length=50)
turtle.mainloop()
