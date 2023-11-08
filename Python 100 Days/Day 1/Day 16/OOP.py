from turtle import Turtle, Screen
from prettytable import PrettyTable

turtle = Turtle()
turtle.shape('turtle')
turtle.color('brown')
turtle.forward(30)

screen = Screen()
screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column("Type", ['Electric', 'Water', 'Fire'])
print(table)