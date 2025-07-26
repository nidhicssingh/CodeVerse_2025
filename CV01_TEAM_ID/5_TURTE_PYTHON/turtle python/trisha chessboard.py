import turtle

board = turtle.Turtle()
board.speed(0)
screen = turtle.Screen()
screen.bgcolor("white")

square_size = 50
colors = ["white", "black"]

# Draw 8x8 grid
for row in range(8):
    for col in range(8):
        board.penup()
        board.goto(col * square_size - 200, row * square_size - 200)
        board.pendown()
        board.begin_fill()
        board.color(colors[(row + col) % 2])
        for _ in range(4):
            board.forward(square_size)
            board.right(90)
        board.end_fill()

board.hideturtle()
turtle.done()
