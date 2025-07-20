import turtle
import math

# Screen setup
screen = turtle.Screen()
screen.title("Indian Flag - Wavy Display")
screen.bgcolor("skyblue")

pen = turtle.Turtle()
pen.speed(5)  # Medium speed
pen.pensize(2)
pen.penup()

# Function to draw a wavy stripe
def draw_wavy_stripe(color, start_y, height):
    pen.color(color)
    pen.penup()
    pen.goto(-150, start_y)
    pen.pendown()
    pen.begin_fill()
    for x in range(-150, 201):
        y = start_y + 10 * math.sin((x + 150) / 25)
        pen.goto(x, y)
    for x in range(200, -151, -1):
        y = start_y - height + 10 * math.sin((x + 150) / 25)
        pen.goto(x, y)
    pen.goto(-150, start_y)
    pen.end_fill()
    pen.penup()

# Draw resized wavy stripes
stripe_height = 40
saffron_y = 120
white_y = saffron_y - stripe_height
green_y = white_y - stripe_height

draw_wavy_stripe("#FF9933", saffron_y, stripe_height)
draw_wavy_stripe("white", white_y, stripe_height)
draw_wavy_stripe("#138808", green_y, stripe_height)

# Draw Ashoka Chakra slightly right and a little bit higher in white stripe
chakra_y = white_y - stripe_height + 15
pen.goto(30, chakra_y)
pen.setheading(0)
pen.pendown()
pen.color("navy")
pen.pensize(1.5)
pen.circle(15)
pen.penup()

pen.goto(30, chakra_y + 15)
pen.setheading(0)
for _ in range(24):
    pen.pendown()
    pen.forward(15)
    pen.backward(15)
    pen.left(15)
    pen.penup()

# Draw longer flag pole
pen.color("black")
pen.pensize(10)
pen.goto(-150, saffron_y)
pen.setheading(270)
pen.pendown()
pen.forward(350)
pen.penup()

# Write Name and Team
pen.goto(-160, -250)
pen.color("black")
pen.write("Created by: Abhijith Skanda HN", font=("Arial", 12, "bold"))
pen.goto(-160, -270)
pen.write("Team: Codeverse_CV22", font=("Arial", 12, "bold"))

pen.hideturtle()
turtle.done()
