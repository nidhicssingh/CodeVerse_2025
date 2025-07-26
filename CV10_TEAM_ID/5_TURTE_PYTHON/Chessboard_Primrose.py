import turtle

def draw_chessboard():
    screen = turtle.Screen()
    screen.bgcolor("white")
    board = turtle.Turtle()
    board.speed(0)
    board.penup()

    square_size = 50
    start_x, start_y = -200, 200  # Top-left corner of the board

    colors = ["white", "black"]

    for row in range(8):
        for col in range(8):
            x = start_x + col * square_size
            y = start_y - row * square_size
            board.goto(x, y)
            board.fillcolor(colors[(row + col) % 2])
            board.begin_fill()
            for _ in range(4):
                board.pendown()
                board.forward(square_size)
                board.right(90)
            board.end_fill()
            board.penup()

    board.hideturtle()
    screen.mainloop()

draw_chessboard()
