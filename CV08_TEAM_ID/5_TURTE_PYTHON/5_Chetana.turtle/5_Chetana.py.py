import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.penup()


square_size = 50

for row in range(8):
    for col in range(8):
        x = col * square_size - 200
        y = row * square_size - 200
        pen.goto(x, y)
        pen.pendown()
        
        
        if (row + col) % 2 == 0:
            pen.fillcolor("white")
        else:
            pen.fillcolor("black")

       
        pen.begin_fill()
        for _ in range(4):
            pen.forward(square_size)
            pen.left(90)
        pen.end_fill()
        pen.penup()


screen.exitonclick()
