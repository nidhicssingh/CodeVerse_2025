from turtle import *

speed(0)
setup(800, 500)

penup()
goto(-400, 250)
pendown()

# Orange Rectangle
color("orange")
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

left(90)
forward(167)

# Green Rectangle
color("green")
begin_fill()
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

# Big Blue Circle
penup()
goto(70, 0)
pendown()
color("navy")
begin_fill()
circle(70)
end_fill()

# Big White Circle
penup()
goto(60, 0)
pendown()
color("white")
begin_fill()
circle(60)
end_fill()

# Mini Blue Circles
penup()
goto(-57, -8)
pendown()
color("navy")
for i in range(24):
    begin_fill()
    circle(3)
    end_fill()
    penup()
    forward(15)
    right(15)
    pendown()

# Small Blue Circle
penup()
goto(20, 0)
pendown()
begin_fill()
circle(20)
end_fill()

# Spokes
penup()
goto(0, 0)
pendown()
pensize(2)
for i in range(24):
    forward(60)
    backward(60)
    left(15)
hideturtle()
done()