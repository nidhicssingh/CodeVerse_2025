# importing the library
from turtle import *


# Function for position
def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


# to draw the left eye
def leftEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x + 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()


# To draw the right eye
def rightEye(x, y):
    my_goto(x, y)
    seth(0)
    fillcolor('#333333')
    begin_fill()
    circle(22)
    end_fill()

    my_goto(x, y + 10)
    fillcolor('#000000')
    begin_fill()
    circle(10)
    end_fill()

    my_goto(x - 6, y + 22)
    fillcolor('#ffffff')
    begin_fill()
    circle(10)
    end_fill()


# To draw the mouth
def mouth(x, y):
    my_goto(x, y)
    fillcolor('#88141D')
    begin_fill()

    # Lower Lip
    l1 = []
    l2 = []
    seth(190)
    a = 0.7
    for i in range(28):
        a += 0.1
        right(3)
        fd(a)
        l1.append(position())

    my_goto(x, y)

    seth(10)
    a = 0.7
    for i in range(28):
        a += 0.1
        left(3)
        fd(a)
        l2.append(position())

    # Upper Lip
    seth(10)
    circle(50, 15)
    left(180)
    circle(-50, 15)

    circle(-50, 40)
    seth(233)
    circle(-50, 55)
    left(180)
    circle(50, 12.1)
    end_fill()

    # Tongue
    my_goto(17, 54)
    fillcolor('#DD716F')
    begin_fill()
    seth(145)
    circle(40, 86)
    penup()
    for pos in reversed(l1[:20]):
        goto(pos[0], pos[1] + 1.5)
    for pos in l2[:20]:
        goto(pos[0], pos[1] + 1.5)
    pendown()
    end_fill()

    # Nose
    my_goto(-17, 94)
    seth(8)
    fd(4)
    back(8)


# to draw the left red cheek
def leftCheek(x, y):
    tracer(False)
    my_goto(x, y)
    seth(300)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 & 30 or 60 & 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()
    tracer(True)

 
# To draw the right red cheek
def rightCheek(x, y):
    tracer(False)
    my_goto(x, y)
    seth(60)
    fillcolor('#DD4D28')
    begin_fill()
    a = 2.3
    for i in range(120):
        if 0 & 30 or 60 & 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    end_fill()
    tracer(True)


# Tp draw the left ear
def LeftEar(x, y):
    my_goto(x, y)
    fillcolor('#000000')
    begin_fill()
    seth(330)
    circle(100, 35)
    seth(219)
    circle(-300, 19)
    seth(110)
    circle(-30, 50)
    circle(-300, 10)
    end_fill()


# To draw the right ear
def RightEar(x, y):
    my_goto(x, y)
    fillcolor('#000000')
    begin_fill()
    seth(300)
    circle(-100, 30)
    seth(35)
    circle(300, 15)
    circle(30, 50)
    seth(190)
    circle(300, 17)
    end_fill()


# To draw the body outline
def body():
    fillcolor('#F6D02F')
    begin_fill()
    # Right face contour
    penup()
    circle(130, 40)
    pendown()
    circle(100, 105)
    left(180)
    circle(-100, 5)

    # Right ear
    seth(20)
    circle(300, 30)
    circle(30, 50)
    seth(190)
    circle(300, 36)

    # Upper profile
    seth(150)
    circle(150, 70)

    # Left ear
    seth(200)
    circle(300, 40)
    circle(30, 50)
    seth(20)
    circle(300, 35)

    # Left face contour
    seth(240)
    circle(105, 95)
    left(180)
    circle(-105, 5)

    # Left hand
    seth(210)
    circle(500, 18)
    seth(200)
    fd(10)
    seth(280)
    fd(7)
    seth(210)
    fd(10)
    seth(300)
    circle(10, 80)
    seth(220)
    fd(10)
    seth(300)
    circle(10, 80)
    seth(240)
    fd(12)
    seth(0)
    fd(13)
    seth(240)
    circle(10, 70)
    seth(10)
    circle(10, 70)
    seth(10)
    circle(300, 18)

    seth(75)
    circle(500, 8)
    left(180)
    circle(-500, 15)
    seth(250)
    circle(100, 65)

    # Left foot
    seth(320)
    circle(100, 5)
    left(180)
    circle(-100, 5)
    seth(220)
    circle(200, 20)
    circle(20, 70)

    seth(60)
    circle(-100, 20)
    left(180)
    circle(100, 20)
    seth(300)
    circle(10, 70)

    seth(60)
    circle(-100, 20)
    left(180)
    circle(100, 20)
    seth(10)
    circle(100, 60)

    # Horizontal
    seth(180)
    circle(-100, 10)
    left(180)
    circle(100, 10)
    seth(5)
    circle(100, 10)
    circle(-100, 40)
    circle(100, 35)
    left(180)
    circle(-100, 10)

    # Right foot
    seth(290)
    circle(100, 55)
    circle(10, 50)
    seth(120)
    circle(100, 20)
    left(180)
    circle(-100, 20)
    seth(0)
    circle(10, 50)
    seth(110)
    circle(100, 20)
    left(180)
    circle(-100, 20)
    seth(30)
    circle(20, 50)
    seth(100)
    circle(100, 40)

    # Right body contour
    seth(200)
    circle(-100, 5)
    left(180)
    circle(100, 5)
    left(30)
    circle(100, 75)
    right(15)
    circle(-300, 21)
    left(180)
    circle(300, 3)

    # Right hand
    seth(43)
    circle(200, 60)
    right(10)
    fd(10)
    circle(5, 160)
    seth(90)
    circle(5, 160)
    seth(90)
    fd(10)
    seth(90)
    circle(5, 180)
    fd(10)
    left(180)
    left(20)
    fd(10)
    circle(5, 170)
    fd(10)
    seth(240)
    circle(50, 30)
    end_fill()
    my_goto(130, 125)
    seth(-20)
    fd(5)
    circle(-5, 160)
    fd(5)

    # Fingers
    my_goto(166, 130)
    seth(-90)
    fd(3)
    circle(-4, 180)
    fd(3)
    seth(-90)
    fd(3)
    circle(-4, 180)
    fd(3)

    # Tail
    my_goto(168, 134)
    fillcolor('#F6D02F')
    begin_fill()
    seth(40)
    fd(200)
    seth(-80)
    fd(150)
    seth(210)
    fd(150)
    left(90)
    fd(100)
    right(95)
    fd(100)
    left(110)
    fd(70)
    right(110)
    fd(80)
    left(110)
    fd(30)
    right(110)
    fd(32)
    right(106)
    circle(100, 25)
    right(15)
    circle(-300, 2)
    seth(30)
    fd(40)
    left(100)
    fd(70)
    right(100)
    fd(80)
    left(100)
    fd(46)
    seth(66)
    circle(200, 38)
    right(10)
    fd(10)
    end_fill()

    # Tail Pattern
    fillcolor('#923E24')
    my_goto(126.82, -156.84)
    begin_fill()
    seth(30)
    fd(40)
    left(100)
    fd(40)
    pencolor('#923e24')
    seth(-30)
    fd(30)
    left(140)
    fd(20)
    right(150)
    fd(20)
    left(150)
    fd(20)
    right(150)
    fd(20)
    left(130)
    fd(18)
    pencolor('#000000')
    seth(-45)
    fd(67)
    right(110)
    fd(80)
    left(110)
    fd(30)
    right(110)
    fd(32)
    right(106)
    circle(100, 25)
    right(15)
    circle(-300, 2)
    end_fill()

    # Calling other functions
    cap(-134.07, 147.81)
    mouth(-5, 25)
    leftCheek(-126, 32)
    rightCheek(107, 63)
    LeftEar(-250, 100)
    RightEar(140, 270)
    leftEye(-85, 90)
    rightEye(50, 110)


# To draw the cap
def cap(x, y):
    my_goto(x, y)
    fillcolor('#CD0000')
    begin_fill()
    seth(200)
    circle(400, 7)
    left(180)
    circle(-400, 30)
    circle(30, 60)
    fd(50)
    circle(30, 45)
    fd(60)
    left(5)
    circle(30, 70)
    right(20)
    circle(200, 70)
    circle(30, 60)
    fd(70)
    right(35)
    fd(50)
    circle(8, 100)
    end_fill()
    my_goto(-168.47, 185.52)
    seth(36)
    circle(-270, 54)
    left(180)
    circle(270, 27)
    circle(-80, 98)
    fillcolor('#444444')
    begin_fill()
    left(180)
    circle(80, 197)
    left(58)
    circle(200, 45)
    end_fill()
    my_goto(-58, 270)
    pencolor('#228B22')
    dot(35)
    my_goto(-30, 280)
    fillcolor('#228B22')
    begin_fill()
    seth(100)
    circle(30, 180)
    seth(190)
    fd(15)
    seth(100)
    circle(-45, 180)
    right(90)
    fd(15)
    end_fill()
    pencolor('#000000')


if _name_ == _name_:
    # Window control
    screensize(800, 700, '#f0f0f0')
    screen = Screen()
    screen.setup(width=1.0, height=1.0)

    # Setting the pen size
    pensize(3)

    # Setting the speed
    speed(10)
    body()
    my_goto(250, -230)
    write('by Trisha', font=("Arial", 15))

    mainloop()
