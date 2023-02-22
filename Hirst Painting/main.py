import colorgram
import turtle as t
import random


timy = t.Turtle()
t.colormode(255)

# Extract colors from an image.
#colors = colorgram.extract('image.jpg', 20)
#extracted_colors = []
#for color in colors:
#    rgb = color.rgb
#    red = rgb[0]
#    blue = rgb[1]
#    green = rgb[2]
#    color_tupple = (red, blue, green)
#    extracted_colors.append(color_tupple)

color_list = [(198, 12, 32), (250, 238, 16), (39, 76, 190), (38, 217, 69), (238, 226, 5),
              (229, 159, 45), (27, 39, 157), (215, 75, 12), (15, 154, 15), (199, 14, 11), (243, 34, 166),
              (230, 17, 122), (70, 9, 30), (241, 246, 251), (61, 15, 8), (10, 97, 62)]

timy.penup()
def forward_and_dots(steps):
    for n in range(steps):
        timy.color(random.choice(color_list))
        timy.dot(20)
        timy.forward(50)


def left_turn():
    timy.color(random.choice(color_list))
    timy.dot(20)
    timy.left(90)
    timy.forward(50)
    timy.left(90)

def right_turn():
    timy.color(random.choice(color_list))
    timy.dot(20)
    timy.right(90)
    timy.forward(50)
    timy.right(90)



for x in range(5):
    forward_and_dots(9)
    left_turn()
    forward_and_dots(9)
    right_turn()

screen = t.Screen()
screen.exitonclick()

