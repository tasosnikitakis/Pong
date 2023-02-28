from turtle import Screen, Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()



    def create_snake(self):
        for i in range(3):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(y=0, x=(0 - i * 20))
            self.snake_segments.append(snake_segment)

    def move(self):
        for seg_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_number - 1].xcor()
            new_y = self.snake_segments[seg_number - 1].ycor()
            self.snake_segments[seg_number].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)
