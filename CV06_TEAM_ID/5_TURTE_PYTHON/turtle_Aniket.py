import turtle

# Screen setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("🙂 Slightly Smiling Face")

# Face
face = turtle.Turtle()
face.penup()
face.goto(0, -150)
face.color("gold")
face.begin_fill()
face.circle(150)
face.end_fill()
face.hideturtle()

# Eyes
eyes = turtle.Turtle()
eyes.penup()
eyes.goto(-50, 50)
eyes.dot(20, "black")
eyes.goto(50, 50)
eyes.dot(20, "black")
eyes.hideturtle()

# Smile
smile = turtle.Turtle()
smile.pensize(5)
smile.penup()
smile.goto(-70, -40)
smile.setheading(-60)
smile.pendown()
smile.circle(80, 120)
smile.hideturtle()

# Keep screen open
turtle.done()
