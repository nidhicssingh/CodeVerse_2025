import turtle

# Set up turtle
screen = turtle.Screen()
screen.bgcolor("white")
wink = turtle.Turtle()
wink.speed(5)

# Draw face (circle)
wink.penup()
wink.goto(0, -100)
wink.pendown()
wink.color("gold")
wink.begin_fill()
wink.circle(100)
wink.end_fill()

# Draw left eye (circle)
wink.penup()
wink.goto(-35, 20)
wink.pendown()
wink.color("black")
wink.begin_fill()
wink.circle(10)
wink.end_fill()

# Draw right eye (wink - line)
wink.penup()
wink.goto(25, 20)
wink.setheading(0)
wink.pensize(5)
wink.pendown()
wink.forward(20)

# Draw smile
wink.penup()
wink.goto(-40, -20)
wink.setheading(-60)
wink.pensize(7)
wink.pendown()
wink.circle(50, 120)  # (radius, extent)

wink.hideturtle()
turtle.done()
