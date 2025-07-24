import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
screen.colormode(255)

pen = turtle.Turtle()
pen.speed(5)

# Helper function
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Colors
blue = (0, 191, 255)
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Head
draw_circle(blue, 100, 0, -100)  # Blue head
draw_circle(white, 85, 0, -85)   # White face inside

# Eyes
draw_circle(white, 15, -25, 20)
draw_circle(white, 15, 25, 20)
draw_circle(black, 5, -25, 35)
draw_circle(black, 5, 25, 35)

# Nose
draw_circle(red, 7, 0, 20)

# Smile
pen.penup()
pen.goto(-35, 0)
pen.setheading(-60)
pen.color(black)
pen.width(2)
pen.pendown()
pen.circle(40, 120)

# Vertical line from nose
pen.penup()
pen.goto(0, 20)
pen.setheading(-90)
pen.pendown()
pen.forward(25)

# Whiskers (Left side)
pen.width(2)
def draw_whisker(x, y, angle):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    pen.forward(40)

for y in [30, 20, 10]:
    draw_whisker(-60, y, 0)

# Whiskers (Right side)
for y in [30, 20, 10]:
    draw_whisker(60, y, 180)

pen.hideturtle()
turtle.done()
