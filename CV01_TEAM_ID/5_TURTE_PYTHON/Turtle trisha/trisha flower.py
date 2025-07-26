import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("hotpink")
flower.speed(10)

# Draw flower
for i in range(36):
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.right(90)
    flower.forward(100)
    flower.left(45)
    flower.forward(100)
    flower.right(100)  # creates curve and rotation

# Hide turtle and finish
flower.hideturtle()
turtle.done()
