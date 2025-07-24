import turtle

# Set up screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Smiley Emoji")

t = turtle.Turtle()
t.speed(3)

# Draw yellow face
t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw left eye
t.penup()
t.goto(-35, 35)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw right eye
t.penup()
t.goto(35, 35)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Draw smiling mouth
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.width(5)
t.pendown()
t.circle(50, 120)

# Hide turtle and finish
t.hideturtle()
turtle.done()
