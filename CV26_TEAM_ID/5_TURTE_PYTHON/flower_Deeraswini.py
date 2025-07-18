import turtle
import colorsys
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Beautiful Flower - Turtle Python")
flower = turtle.Turtle()
flower.speed(0)
flower.width(2)
def get_color(i, n):
    return colorsys.hsv_to_rgb(i/n, 1, 1)
def draw_petal(radius, angle):
    for _ in range(2):
        flower.circle(radius, angle)
        flower.left(180 - angle)
petals = 36
for i in range(petals):
    flower.color(get_color(i, petals))
    draw_petal(100, 60)
    flower.left(360 / petals)
flower.penup()
flower.goto(0, -20)
flower.pendown()
flower.color("yellow")
flower.begin_fill()
flower.circle(20)
flower.end_fill()
flower.hideturtle()
screen.mainloop()
