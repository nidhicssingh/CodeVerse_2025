import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
emoji = turtle.Turtle()
emoji.speed(20)

# --- Draw face (yellow circle) ---
emoji.penup()
emoji.goto(0, -200)
emoji.pendown()
emoji.color("yellow")
emoji.begin_fill()
emoji.circle(200)
emoji.end_fill()

# --- Draw left eye ---
emoji.penup()
emoji.goto(-70, 50)
emoji.pendown()
emoji.color("black")
emoji.begin_fill()
emoji.circle(20)
emoji.end_fill()

# --- Draw right eye ---
emoji.penup()
emoji.goto(70, 50)
emoji.pendown()
emoji.begin_fill()
emoji.circle(20)
emoji.end_fill()

# --- Draw mouth (sad) ---
emoji.penup()
emoji.goto(-70, -70)
emoji.setheading(-60)
emoji.width(5)
emoji.pendown()
emoji.circle(80, 120)

# --- Draw tear drop ---
emoji.penup()
emoji.goto(70, 20)
emoji.color("blue")
emoji.begin_fill()
emoji.pendown()
emoji.circle(10)
emoji.goto(80, -30)
emoji.circle(10)
emoji.goto(70, 20)
emoji.end_fill()

# Hide turtle and finish
emoji.hideturtle()
turtle.done()

