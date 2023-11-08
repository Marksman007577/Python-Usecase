import turtle
from turtle import Turtle, Screen
import random


turtle.colormode(255)


def random_color_generator():
    red = random.randint(a=0,b=255)
    green = random.randint(a=0,b=255)
    blue = random.randint(a=0,b=255)
    rgb_color = (red, green, blue)
    return rgb_color


timmy = Turtle()
timmy.shape()
timmy.color('green')
timmy.pencolor('red')

heading_angle_list = []


def draw_spirograph(n_spiral):
    angle = round(float(360/n_spiral), 2)
    for i in range(n_spiral):
        current_heading = timmy.heading()
        new_heading = current_heading + angle
        heading_angle_list.append(new_heading)
        timmy.pensize(1)
        timmy.speed('fast')
        timmy.pencolor(random_color_generator())
        timmy.circle(100)
        timmy.setheading(new_heading)


draw_spirograph(n_spiral=50)

screen = Screen()
screen.screensize(canvwidth=400, canvheight=400, bg=None)
screen.exitonclick()
