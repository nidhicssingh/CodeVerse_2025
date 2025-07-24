import turtle

screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("skyblue")
screen.setup(width=1000, height=700)

flag = turtle.Turtle()
flag.speed(0)
flag.hideturtle()

flag_x = -200
flag_y = 150
flag_width = 450
flag_height = 300
stripe_height = flag_height / 3

pole = turtle.Turtle()
pole.penup()
pole.goto(flag_x - 10, flag_y + 10)
pole.pendown()
pole.pensize(10)
pole.color("black")
pole.setheading(-90)
pole.forward(500)
pole.hideturtle()

def draw_stripe(color, y):
    flag.penup()
    flag.goto(flag_x, y)
    flag.pendown()
    flag.color(color)
    flag.begin_fill()
    for _ in range(2):
        flag.forward(flag_width)
        flag.right(90)
        flag.forward(stripe_height)
        flag.right(90)
    flag.end_fill()

draw_stripe("orange", flag_y)
draw_stripe("white", flag_y - stripe_height)
draw_stripe("green", flag_y - 2 * stripe_height)

chakra = turtle.Turtle()
chakra.speed(0)
chakra.color("navy")
chakra.pensize(2)
chakra.penup()

center_x = flag_x + flag_width / 2
center_y = flag_y - stripe_height * 1.5
chakra.goto(center_x, center_y - 30)
chakra.pendown()
chakra.circle(30)  

chakra.penup()
chakra.goto(center_x, center_y)
chakra.setheading(0)

for _ in range(24):
    chakra.forward(30)
    chakra.pendown()
    chakra.backward(30)
    chakra.left(15)
    chakra.penup()
    chakra.goto(center_x, center_y)

chakra.dot(5)
chakra.hideturtle()

base = turtle.Turtle()
base.color("gray")
base.penup()
base.goto(flag_x - 50, -350)
base.pendown()
base.begin_fill()
base.forward(100)
base.right(90)
base.forward(20)
base.right(90)
base.forward(200)
base.left(90)
base.forward(20)
base.left(90)
base.forward(200)
base.right(90)
base.forward(20)
base.right(90)
base.forward(100)
base.end_fill()
base.hideturtle()

label = turtle.Turtle()
label.hideturtle()
label.penup()
label.color("darkblue")
label.goto(center_x, -400)
label.write("भारत का राष्ट्रीय ध्वज", align="center", font=("Arial", 20, "bold"))

turtle.done()
