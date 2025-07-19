import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw the face
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw the eyes
t.penup()
t.goto(-40, 120)
t.pendown()
t.dot(20, 'black')  # First eye

t.penup()
t.goto(40, 120)
t.pendown()
t.dot(20, 'black')  # Second eye

# Draw the smile
t.penup()
t.goto(-40, 60)
t.pendown()
t.right(90)  # Rotate the turtle to draw the arc correctly
t.circle(40, 180) # Draw an arc for the smile

# Keep the window open
turtle.done()