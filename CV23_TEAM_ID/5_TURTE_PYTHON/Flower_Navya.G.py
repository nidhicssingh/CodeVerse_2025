import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("#40E0D0")  # Nifty turquoise background
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Draw one petal
def draw_petal():
    pen.color("#FFD700", "#FFD700")  # Petal yellow
    pen.begin_fill()
    pen.circle(100, 60)
    pen.left(120)
    pen.circle(100, 60)
    pen.left(120)
    pen.end_fill()

# Draw all petals in circular pattern
def draw_flower():
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(0)
    for _ in range(18):  # 18 petals
        draw_petal()
        pen.right(20)

# Draw center
def draw_center():
    pen.penup()
    pen.goto(0, -50)
    pen.pendown()
    pen.color("#8B4513", "#8B4513")  # Brown center
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()

# Draw stem
def draw_stem():
    pen.penup()
    pen.goto(0, -50)
    pen.setheading(-90)
    pen.pensize(20)
    pen.pencolor("green")
    pen.pendown()
    pen.forward(200)

# Draw a leaf using curve
def draw_leaf(x, y, angle):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.color("green", "green")
    pen.begin_fill()
    pen.circle(60, 60)
    pen.left(120)
    pen.circle(60, 60)
    pen.end_fill()

# Draw all parts
draw_flower()
draw_center()
draw_stem()
draw_leaf(-30, -120, -160)  # Left leaf
draw_leaf(30, -170, -20)    # Right leaf

# Finish
pen.hideturtle()
turtle.done()
