from turtle import Turtle, Screen


timmy = Turtle()
screen = Screen()


def forward():
    timmy.forward(30)


def backward():
    timmy.back(30)


def clockwise():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)


def anticlockwise():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)


def clear_screen():
    timmy.clear()
    timmy.reset()


screen.listen()
screen.onkey(fun=forward, key='w')
screen.onkey(fun=backward, key='s')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=anticlockwise, key='a')
screen.onkey(fun=clear_screen, key='c')
screen.exitonclick()
