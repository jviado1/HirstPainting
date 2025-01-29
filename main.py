import turtle as t
from turtle import Screen
import random
import colorgram


color_list = []
colors = colorgram.extract("hirst.jpg", 20)
for color in colors:
    color_tuple = (color.rgb.r, color.rgb.g,color.rgb.b)
    color_list.append(color_tuple)

print(color_list)

screen = Screen()
screen.exitonclick()