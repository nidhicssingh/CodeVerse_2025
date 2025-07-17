import turtle
turtle.title("Ramanee Kaanth's Chessboard")
s = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("white")
t.penup()
t.goto(-200, 200)
t.pendown()
colors = ["black", "white"]
for row in range(8):
    for col in range(8):
        x = -200 + col*50
        y = 200 - row*50
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.fillcolor(colors[(row + col) % 2])
        t.begin_fill()
        for _ in range(4):
            t.forward(50)
            t.right(90)
        t.end_fill()
t.hideturtle()
turtle.done()
