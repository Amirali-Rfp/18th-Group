import turtle
import time

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0)
turtle.bgcolor('black')
turtle.pencolor('medium sea green')


def update():
    turtle.clear()
    turtle.write(time.strftime('%H:%M:%S %p'), align='center', font=('Arial', 25, 'bold'))
    turtle.ontimer(update, 1000)


update()
turtle.exitonclick()
