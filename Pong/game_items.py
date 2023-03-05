from turtle import Turtle

class Padles(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)


    def move_padle_up(self):
        oldycor = self.ycor()
        self.goto(self.xcor(), oldycor + 20)

    def move_padle_down(self):
        oldycor = self.ycor()
        self.goto(self.xcor(), oldycor - 20)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def ball_move(self):
        newy = self.ycor() + 10
        newx = self.xcor() + 10
        self.goto(newx, newy)

