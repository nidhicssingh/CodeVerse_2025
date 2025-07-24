import turtle

# Setup screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Main turtle for flower
flower = turtle.Turtle()
flower.speed(0)
flower.hideturtle()

# ----- 1. Draw Sepals (BEHIND the petals) -----
def draw_sepal():
    flower.color("darkgreen", "forestgreen")
    flower.begin_fill()
    flower.circle(70, 60)
    flower.left(120)
    flower.circle(70, 60)
    flower.left(120)
    flower.end_fill()

flower.penup()
flower.goto(0, 0)
flower.setheading(0)
flower.pendown()

for _ in range(6):  # Fewer sepals, spaced out
    draw_sepal()
    flower.left(60)

# ----- 2. Draw Petals (on top of sepals) -----
def draw_petal():
    flower.color("gold", "yellow")
    flower.begin_fill()
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)
    flower.end_fill()

flower.penup()
flower.goto(0, 0)
flower.setheading(0)
flower.pendown()

for _ in range(18):  # 18 overlapping petals
    draw_petal()
    flower.left(20)

# ----- 3. Draw Center (on top of petals) -----
flower.penup()
flower.goto(0, -35)
flower.setheading(0)
flower.pendown()
flower.color("saddlebrown", "chocolate")
flower.begin_fill()
flower.circle(35)
flower.end_fill()

# ----- 4. Draw Stem -----
stem = turtle.Turtle()
stem.hideturtle()
stem.color("green")
stem.pensize(12)
stem.penup()
stem.goto(0, -35)
stem.setheading(-90)
stem.pendown()
stem.forward(150)

# ----- 5. Draw Leaves -----
def draw_leaf(x, y, angle):
    stem.penup()
    stem.goto(x, y)
    stem.setheading(angle)
    stem.pendown()
    stem.begin_fill()
    stem.circle(30, 60)
    stem.left(120)
    stem.circle(30, 60)
    stem.end_fill()

stem.fillcolor("green")
draw_leaf(-25, -110, -160)
draw_leaf(25, -130, -20)

# Show window
screen.mainloop()
