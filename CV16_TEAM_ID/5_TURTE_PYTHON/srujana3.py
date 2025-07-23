import turtle

def draw_square(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()

def draw_base_zone():
    # Red
    draw_square("red", -200, 100)
    # Green
    draw_square("green", 100, 100)
    # Yellow
    draw_square("yellow", -200, -200)
    # Blue
    draw_square("blue", 100, -200)

def draw_center_star():
    turtle.penup()
    turtle.goto(-50, -50)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(100)
        turtle.right(90)
    turtle.end_fill()
    turtle.color("black")
    turtle.write("★", font=("Arial", 32, "bold"), align="center")

def draw_path_strips():
    # Horizontal strips
    turtle.color("gray")
    for i in range(6):
        draw_square("white", -100 + i*20, 50)
        draw_square("white", -100 + i*20, -70)

    # Vertical strips
    for i in range(6):
        draw_square("white", -70, 100 - i*20)
        draw_square("white", 50, 100 - i*20)

# Setup
turtle.speed(0)
turtle.bgcolor("lightgray")
turtle.title("Ludo Board")

draw_base_zone()
draw_path_strips()
draw_center_star()

turtle.hideturtle()
turtle.done()