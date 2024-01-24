import turtle as t
from random import random

t.speed(0)
t.hideturtle()

t.left(90)
for i in range(10):
    if i == 0 or i == 9:
        t.pensize(5)
    elif not i % 3:
        t.pensize(3)
    else:
        t.pensize(1)

    t.penup()
    t.goto(-180, -180 + 40 * i)
    t.pendown()
    t.right(90)
    t.forward(360)

    t.penup()
    t.goto(-180 + 40 * i, -180)
    t.pendown()
    t.left(90)
    t.forward(360)

t.done()

