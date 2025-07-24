import turtle

def draw_rectangle(color, y):
    turtle.penup()
    turtle.goto(-300, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(600)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def draw_chakra():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("navy")
    turtle.circle(50)

    # Draw 24 spokes
    for _ in range(24):
        turtle.penup()
        turtle.goto(0, -50)
        turtle.setheading(_ * (360 / 24))
        turtle.pendown()
        turtle.forward(50)

# Setup
turtle.speed(0)
turtle.bgcolor("white")
turtle.title("Indian Flag")

# Draw flag stripes
draw_rectangle("orange", 100)  # Top saffron band
draw_rectangle("white", 0)     # Middle white band
draw_rectangle("green", -100)  # Bottom green band

# Draw the Ashoka Chakra
draw_chakra()

# Finish
turtle.hideturtle()
turtle.done()
