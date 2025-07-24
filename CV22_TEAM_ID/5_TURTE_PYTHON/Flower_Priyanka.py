from turtle import *
import colorsys


bgcolor("black")
speed(0)
pensize(2)
h = 0


for i in range(120):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    color(c)
    h += 0.008

    forward(i * 3)
    left(59)
    forward(i * 3)
    left(59)
    forward(i * 3)
    left(59)
    left(15)

hideturtle()
done()
