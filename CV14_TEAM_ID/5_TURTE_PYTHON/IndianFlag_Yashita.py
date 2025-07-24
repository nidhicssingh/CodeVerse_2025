import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(3)

# Function to draw a rectangle
def draw_rectangle(color, y):
    pen.penup()
    pen.goto(-150, y)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(300)
        pen.right(90)
        pen.forward(50)
        pen.right(90)
    pen.end_fill()

# Draw stripes
draw_rectangle("orange", 100)  # Top
draw_rectangle("white", 50)    # Middle
draw_rectangle("green", 0)     # Bottom

# Draw centered Ashoka Chakra
pen.penup()
pen.goto(0, 10)  # Adjusted from 25 to 10
pen.setheading(0)
pen.pendown()
pen.color("blue")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Hide turtle
pen.hideturtle()
turtle.done()
