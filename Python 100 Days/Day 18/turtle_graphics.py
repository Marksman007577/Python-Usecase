import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)

direction = [0, 90, 180, 270]

timmy = Turtle()
timmy.shape(name='turtle')
timmy.color('green')
timmy.pencolor('red')


def random_color_generator():
    red = random.randint(a=0,b=255)
    green = random.randint(a=0,b=255)
    blue = random.randint(a=0,b=255)
    rgb_color = (red,green,blue)
    return rgb_color


def draw_square():
    sides = 4
    for i in range(sides):
        timmy.forward(100)
        timmy.left(90)


def draw_rectangle():
    sides = 3
    for i in range(sides):
        timmy.forward(100)
        timmy.left(120)


def draw_polygon():
    sides = 5
    for i in range(sides):
        timmy.forward(100)
        timmy.left(72)


def draw_dotted_line():
    paces = 10
    for i in range(15):
        timmy.forward(paces)
        timmy.penup()
        timmy.forward(paces)
        timmy.pendown()


def draw_shape(sides):
    angles = round(float(360 / i), 2)
    for n in range(sides):
        timmy.forward(100)
        timmy.left(angles)


def random_walk(steps):
    for step in range(steps):
        timmy.hideturtle()
        timmy.setheading(random.choice(direction))
        timmy.forward(20)


for i in range(3, 11):
    timmy.pensize(5)
    timmy.pencolor(random_color_generator())
    draw_shape(sides=i)


for i in range(10):
    timmy.speed('fastest')
    timmy.pensize(10)
    timmy.pencolor(random_color_generator())
    random_walk(steps=i)


screen = Screen()
screen.screensize(canvwidth=400, canvheight=400, bg=None)
screen.exitonclick()

