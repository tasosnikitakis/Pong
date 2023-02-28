from turtle import Screen, Turtle
import time

#screen creation
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


#turtle creation
turtle_segments = []
for i in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(y=0, x=(0-i*20))
    turtle_segments.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    for seg_number in range(len(turtle_segments) - 1, 0 , -1):
        new_x = turtle_segments[seg_number - 1].xcor()
        new_y = turtle_segments[seg_number - 1].ycor()
        turtle_segments[seg_number].goto(new_x, new_y)
    turtle_segments[0].forward(20)


screen.exitonclick()