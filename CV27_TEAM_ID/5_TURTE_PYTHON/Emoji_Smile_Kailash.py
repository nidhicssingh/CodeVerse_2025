import turtle

def draw_circle(color, x, y, radius):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_eye(x, y):
    draw_circle("white", x, y, 30)
    draw_circle("black", x, y, 10)

def draw_smile():
    turtle.penup()
    turtle.goto(-40, -20)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(50, 120)

def draw_face():
    draw_circle("peachpuff", 0, 0, 100)  # Head
    draw_eye(-35, 40)  # Left eye
    draw_eye(35, 40)   # Right eye
    draw_smile()       # Smile

# Setup
turtle.speed(0)
turtle.bgcolor("lightblue")
turtle.title("Cartoon Character Face")

draw_face()

turtle.hideturtle()
turtle.done()