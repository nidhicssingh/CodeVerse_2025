import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(5)

# --- Draw Yellow Face Circle ---
pen.penup()
pen.goto(0, -100)
pen.pendown()
pen.color("#FFD700")  # Bright yellow
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# --- Left Eye (Open Circle) ---
pen.penup()
pen.goto(-35, 30)
pen.pendown()
pen.color("black")
pen.begin_fill()
pen.circle(10)
pen.end_fill()

# --- Right Eye (Winking Line) ---
pen.penup()
pen.goto(30, 35)
pen.setheading(0)
pen.pendown()
pen.width(4)
pen.forward(20)

# --- Smile ---
pen.penup()
pen.goto(-40, -20)
pen.setheading(-60)
pen.width(6)
pen.pendown()
pen.circle(50, 120)  # Draw curved smile

# Hide turtle
pen.hideturtle()
turtle.done()
