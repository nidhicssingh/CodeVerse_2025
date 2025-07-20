import turtle

# Constants
square_size = 60
board_size = 8
start_x = -240
start_y = 240

# Create the screen
screen = turtle.Screen()
screen.title("Advanced Chess Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)

# Turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.hideturtle()
drawer.penup()

# Turtle for pieces
pieces_drawer = turtle.Turtle()
pieces_drawer.speed(0)
pieces_drawer.hideturtle()
pieces_drawer.penup()

# Board representation (using unicode)
board = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟"]*8,
    [""]*8,
    [""]*8,
    [""]*8,
    [""]*8,
    ["♙"]*8,
    ["♖","♘","♗","♕","♔","♗","♘","♖"]
]

selected_piece = None
selected_pos = None

def draw_square(x, y, color):
    drawer.goto(x, y)
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.pendown()
        drawer.forward(square_size)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

def draw_board():
    drawer.clear()
    for row in range(board_size):
        for col in range(board_size):
            x = start_x + col * square_size
            y = start_y - row * square_size
            color = "white" if (row + col) % 2 == 0 else "gray"
            draw_square(x, y, color)
    draw_pieces()

def draw_pieces():
    pieces_drawer.clear()
    for row in range(board_size):
        for col in range(board_size):
            piece = board[row][col]
            if piece:
                x = start_x + col * square_size + square_size / 4
                y = start_y - row * square_size - square_size * 0.75
                pieces_drawer.goto(x, y)
                pieces_drawer.write(piece, font=("Arial", 28, "normal"))

def get_board_position(x, y):
    col = int((x - start_x) // square_size)
    row = int((start_y - y) // square_size)
    if 0 <= row < 8 and 0 <= col < 8:
        return row, col
    return None

def on_click(x, y):
    global selected_piece, selected_pos
    pos = get_board_position(x, y)
    if not pos:
        return

    row, col = pos
    current_piece = board[row][col]

    if selected_piece:
        # Move selected piece to new location
        if (row, col) != selected_pos:
            board[row][col] = selected_piece
            prev_row, prev_col = selected_pos
            board[prev_row][prev_col] = ""
        selected_piece = None
        selected_pos = None
        draw_board()
    elif current_piece:
        # Select a piece
        selected_piece = current_piece
        selected_pos = (row, col)

# Initial draw
draw_board()
screen.onclick(on_click)

screen.mainloop()
