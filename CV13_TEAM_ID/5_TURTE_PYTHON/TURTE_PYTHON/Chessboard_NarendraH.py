import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
board = turtle.Turtle()
board.speed(0)

# Constants
square_size = 50
start_x = -200
start_y = 200
colors = ["white", "black"]

# Draw the chessboard
for row in range(8):
    for col in range(8):
        board.penup()
        x = start_x + col * square_size
        y = start_y - row * square_size
        board.goto(x, y)
        board.pendown()
        
        # Choose color based on position
        color_index = (row + col) % 2
        board.fillcolor(colors[color_index])
        board.begin_fill()

        for _ in range(4):
            board.forward(square_size)
            board.right(90)

        board.end_fill()

# Hide turtle and keep window open
board.hideturtle()
turtle.done()
