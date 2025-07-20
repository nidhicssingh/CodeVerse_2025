import turtle
import math

# Setup screen
screen = turtle.Screen()
screen.title("Indian National Flag")
screen.bgcolor("white")
flag = turtle.Turtle()
flag.speed(0)

# Function to draw a rectangle
def draw_rectangle(color, x, y, width, height):
    flag.penup()
    flag.goto(x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(width)
        flag.right(90)
        flag.forward(height)
        flag.right(90)
    flag.end_fill()

# Function to draw Ashoka Chakra
def draw_chakra(center_x, center_y, radius):
    chakra = turtle.Turtle()
    chakra.speed(0)
    chakra.pensize(2)
    chakra.color("navy")
    chakra.penup()
    chakra.goto(center_x, center_y - radius)
    chakra.pendown()
    chakra.circle(radius)

    # 24 spokes
    for i in range(24):
        chakra.penup()
        chakra.goto(center_x, center_y)
        chakra.setheading(i * 15)
        chakra.pendown()
        chakra.forward(radius)
    
    chakra.hideturtle()

# Draw the three color bands
width = 600
height = 300
stripe_height = height / 3
start_x = -width / 2
start_y = height / 2

# Saffron
draw_rectangle("#FF9933", start_x, start_y, width, stripe_height)

# White
draw_rectangle("white", start_x, start_y - stripe_height, width, stripe_height)

# Green
draw_rectangle("#138808", start_x, start_y - 2 * stripe_height, width, stripe_height)

# Draw Chakra in center
center_x = 0
center_y = start_y - stripe_height * 1.5
draw_chakra(center_x, center_y, 40)

# Add "Jai Hind"
flag.penup()
flag.goto(0, start_y - height - 40)
flag.color("black")
flag.write("Jai Hind", align="center", font=("Arial", 24, "bold"))

flag.hideturtle()
turtle.done()
