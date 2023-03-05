#imports
import turtle
from turtle import Turtle
from turtle import Screen
from game_items import Padles

import time

#screen creation
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
#screen.tracer(0)




#right padle creation
right_padle = Padles()
right_padle.setposition(350,0)


#left padle creation
left_padle = Padles()
left_padle.setposition(-350,0)



#right_paddle move up or down


screen.listen()
screen.onkey(right_padle.move_padle_down, "Down")
screen.onkey(right_padle.move_padle_up, "Up")
screen.onkey(left_padle.move_padle_up, "w")
screen.onkey(left_padle.move_padle_down, "s")

screen.exitonclick()