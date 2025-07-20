import turtle
screen = turtle.Screen()
screen.title("Indian Flag 🇮🇳")
screen.bgcolor("skyblue")

flag = turtle.Turtle()
flag.speed(2)
def draw_rectangle(color, y):
    flag.penup()
    flag.goto(-180, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()

    for _ in range(2):
        flag.forward(360)
        flag.right(90)
        flag.forward(50)
        flag.right(90)
    flag.end_fill()

draw_rectangle("#FF9933", 100)   # Saffron
draw_rectangle("white", 50)      # White
draw_rectangle("#138808", 0)     # Green
chakra = turtle.Turtle()
chakra.speed(0)
chakra.color("navy")
chakra.pensize(1)
chakra.penup()
chakra.goto(0, 0)  # y = 0 so that radius goes 25 units up to 25 (centered)
chakra.setheading(0)
chakra.pendown()
chakra.circle(25)
# Draw 24 spokes from center at (0, 25)
chakra.penup()
chakra.goto(0, 25)
chakra.setheading(0)
for _ in range(24):
    chakra.pendown()
    chakra.forward(25)
    chakra.backward(25)
    chakra.left(15)
    chakra.penup()
pole = turtle.Turtle()
pole.color("black")
pole.pensize(5)
pole.penup()
pole.goto(-180, 100)
pole.setheading(-90)
pole.pendown()
pole.forward(300)

flag.hideturtle()
chakra.hideturtle()
pole.hideturtle()

turtle.done()