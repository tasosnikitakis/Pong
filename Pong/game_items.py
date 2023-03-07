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
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1



    def ball_move(self):
        newy = self.ycor() + self.y_move
        newx = self.xcor() + self.x_move
        self.goto(newx, newy)

    def bounce(self):
        self.y_move *= -1


    def padle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_positon(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
        self.y_move *= -1


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font = ("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()