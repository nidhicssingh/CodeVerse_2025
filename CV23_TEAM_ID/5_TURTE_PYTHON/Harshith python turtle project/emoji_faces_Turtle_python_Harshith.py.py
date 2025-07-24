import turtle

def draw_circle(x, y, radius, color="yellow", outline="black"):
    turtle.penup()
    turtle.goto(x, y - radius)  # Adjust so center of circle is at (x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color(outline, color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_eye(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

def draw_smile(x, y):
    turtle.penup()
    turtle.goto(x - 25, y - 20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(30, 120)

def draw_sad(x, y):
    turtle.penup()
    turtle.goto(x - 25, y - 5)
    turtle.setheading(60)
    turtle.pendown()
    turtle.circle(-30, 120)

def draw_wink_eye(x, y):
    turtle.penup()
    turtle.goto(x - 10, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.pensize(3)
    turtle.forward(20)
    turtle.pensize(1)

def draw_smiley_face(x, y):
    draw_circle(x, y, 50)
    draw_eye(x - 20, y + 20)
    draw_eye(x + 20, y + 20)
    draw_smile(x, y)

def draw_sad_face(x, y):
    draw_circle(x, y, 50, color="lightblue")
    draw_eye(x - 20, y + 20)
    draw_eye(x + 20, y + 20)
    draw_sad(x, y)

def draw_wink_face(x, y):
    draw_circle(x, y, 50, color="lightyellow")
    draw_eye(x - 20, y + 20)
    draw_wink_eye(x + 20, y + 20)
    draw_smile(x, y)

# Setup
turtle.speed(3)
turtle.bgcolor("white")
turtle.title("Turtle Emoji Faces")

# Draw emojis side by side
draw_smiley_face(-200, 0)
draw_sad_face(0, 0)
draw_wink_face(200, 0)

turtle.hideturtle()
turtle.done()

