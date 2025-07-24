import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(7)

def draw_circle(x, y, radius, color):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

draw_circle(0, -100, 100, "saddlebrown")  

draw_circle(-80, 80, 40, "saddlebrown")  
draw_circle(80, 80, 40, "saddlebrown")   
draw_circle(-80, 90, 20, "pink")         
draw_circle(80, 90, 20, "pink")          

draw_circle(-30, 20, 20, "white")
draw_circle(30, 20, 20, "white")
draw_circle(-30, 30, 8, "black")
draw_circle(30, 30, 8, "black")

draw_circle(0, 0, 10, "black")

pen.penup()
pen.goto(-40, -40)
pen.setheading(-60)
pen.pendown()
pen.width(4)
pen.circle(40, 120)

def draw_whiskers():
    for y in [-15, -10, -5]:
        pen.penup()
        pen.goto(-20, y)
        pen.setheading(180)
        pen.pendown()
        pen.forward(30)

    for y in [-15, -10, -5]:
        pen.penup()
        pen.goto(20, y)
        pen.setheading(0)
        pen.pendown()
        pen.forward(30)

draw_whiskers()

pen.penup()
pen.goto(0, -200)
pen.setheading(0)
pen.color("saddlebrown")
pen.begin_fill()
pen.pendown()
pen.circle(60)
pen.end_fill()

draw_circle(0, -180, 30, "peachpuff")

def draw_arm(x, y, angle):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    pen.width(8)
    pen.forward(50)

draw_arm(-60, -160, 220)  # Left arm
draw_arm(60, -160, -40)   # Right arm

draw_circle(-30, -270, 15, "saddlebrown")  # Left foot
draw_circle(30, -270, 15, "saddlebrown")   # Right foot


pen.hideturtle()

turtle.done()
