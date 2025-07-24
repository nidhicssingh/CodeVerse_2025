import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("skyblue")
t = turtle.Turtle()
t.speed(5)

# Function to draw circle with color
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Head
draw_circle("yellow", 100, 0, -20)

# Eyes
draw_circle("white", 15, -35, 70)
draw_circle("white", 15, 35, 70)
draw_circle("black", 5, -35, 85)
draw_circle("black", 5, 35, 85)

# Smile
t.penup()
t.goto(-40, 40)
t.setheading(-60)
t.pendown()
t.width(5)
t.circle(50, 120)

# Body
t.width(1)
t.color("orange")
t.penup()
t.goto(0, -120)
t.pendown()
t.begin_fill()
t.circle(60)
t.end_fill()

# Arms
t.penup()
t.goto(-60, -80)
t.pendown()
t.color("black")
t.width(4)
t.goto(-120, -20)

t.penup()
t.goto(60, -80)
t.pendown()
t.goto(120, -20)

# Legs
t.penup()
t.goto(-30, -180)
t.setheading(-90)
t.pendown()
t.forward(50)

t.penup()
t.goto(30, -180)
t.setheading(-90)
t.pendown()
t.forward(50)

# Hide turtle
t.hideturtle()

# Keep window open
turtle.done()
