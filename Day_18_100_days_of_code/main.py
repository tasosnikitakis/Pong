import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(n):
    for _ in range(int(360/n)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + n)

draw_spirograph(3)

screen = t.Screen()
screen.exitonclick()

