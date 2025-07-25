import turtle

screen = turtle.Screen()
screen.title("Indian Flag - Better Proportions")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)

flag = turtle.Turtle()
flag.speed(0)
flag.pensize(2)

# Adjusted flag width and height
FLAG_WIDTH = 360   # reduced from 540
FLAG_HEIGHT = 60

# Function to draw a rectangle stripe
def draw_stripe(color, y):
    flag.penup()
    flag.goto(-180, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(FLAG_WIDTH)
        flag.right(90)
        flag.forward(FLAG_HEIGHT)
        flag.right(90)
    flag.end_fill()

# Draw flagpole
def draw_flagpole():
    pole = turtle.Turtle()
    pole.speed(0)
    pole.color("gray20")
    pole.pensize(10)
    pole.penup()
    pole.goto(-180, 180)
    pole.pendown()
    pole.goto(-180, -150)
    pole.hideturtle()

# Draw stand/base
def draw_base():
    base = turtle.Turtle()
    base.speed(0)
    base.color("black")
    base.penup()
    base.goto(-210, -150)
    base.pendown()
    base.begin_fill()
    for _ in range(2):
        base.forward(60)
        base.right(90)
        base.forward(20)
        base.right(90)
    base.end_fill()
    base.hideturtle()

# Draw flag stripes
draw_flagpole()
draw_base()
draw_stripe("#FF9933", 180)   # Saffron
draw_stripe("white", 120)     # White
draw_stripe("#138808", 60)    # Green

# Draw Ashoka Chakra in the center of white stripe
chakra = turtle.Turtle()
chakra.speed(0)
chakra.pensize(2)
chakra.color("#000088")

# Centered according to new flag size
center_x = -180 + FLAG_WIDTH / 2  # middle of the flag width
center_y = 120 - (FLAG_HEIGHT / 2)  # middle of the white band

# Draw outer circle
chakra.penup()
chakra.goto(center_x, center_y - 30)  # radius = 30
chakra.pendown()
chakra.circle(30)

# Draw 24 spokes
for i in range(24):
    chakra.penup()
    chakra.goto(center_x, center_y)
    chakra.setheading(i * 15)
    chakra.forward(30)
    chakra.pendown()
    chakra.backward(30)

chakra.hideturtle()

# Done
turtle.done()