import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(10)

# Draw a petal
def draw_petal():
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Draw flower with multiple petals
for _ in range(6):  # 6 petals
    draw_petal()
    flower.right(60)

# Draw center
flower.color("yellow")
flower.penup()
flower.goto(0, 0)
flower.pendown()
flower.begin_fill()
flower.circle(30)
flower.end_fill()

# Hide turtle and finish
flower.hideturtle()
screen.mainloop()
