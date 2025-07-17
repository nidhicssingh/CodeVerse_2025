import turtle
screen = turtle.Screen()
screen.title("Harishitha's Tic Tac Toe")
screen.setup(width=1000, height=1000)
screen.bgcolor("LavenderBlush")  
screen.tracer(0)

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

def draw_grid():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.pensize(4)
    drawer.color("black")

    for i in [-100, 100]:
        drawer.penup()
        drawer.goto(i, 300)
        drawer.pendown()
        drawer.goto(i, -300)
    for i in [-100, 100]:
        drawer.penup()
        drawer.goto(-300, i)
        drawer.pendown()
        drawer.goto(300, i)
    for i in [-100, 100]:
        drawer.penup()
        drawer.goto(-300, i)
        drawer.pendown()
        drawer.goto(300, i)

def draw_symbol(x, y, symbol):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(x, y)
    writer.color("Black" if symbol == "X" else "red")
    writer.write(symbol, align="center", font=("Arial", 48, "bold"))

def get_cell_index(x, y):
    col = (x + 300) // 200
    row = (300 - y) // 200
    return int(row), int(col)

def check_winner(player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)): return True
        if all(board[j][i] == player for j in range(3)): return True
    if all(board[i][i] == player for i in range(3)): return True
    if all(board[i][2 - i] == player for i in range(3)): return True
    return False
def sprinkle_blast():
    import random
    import turtle

    colors = ["hotpink", "skyblue", "gold", "violet", "lightgreen", "orange", "turquoise"]
    sprinkles = []

    def create_sprinkle():
        sparkle = turtle.Turtle()
        sparkle.shape("circle")
        sparkle.color(random.choice(colors))
        sparkle.penup()
        sparkle.speed("fastest")

        
        corner = random.choice(["left", "right"])
        x = -480 if corner == "left" else 480
        y = -480
        sparkle.goto(x, y)

        dx = random.randint(2, 5) * (-1 if corner == "right" else 1)  
        dy = random.randint(3, 6)  
        return (sparkle, dx, dy)

    
    for _ in range(60):
        sprinkles.append(create_sprinkle())

    
    while True:
        for i in range(len(sprinkles)):
            sparkle, dx, dy = sprinkles[i]
            sparkle.setx(sparkle.xcor() + dx)
            sparkle.sety(sparkle.ycor() + dy)
            if sparkle.ycor() > 500 or abs(sparkle.xcor()) > 500:
                sparkle.clear()
                sprinkles[i] = create_sprinkle()
        screen.update()


def display_winner(player):
    winner = turtle.Turtle()
    winner.hideturtle()
    winner.penup()
    winner.goto(0, -260)
    winner.color("green")
    winner.write(f"congragulations 🎉!! Player {player} wins!", align="center", font=("Stencil", 32, "bold"))

    sprinkle_blast()  

def click_handler(x, y):
    global current_player, game_over
    if game_over:
        return

    row, col = get_cell_index(x, y)
    if row not in range(3) or col not in range(3):
        return
    if board[row][col] == "":
        board[row][col] = current_player
        draw_symbol((col * 200 - 200), (100 - row * 200), current_player)
        if check_winner(current_player):
            game_over = True
            display_winner(current_player)
        else:
            current_player = "❤" if current_player == "X" else "X"


draw_grid()
screen.onclick(click_handler)
screen.mainloop()