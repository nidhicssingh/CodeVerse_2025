import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Happy Emoji Face")
pen = turtle.Turtle()
pen.speed(0)

# Helper function to draw filled circles
def draw_circle(color, radius, x, y):
    pen.penup()
    pen.goto(x, y - radius)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

# Draw face
draw_circle("yellow", 100, 0, 0)

# Draw eyes (white + centered black pupils)
draw_circle("white", 15, -30, 40)   # Left eye
draw_circle("black", 5, -30, 40)    # Left pupil (centered)

draw_circle("white", 15, 30, 40)    # Right eye
draw_circle("black", 5, 30, 40)     # Right pupil (centered)

# Draw smile
pen.penup()
pen.goto(-40, -20)
pen.setheading(-60)
pen.pendown()
pen.pensize(5)
pen.color("black")
pen.circle(50, 120)

# Done
pen.hideturtle()
turtle.done()
