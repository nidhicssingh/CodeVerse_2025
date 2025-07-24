import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
sunflower = turtle.Turtle()
sunflower.speed(0)

# Function to draw a petal
def draw_petal():
    sunflower.color("yellow", "yellow")
    sunflower.begin_fill()
    sunflower.circle(100, 60)
    sunflower.left(120)
    sunflower.circle(100, 60)
    sunflower.left(120)
    sunflower.end_fill()

# Draw petals
sunflower.penup()
sunflower.goto(0, 0)
sunflower.setheading(0)
sunflower.pendown()
for _ in range(18):
    draw_petal()
    sunflower.left(20)

# Draw flower center
sunflower.penup()
sunflower.goto(0, -40)
sunflower.setheading(0)
sunflower.color("brown", "brown")
sunflower.pendown()
sunflower.begin_fill()
sunflower.circle(40)
sunflower.end_fill()

# Draw stem
sunflower.penup()
sunflower.goto(0, -80)
sunflower.setheading(-90)
sunflower.pensize(10)
sunflower.color("green")
sunflower.pendown()
sunflower.forward(200)

# Reset pen size for leaves
sunflower.pensize(1)
sunflower.color("green", "lightgreen")

# Draw left leaf (upright and outward)
sunflower.penup()
sunflower.goto(0, -160)
sunflower.setheading(180)  # direct left
sunflower.pendown()
sunflower.begin_fill()
sunflower.circle(40, 60)
sunflower.left(120)
sunflower.circle(40, 60)
sunflower.end_fill()

# Draw right leaf (upright and outward)
sunflower.penup()
sunflower.goto(0, -160)
sunflower.setheading(0)  # direct right
sunflower.pendown()
sunflower.begin_fill()
sunflower.circle(-40, 60)  # mirror curve with negative radius
sunflower.right(120)
sunflower.circle(-40, 60)
sunflower.end_fill()

# Hide turtle
sunflower.hideturtle()
screen.mainloop()