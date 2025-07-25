import turtle
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create turtle
pen = turtle.Turtle()
pen.speed(0)        # Fastest
pen.width(2)
pen.hideturtle()

# Color settings
hue = 0
num_colors = 36     # Color variety
n = 36              # Number of patterns

# Draw complex pattern
for i in range(360):
    color = colorsys.hsv_to_rgb(hue, 1, 1)
    pen.color(color)
    pen.forward(i * 3 / n + i)
    pen.left(59)
    pen.forward(i * 3 / n + i)
    pen.left(59)
    pen.forward(i * 3 / n + i)
    pen.left(59)
    pen.left(1)

    hue += 1 / 360

# Keep the window open
turtle.done()