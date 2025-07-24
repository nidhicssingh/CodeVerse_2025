import turtle
import colorsys


screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Yellow Flower by Zaina")


flower = turtle.Turtle()
flower.speed(0)
flower.width(2)
flower.color("gold")


def draw_flower():
    for i in range(36):
        flower.circle(100, 60)
        flower.left(120)
        flower.circle(100, 60)
        flower.left(120)
        flower.left(10)

def draw_center():
    flower.penup()
    flower.goto(0, -20)
    flower.pendown()
    flower.color("orange")
    flower.begin_fill()
    flower.circle(20)
    flower.end_fill()

draw_flower()
draw_center()

flower.hideturtle()
turtle.done()
