# EmojiFace_YourName.py
import turtle
t = turtle.Turtle()

# Face
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Eyes
for x in [-35, 35]:
    t.penup()
    t.goto(x, 120)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

# Smile
t.penup()
t.goto(-40, 70)
t.setheading(-60)
t.pendown()
t.circle(50, 120)

t.hideturtle()
turtle.done()
