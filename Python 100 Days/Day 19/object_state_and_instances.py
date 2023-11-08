from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput('Turtle Racing Bet', 'Who will win the Race? Enter a color:').title()
colors = ['red', 'orange', 'yellow','green', 'blue', 'purple']
y_positions = [-180, -120, -60, 0, 60, 120]
all_turtle = []

for i in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-220, y=y_positions[i])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You won!!!{winning_color } turtle have won the race')
            else:
                print(f'You lost!!!{winning_color } turtle have won the race')

        speed_selection = random.randint(0, 10)
        turtle.forward(speed_selection)

screen.exitonclick()
