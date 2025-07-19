import turtle

t = turtle.Turtle()
t.speed(5)

screen = turtle.Screen()
screen.bgcolor("white")
 
def draw_box(color):
    t.fillcolor(color)
    t.begin_fill()
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.end_fill()
t.penup()
t.goto(-200, 200)
t.pendown()

for row in range(8):
    for box in range(8):
        if (row + box) % 2 == 0:
            draw_box("white")
        else:
            draw_box("black")
        t.forward(50)

    t.backward(400) 
    t.right(90)
    t.forward(50)   
    t.left(90)

t.hideturtle()

screen.exitonclick()