# This is a simple Python based snake game.
from turtle import Turtle, Screen
import time
faz = Turtle(shape='square')
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

faz.color('white')
faz.penup()
segments = []
segments.append(faz)
x_coordinate = 0

for turtle in range(3):
    x_coordinate -= 20
    new_turtle = Turtle(shape='square')
    new_turtle.penup()
    new_turtle.color('white')
    new_turtle.goto(x_coordinate, 0)
    segments.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)


screen.exitonclick()
