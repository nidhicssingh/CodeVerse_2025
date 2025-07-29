import turtle
import colorsys

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
flower = turtle.Turtle()
flower.speed(0)
flower.width(2)

# --- Draw Colorful Petals ---
def draw_flower():
    flower.penup()
    flower.goto(0, 0)
    flower.pendown()
    
    n_petals = 36
    hue = 0
    for _ in range(n_petals):
        color = colorsys.hsv_to_rgb(hue, 1, 1)
        flower.color(color)
        flower.begin_fill()
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)
        flower.end_fill()
        flower.left(360 / n_petals)
        hue += 1 / n_petals

# --- Draw Flower Center ---
def draw_center():
    flower.penup()
    flower.goto(0, -20)
    flower.color("yellow")
    flower.pendown()
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

# --- Draw Stem ---
def draw_stem():
    flower.penup()
    flower.goto(0, -100)
    flower.setheading(-90)
    flower.color("green")
    flower.width(10)
    flower.pendown()
    flower.forward(150)

# --- Draw Leaves ---
def draw_leaf(x, y, angle):
    flower.penup()
    flower.goto(x, y)
    flower.setheading(angle)
    flower.color("darkgreen")
    flower.width(2)
    flower.begin_fill()
    flower.pendown()
    flower.circle(40, 90)
    flower.left(90)
    flower.circle(40, 90)
    flower.end_fill()

# --- Build Full Flower ---
draw_flower()
draw_center()
draw_stem()
draw_leaf(-30, -150, -160)  # Left leaf
draw_leaf(30, -150, -20)    # Right leaf

flower.hideturtle()
screen.mainloop()
