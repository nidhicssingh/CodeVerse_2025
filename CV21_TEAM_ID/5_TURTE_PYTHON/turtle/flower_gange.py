import math
import turtle

# Setup
turtle.bgcolor("black")

# Draw stem first so it's behind
stem = turtle.Turtle()
stem.hideturtle()
stem.color("green")
stem.pensize(14)
stem.penup()
stem.goto(0, -250)  # Start lower for longer stem
stem.setheading(90)  # Pointing up
stem.pendown()
stem.forward(250)  # Draw up to the base of the flower

# Flower turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.speed(0)
flower.fillcolor("brown")

phi = 137.508 * (math.pi / 180.0)

# Draw petals and center
for i in range(160 + 40):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)

    flower.penup()
    flower.goto(x, y)
    flower.setheading(i * 137.508)
    flower.pendown()

    if i < 160:
        flower.stamp()
    else:
        flower.fillcolor("yellow")
        flower.begin_fill()
        flower.right(20)
        flower.forward(70)
        flower.left(40)
        flower.forward(70)
        flower.left(140)
        flower.forward(70)
        flower.left(40)
        flower.forward(70)
        flower.end_fill()

flower.hideturtle()
turtle.done()

