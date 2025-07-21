import turtle

def draw_petals():
    turtle.color("yellow")
    for _ in range(24):  # 24 petals
        turtle.begin_fill()
        turtle.circle(100, 60)
        turtle.left(120)
        turtle.circle(100, 60)
        turtle.left(15)
        turtle.end_fill()

def draw_center():
    turtle.penup()
    turtle.goto(0, -50)
    turtle.pendown()
    turtle.color("saddlebrown")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

def draw_stem():
    turtle.penup()
    turtle.goto(0, -100)
    turtle.setheading(-90)
    turtle.color("green")
    turtle.pensize(10)
    turtle.pendown()
    turtle.forward(200)

# Setup
turtle.speed(0)
turtle.bgcolor("skyblue")
turtle.title("Sunflower Drawing")

draw_petals()
draw_center()
draw_stem()

turtle.hideturtle()
turtle.done()