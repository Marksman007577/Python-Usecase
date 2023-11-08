import turtle
import colorgram
from turtle import Turtle, Screen
turtle.colormode(255)
import random

#color_list = []
#number_of_colors = 35

#colors = colorgram.extract('image.jpg', number_of_colors)

# Get the color list by extracting them from the image using colorgram
#for n in range(len(colors)):
    #color_rgb = colors[n].rgb
    #color_rgb_red = color_rgb[0]
    #color_rgb_green = color_rgb[1]
    #color_rgb_blue = color_rgb[2]
    #final_rgb_color = (color_rgb_red, color_rgb_green, color_rgb_blue)
    #color_list.append(final_rgb_color)


new_colors = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102),
              (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]


timmy = Turtle()
timmy.speed('fastest')
timmy.penup()
timmy.hideturtle()

screen = Screen()
screen.bgcolor((229,234,183))

timmy.setheading(225)
timmy.forward(320)
timmy.setheading(0)
number_of_dots = 100

for dot in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(new_colors))
    timmy.forward(50)

    if dot % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen.exitonclick()
