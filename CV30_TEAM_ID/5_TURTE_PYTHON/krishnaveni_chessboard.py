import turtle

def draw_square(t, size, color):
    """Draws a square of a given size and color."""
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    t.end_fill()

def draw_chessboard(pen, square_size=40, num_squares=8):
    """Draws an 8x8 chessboard."""
    start_x = - (num_squares * square_size) / 2
    start_y = (num_squares * square_size) / 2

    pen.penup()
    pen.goto(start_x, start_y)
    pen.pendown()

    for row in range(num_squares):
        for col in range(num_squares):
            # Determine the color of the square
            if (row + col) % 2 == 0:
                color = "white"
            else:
                color = "black"

            draw_square(pen, square_size, color)

            # Move to the next position for the next square
            pen.penup()
            pen.forward(square_size)
            pen.pendown()

        # Move to the beginning of the next row
        pen.penup()
        pen.goto(start_x, start_y - (row + 1) * square_size)
        pen.pendown()

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Turtle Chessboard")
    screen.tracer(0)  # Turn off screen updates for faster drawing

    pen = turtle.Turtle()
    pen.speed(0)  # Fastest speed
    pen.hideturtle()

    draw_chessboard(pen)

    screen.update()  # Update the screen once drawing is complete
    screen.exitonclick()

if __name__ == "__main__":
    main()