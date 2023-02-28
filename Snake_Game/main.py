from turtle import Screen, Turtle

#screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

#turtle creation
for i in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(y=0, x=(0-i*20))




screen.exitonclick()