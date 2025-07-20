import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Indian Flag")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)

# Constants
flag_height = 300
flag_width = 450
stripe_height = flag_height / 3
chakra_radius = 30

# Function to draw a filled rectangle
def draw_rectangle(color, x, y, width, height):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(0)
    pen.pendown()
    pen.color("black", color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Draw saffron stripe (top)
draw_rectangle("#FF9933", -flag_width/2, flag_height/2, flag_width, stripe_height)

# Draw white stripe (middle)
draw_rectangle("white", -flag_width/2, flag_height/6, flag_width, stripe_height)

# Draw green stripe (bottom)
draw_rectangle("#138808", -flag_width/2, -flag_height/6, flag_width, stripe_height)

# Draw Ashoka Chakra in center of white stripe
chakra_center_y = flag_height/6 - stripe_height/2
pen.penup()
pen.goto(0, chakra_center_y - chakra_radius)
pen.setheading(0)
pen.pendown()
pen.color("navyblue")
pen.pensize(2)
pen.circle(chakra_radius)

# Draw 24 spokes
pen.pensize(1)
for i in range(24):
    pen.penup()
    pen.goto(0, chakra_center_y)
    pen.setheading(i * 15)
    pen.pendown()
    pen.forward(chakra_radius)

# Draw the flag pole
pen.penup()
pen.goto(-flag_width/2, flag_height/2)
pen.setheading(-90)
pen.color("black")
pen.pensize(5)
pen.pendown()
pen.forward(400)

pen.hideturtle()
screen.mainloop()
