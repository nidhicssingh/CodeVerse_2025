import turtle 
  
# create screen object and turtle object
screen = turtle.Screen()
pen = turtle.Turtle()
  
# method to draw square
def draw():
  for i in range(4):
    pen.forward(30)
    pen.left(90)
  pen.forward(30)

# Main Code to draw the chess board using turtle
if __name__ == "__main__" :
      
    # set screen
    screen.setup(600, 600)
      
    # set turtle object speed
    pen.speed(1000)
      
    # loops for board
    for i in range(8):
      
      # not ready to draw
      pen.up()
      
      # set position for every row
      pen.setpos(0, 30 * i)
      
      # ready to draw
      pen.down()

      for j in range(8):
        # conditions for alternative color
        if (i + j)% 2 == 0:
          color ='black'
        else:
          color ='white'
        # fill with given color
        pen.fillcolor(color)
        # start filling with color
        pen.begin_fill()
        draw()
        pen.end_fill()
    # hide the turtle
    pen.hideturtle()
