import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("lightblue")

# Create turtle
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(3)

# ---------------------
# HEAD
# ---------------------
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("black", "yellow")
pen.begin_fill()
pen.circle(100)  # Face circle
pen.end_fill()

# ---------------------
# LEFT EYE
# ---------------------
pen.penup()
pen.goto(-35, 30)
pen.setheading(0)
pen.pendown()
pen.color("black", "white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Left eyeball
pen.penup()
pen.goto(-30, 35)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# ---------------------
# RIGHT EYE
# ---------------------
pen.penup()
pen.goto(35, 30)
pen.pendown()
pen.color("black", "white")
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Right eyeball
pen.penup()
pen.goto(40, 35)
pen.pendown()
pen.color("black", "black")
pen.begin_fill()
pen.circle(5)
pen.end_fill()

# ---------------------
# SMILE / MOUTH
# ---------------------
pen.penup()
pen.goto(-40, -20)
pen.setheading(-60)
pen.pendown()
pen.color("black")
pen.circle(50, 120)  # Draw a curved smile

# ---------------------
# NOSE (small triangle)
# ---------------------
pen.penup()
pen.goto(0, 10)
pen.setheading(0)
pen.pendown()
pen.color("black", "orange")
pen.begin_fill()
for _ in range(3):
    pen.forward(20)
    pen.left(120)
pen.end_fill()

# Hide turtle
pen.hideturtle()

# Keep window open
turtle.done()
