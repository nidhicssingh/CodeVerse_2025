import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Creative Chessboard")
screen.bgcolor("gray20")
screen.setup(width=600, height=600)

# Constants
square_size = 60
start_x = -240
start_y = 240
colors = ["white", "black"]

# Create turtle for drawing squares
board = turtle.Turtle()
board.speed(0)
board.penup()
board.hideturtle()

# Draw 8x8 squares
for row in range(8):
    for col in range(8):
        x = start_x + col * square_size
        y = start_y - row * square_size
        board.goto(x, y)
        board.color("black", colors[(row + col) % 2])  # Alternate colors
        board.begin_fill()
        for _ in range(4):
            board.pendown()
            board.forward(square_size)
            board.right(90)
        board.end_fill()
        board.penup()

# Optional: Add labels (creative touch)
label = turtle.Turtle()
label.hideturtle()
label.color("lightblue")
label.penup()
label.speed(0)

files = 'ABCDEFGH'
ranks = '12345678'

# Draw file (A-H) labels
for i in range(8):
    # Bottom
    label.goto(start_x + i * square_size + square_size/2 - 5, start_y - 8*square_size - 20)
    label.write(files[i], align="center", font=("Arial", 10, "bold"))
    # Top
    label.goto(start_x + i * square_size + square_size/2 - 5, start_y + 10)
    label.write(files[i], align="center", font=("Arial", 10, "bold"))

# Draw rank (1-8) labels
for j in range(8):
    # Left
    label.goto(start_x - 20, start_y - j * square_size - square_size/2 + 5)
    label.write(ranks[7-j], align="center", font=("Arial", 10, "bold"))
    # Right
    label.goto(start_x + 8*square_size + 10, start_y - j * square_size - square_size/2 + 5)
    label.write(ranks[7-j], align="center", font=("Arial", 10, "bold"))

# Add glowing border
glow = turtle.Turtle()
glow.pensize(6)
glow.pencolor("gold")
glow.penup()
glow.goto(start_x - 5, start_y + 5)
glow.pendown()
for _ in range(4):
    glow.forward(square_size * 8 + 10)
    glow.right(90)

turtle.done()
