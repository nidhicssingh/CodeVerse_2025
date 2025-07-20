from turtle import *

speed(0)
pensize(3)
color("black")

# Move without drawing
def jump(x, y):
    penup()
    goto(x, y)
    pendown()

# Approximate circle using small lines
def curve(radius, extent, angle_step=1):
    for _ in range(int(extent / angle_step)):
        forward(2 * 3.14 * radius * angle_step / 360)
        left(angle_step)

# -------------------------
# Face outline (circle-like)
# -------------------------
def draw_face():
    jump(0, -100)
    setheading(0)
    color("orange")
    begin_fill()
    for _ in range(360):
        forward(1.75)
        left(1)
    end_fill()
    color("black")

# -------------------------
# Eyes
# -------------------------
def draw_eyes():
    # Left eye
    jump(-40, 60)
    setheading(0)
    color("black")
    begin_fill()
    for _ in range(36):
        forward(1)
        left(10)
    end_fill()
    
    # Right eye
    jump(40, 60)
    begin_fill()
    for _ in range(36):
        forward(1)
        left(10)
    end_fill()

# -------------------------
# Smile
# -------------------------
def draw_smile():
    jump(-40, -10)
    setheading(-60)
    pensize(5)
    for _ in range(60):
        forward(2)
        left(2)

# -------------------------
# Main drawing
# -------------------------
bgcolor("white")
draw_face()
draw_eyes()
draw_smile()

hideturtle()
done()
