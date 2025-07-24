import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Don't Catch the Block!")
screen.bgcolor("lightgray")
screen.tracer(0)
screen.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.color("black")
paddle.penup()
paddle.goto(0, -250)

# Block
block = turtle.Turtle()
block.shape("square")
block.color("red")
block.penup()
block.goto(random.randint(-250, 250), 250)

# Score
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))

# Paddle movement
def move_left():
    x = paddle.xcor()
    x -= 30
    if x > -250:
        paddle.setx(x)

def move_right():
    x = paddle.xcor()
    x += 30
    if x < 250:
        paddle.setx(x)

# Reset block
def reset_block():
    block.goto(random.randint(-250, 250), 250)

# Game loop
def update():
    global score
    y = block.ycor()
    y -= 10
    block.sety(y)

    # Collision check
    if block.ycor() < -240 and abs(block.xcor() - paddle.xcor()) < 50:
        screen.clear()
        game_over = turtle.Turtle()
        game_over.hideturtle()
        game_over.write("💥 Game Over!", align="center", font=("Arial", 28, "bold"))
        return

    elif block.ycor() < -300:
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 16, "bold"))
        reset_block()

    screen.update()
    screen.ontimer(update, 100)

# Controls
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Start game
update()
screen.mainloop()