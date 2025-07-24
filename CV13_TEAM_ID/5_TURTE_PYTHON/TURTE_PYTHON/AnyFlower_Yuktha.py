import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Turtle Rose Flower")

# Set up turtle
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.pensize(2)
pen.hideturtle()

# Function to draw a petal shape
def draw_petal():
    pen.circle(100, 60)     # Draw first arc
    pen.left(120)
    pen.circle(100, 60)     # Draw second arc
    pen.left(120)

# Draw the full rose flower
def draw_flower(petals=36):
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    for _ in range(petals):
        draw_petal()
        pen.left(360 / petals)

# Draw flower center
def draw_center():
    pen.penup()
    pen.goto(0, -20)
    pen.color("yellow")
    pen.pendown()
    pen.begin_fill()
    pen.circle(20)
    pen.end_fill()

# Draw leaves
def draw_leaves():
    pen.penup()
    pen.goto(0, -150)
    pen.setheading(-60)
    pen.color("green")
    pen.pendown()
    for _ in range(2):  # two leaves
        pen.begin_fill()
        pen.circle(100, 60)
        pen.left(120)
        pen.circle(100, 60)
        pen.end_fill()
        pen.setheading(60)

# Run drawing functions
draw_flower(36)
draw_center()
draw_leaves()

# Keep window open
turtle.done()
