import turtle as t
from turtle import Screen
import random
import colorgram
screen = Screen()
screen.colormode(255)
# color_list = []
# colors = colorgram.extract("hirst.jpg", 30)
# for color in colors:
#     color_tuple = (color.rgb.r, color.rgb.g,color.rgb.b)
#     color_list.append(color_tuple)

color_list = [(252, 138, 52), (49, 171, 90), (120, 185, 140), (249, 75, 110), (247, 223, 64), (250, 77, 50), (120, 120, 67), (226, 212, 16), (19, 37, 103), (3, 111, 166), (156, 76, 130), (52, 148, 24), (254, 167, 160), (2, 59, 126), (199, 192, 28), (223, 122, 146), (130, 166, 194), (245, 159, 176), (161, 211, 175), (51, 178, 183), (110, 121, 157), (176, 189, 216), (152, 208, 218)]
# color_list was extracted from line 7 - 11
x = -230
y = -230
t.pensize(20)
gap = 50
t.speed(10)

screen.setup (width=800, height=800)

def go_to_starting_pos():
    t.pu()
    t.goto(x, -300)
    t.pd()

def move():
    t.dot(20, random.choice(color_list))
    t.pu()
    t.forward(50)

go_to_starting_pos()
for num in range(10):
    t.teleport(x, y + (num * 50))
    for n in range(10):
        move()

screen.exitonclick()