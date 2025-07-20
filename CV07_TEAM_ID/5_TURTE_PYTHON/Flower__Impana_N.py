import turtle as t

t.speed(0)
t.color("red", "yellow")
t.begin_fill()

for _ in range(36):
    t.circle(100, 60)
    t.left(120)
    t.circle(100, 60)
    t.left(170)

t.end_fill()
t.hideturtle()
t.done()
