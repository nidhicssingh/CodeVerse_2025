import turtle

# Setup
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)

# Helper function to draw a filled circle
def draw_circle(color, radius, x, y):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Draw face
draw_circle("skyblue", 100, 0, 0)

# Draw eyes
draw_circle("white", 20, -30, 40)
draw_circle("white", 20, 30, 40)
draw_circle("black", 8, -30, 50)
draw_circle("black", 8, 30, 50)

# Draw nose
draw_circle("red", 10, 0, 20)

# Draw smile
t.penup()
t.goto(-40, -20)
t.setheading(-60)
t.pendown()
t.circle(50, 120)

# Hide turtle
t.hideturtle()
screen.mainloop()
