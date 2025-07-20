import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)

# Move to center
pen.penup()
pen.goto(0, 0)
pen.pendown()

# Realistic rose pattern
pen.color("red")
pen.begin_fill()

for i in range(360):
    angle = i * math.pi / 180
    r = 200 * math.sin(4 * angle)  # 4 petals (sin(4θ) is realistic)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    pen.goto(x, y)

pen.end_fill()

# Add green stem
pen.penup()
pen.goto(0, -50)
pen.setheading(-90)
pen.color("green")
pen.pendown()
pen.pensize(10)
pen.forward(300)

# Add leaf (left)
pen.penup()
pen.goto(0, -150)
pen.setheading(160)
pen.color("green")
pen.begin_fill()
pen.circle(100, 60)
pen.left(120)
pen.circle(100, 60)
pen