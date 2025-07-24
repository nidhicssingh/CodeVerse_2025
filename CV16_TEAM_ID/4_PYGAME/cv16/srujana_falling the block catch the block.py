import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Falling Block")
screen.tracer(0)

# Create the paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("black")
paddle.penup()
paddle.goto(0, -250)

# Create the falling block
block = turtle.Turtle()
block.shape("square")
block.color("red")
block.penup()
block.goto(random.randint(-200, 200), 250)

# Move paddle left
def move_left():
    x = paddle.xcor()
    x -= 30
    if x > -250:
        paddle.setx(x)

# Move paddle right
def move_right():
    x = paddle.xcor()
    x += 30
    if x < 250:
        paddle.setx(x)

# Reset block position
def reset_block():
    block.goto(random.randint(-200, 200), 250)

# Game loop
def update():
    y = block.ycor()
    y -= 10
    block.sety(y)

    # Collision check
    if block.ycor() < -240 and abs(block.xcor() - paddle.xcor()) < 50:
        print("Caught!")
        reset_block()

    elif block.ycor() < -300:
        print("Missed!")
        reset_block()

    screen.update()
    screen.ontimer(update, 100)

# Key bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Start the game
update()
screen.mainloop()