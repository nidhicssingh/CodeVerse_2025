import turtle

t = turtle.Turtle()
t.speed(3)

# Face
t.penup()
t.goto(0, -100)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

# Eyes
t.penup()
t.goto(-35, 20)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(35, 20)
t.pendown()
t.begin_fill()
t.circle(10)
t.end_fill()

# Smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.width(5)
t.circle(50, 120)

t.hideturtle()
turtle.done()





