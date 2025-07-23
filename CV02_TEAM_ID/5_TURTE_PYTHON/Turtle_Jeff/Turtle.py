import turtle

screen = turtle.Screen()
screen.bgcolor("white")

cross = turtle.Turtle()
cross.speed(3)
cross.pensize(3)

def draw_rectangle(x, y, width, height, color):
    cross.penup()
    cross.goto(x, y)
    cross.pendown()
    cross.color(color)
    cross.begin_fill()
    for _ in range(2):
        cross.forward(width)
        cross.right(90)
        cross.forward(height)
        cross.right(90)
    cross.end_fill()

draw_rectangle(-15, 100, 30, 200, "#8B0000")  

draw_rectangle(-75, 30, 150, 30, "#8B0000")

draw_rectangle(-15, 100, 5, 200, "#A52A2A")  
draw_rectangle(10, 100, 5, 200, "#5C0000")   

draw_rectangle(-75, 30, 5, 30, "#A52A2A")   
draw_rectangle(70, 30, 5, 30, "#5C0000")    

cross.hideturtle()
turtle.done()
