import turtle
import time

screen = turtle.Screen()
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)

# Function to draw a petal
def draw_petal(t, radius, angle):
    for _ in range(2):
        t.circle(radius, angle)
        t.left(180 - angle)

# Blooming petals one by one
pen.color("orange", "yellow")
pen.penup()
pen.goto(0, 0)
pen.pendown()

for _ in range(36):
    pen.begin_fill()
    draw_petal(pen, 100, 60)
    pen.end_fill()
    pen.left(10)
    time.sleep(0.05)  # Animation delay

# Draw center
pen.penup()
pen.goto(0, -40)
pen.setheading(0)
pen.pendown()
pen.color("brown")
pen.begin_fill()
pen.circle(40)
pen.end_fill()

# Draw stem
pen.penup()
pen.goto(0, -80)
pen.setheading(-90)
pen.color("darkgreen")
pen.pensize(20)
pen.pendown()
pen.forward(200)

# Draw left leaf
pen.penup()
pen.goto(0, -150)
pen.setheading(220)
pen.pensize(2)
pen.color("green")
pen.begin_fill()
draw_petal(pen, 60, 60)
pen.end_fill()

# Draw right leaf
pen.penup()
pen.goto(0, -170)
pen.setheading(-40)
pen.begin_fill()
draw_petal(pen, 60, 60)
pen.end_fill()

# Hide turtle
pen.hideturtle()

# Wait for user to close
screen.exitonclick()
