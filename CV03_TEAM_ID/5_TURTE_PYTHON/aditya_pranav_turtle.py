import turtle

screen = turtle.Screen()
screen.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(3)


pen.penup()
pen.goto(-50, -50)
pen.pendown()
pen.fillcolor("yellow")
pen.begin_fill()
for _ in range(4):
    pen.forward(100)
    pen.left(90)
pen.end_fill()


pen.penup()
pen.goto(-50, 50)
pen.pendown()
pen.fillcolor("brown")
pen.begin_fill()
pen.goto(0, 100)
pen.goto(50, 50)
pen.goto(-50, 50)
pen.end_fill()

# Draw the door
pen.penup()
pen.goto(-10, -50)
pen.pendown()
pen.fillcolor("red")
pen.begin_fill()
for _ in range(2):
    pen.forward(20)
    pen.left(90)
    pen.forward(40)
    pen.left(90)
pen.end_fill()

pen.hideturtle()
turtle.done()