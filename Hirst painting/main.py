# import colorgram
import turtle
from turtle import Turtle, Screen
import random

#
# colors = colorgram.extract("hirst-1.jpg", 40)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)
#
# print(color_list)

color_list = [(236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129),
              (147, 85, 53),
              (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23),
              (120, 70, 93),
              (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94),
              (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173),
              (160, 209, 191),
              (67, 86, 23), (219, 206, 8), (181, 186, 213), (46, 72, 57), (168, 201, 212), (100, 137, 144)]

turtle.colormode(255)
y = 50
toto = Turtle()
toto.hideturtle()
toto.setheading(225)
toto.penup()

toto.forward(300)
toto.setheading(0)
num_of_dots = 100
toto.speed("fastest")

# for column in range(10):

for dot_count in range(1, num_of_dots+1):
    color = random.choice(color_list)
    toto.dot(20, color)

    toto.forward(50)

    if dot_count % 10 == 0:
        toto.setheading(90)

        toto.forward(50)
        toto.setheading(180)
        toto.forward(500)
        toto.setheading(0)

my_screen = Screen()
my_screen.exitonclick()
