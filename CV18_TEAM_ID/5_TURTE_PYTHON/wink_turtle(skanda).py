import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("😉 Emoji - Only One Eyebrow Like Umbrella")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# Face
def draw_face():
    t.penup()
    t.goto(0, -200)
    t.color("orange", "yellow")
    t.begin_fill()
    t.circle(200)
    t.end_fill()

# Left Eye (open)
def draw_left_eye():
    t.penup()
    t.goto(-70, 60)
    t.color("black")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# Right Eye (wink)
def draw_right_eye():
    t.penup()
    t.goto(50, 65)
    t.setheading(0)
    t.pensize(6)
    t.pendown()
    t.forward(30)
    t.penup()

# ✅ Only one eyebrow — left side (above circle eye)
def draw_left_eyebrow():
    t.pensize(5)
    t.penup()
    t.goto(-90, 105)     # starting above left eye
    t.setheading(10)
    t.pendown()
    t.circle(40, 40)     # curved like umbrella
    t.penup()


# Smile
def draw_smile():
    t.pensize(8)
    t.penup()
    t.goto(-65, -60)
    t.setheading(-60)
    t.pendown()
    t.circle(85, 120)
    t.penup()

# Draw it all
draw_face()
draw_left_eye()
draw_right_eye()
draw_left_eyebrow()
draw_smile()

turtle.done()