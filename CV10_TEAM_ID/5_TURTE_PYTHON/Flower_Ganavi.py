import turtle

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("lightyellow")
sun = turtle.Turtle()
sun.speed(0)
sun.width(2)

# Sunflower petals in orange
sun.color("darkorange", "orange")

def draw_petal():
    sun.begin_fill()
    sun.circle(100, 60)     
    sun.left(120)
    sun.circle(100, 60)     
    sun.left(120)
    sun.end_fill()

for _ in range(20):         # 20 petals
    draw_petal()
    sun.left(18)

# Center of the sunflower
sun.penup()
sun.goto(0, -50)
sun.pendown()
sun.color("saddlebrown")
sun.begin_fill()
sun.circle(50)
sun.end_fill()

# Stem
sun.penup()
sun.goto(0, -100)
sun.setheading(-90)
sun.pendown()
sun.color("green")
sun.width(10)
sun.forward(200)

# Leaves
def draw_leaf():
    sun.color("forestgreen")
    sun.begin_fill()
    sun.circle(40, 60)
    sun.left(120)
    sun.circle(40, 60)
    sun.left(120)
    sun.end_fill()

sun.width(2)

# Left leaf
sun.penup()
sun.goto(0, -180)
sun.setheading(210)
sun.pendown()
draw_leaf()

# Right leaf
sun.penup()
sun.goto(0, -180)
sun.setheading(-30)
sun.pendown()
draw_leaf()

sun.hideturtle()
screen.mainloop()