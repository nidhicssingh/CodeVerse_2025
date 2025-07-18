import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Chessboard")
screen.bgcolor("white")

# Create turtle
board = turtle.Turtle()
board.speed(0)
square_size = 50

def draw_square(x, y, color):
    board.penup()
    board.goto(x, y)
    board.pendown()
    board.fillcolor(color)
    board.begin_fill()
    for _ in range(4):
        board.forward(square_size)
        board.right(90)
    board.end_fill()

# Draw the board
start_x = -square_size * 4
start_y = square_size * 4

colors = ["white", "black"]
for row in range(8):
    for col in range(8):
        color = colors[(row + col) % 2]
        draw_square(start_x + col * square_size, start_y - row * square_size, color)

# Hide turtle and display
board.hideturtle()
turtle.done()

