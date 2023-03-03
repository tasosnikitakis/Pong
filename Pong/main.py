#imports
import turtle
from turtle import Turtle
from turtle import Screen

import time

#screen creation
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)




#right padle creation
padle = Turtle()
padle.penup()
padle.shape("square")
padle.color("white")
padle.resizemode("user")
padle.setposition(350,0)
padle.shapesize(stretch_wid=5, stretch_len=1)

#right_paddle move up or down


def move_down():
    oldycor = padle.ycor()
    padle.goto(350, oldycor-20)


def move_up():
    oldycor = padle.ycor()
    padle.goto(350, oldycor+20)

screen.listen()
screen.onkey(move_down, "Down")
screen.onkey(move_up, "Up")



screen.exitonclick()