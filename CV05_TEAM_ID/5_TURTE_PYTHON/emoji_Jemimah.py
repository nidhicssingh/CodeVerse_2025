import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(5)

# Function to draw circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw face (yellow circle)
draw_circle("yellow", 100, 0, -100)

# Draw left eye (open)
draw_circle("black", 10, -35, 20)

# Draw right eye (wink - a horizontal line)
t.penup()
t.goto(30, 20)
t.setheading(0)
t.pendown()
t.pensize(4)
t.forward(20)

# Draw smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.width(5)
t.pendown()
t.circle(50, 120)  # big smile arc

t.hideturtle()
turtle.done()