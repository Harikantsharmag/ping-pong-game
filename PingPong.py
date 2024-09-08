# Importing turtle for graphics and functools for higher-order functions like 'partial'
import turtle
from functools import partial

# Setting up the game screen
screen = turtle.Screen()  # Create a screen object to display the game
screen.title("Ping Pong")  # Set the window title
screen.bgcolor("black")  # Set the background color to black
screen.bgpic("bg.png")  # Set a background image for the game (bg.png should exist in your directory)
screen.setup(width=800, height=600)  # Set the window size to 800x600 pixels
screen.tracer(0)  # Turn off automatic screen updates to manually control the refresh rate

# Initializing the paddles (players) and the ball
player1 = turtle.Turtle()  # Player 1 paddle
player2 = turtle.Turtle()  # Player 2 paddle
ball = turtle.Turtle()  # Ball object

# Configuring the ball's shape and appearance
ball.shape("circle")  # Ball is circular
ball.color("white")  # Ball color is white
ball.penup()  # Disable drawing lines while moving the ball
ball.dx = 0.1  # Ball's speed on the x-axis
ball.dy = -0.1  # Ball's speed on the y-axis

# Paddle size setup (global variables)
barWidth = 5  # Paddle width
barLen = 1  # Paddle length

# Initialize scores for both players
score1 = 0  # Score for Player 1
score2 = 0  # Score for Player 2

# Turtle object to display the score on the screen
showScore = turtle.Turtle()
showScore.color("white")  # Score color
showScore.hideturtle()  # Hide the turtle pointer
showScore.penup()  # Disable drawing when moving
showScore.goto(0, 240)  # Place the score at the top of the screen
showScore.write("Player 1: 0        Player 2: 0", align="center", font=("Trebuchet MS", 30))  # Initial score display

# Function to create the paddles (bars) for each player
def createBars(player, pos):
    global barWidth, barLen
    player.shape("square")  # Paddle shape
    player.color("white")  # Paddle color
    player.shapesize(stretch_wid=barWidth, stretch_len=barLen)  # Set paddle size
    player.penup()  # Disable drawing
    player.goto(pos, 0)  # Set paddle position (left for Player 1, right for Player 2)

# Creating paddles for both players with initial positions
createBars(player1, -350)  # Player 1 (left side)
createBars(player2, 350)  # Player 2 (right side)

# Function to move paddles based on player input
def moveBar(bar, barDir):
    global barWidth
    # Define movement boundaries
    barHaftWidthUP = (300 - (barWidth * 21) / 2)  # Upper boundary
    barHaftWidthDown = (-300 + (barWidth * 21) / 2)  # Lower boundary
    y = bar.ycor()  # Get current y-coordinate of the paddle
    x = bar.xcor()  # Get current x-coordinate of the paddle
    
    # Move paddle vertically or horizontally depending on user input
    if barDir == "UP":  # Move paddle up
        y = y + 10
        bar.sety(y)
        if y > barHaftWidthUP:  # Prevent the paddle from moving beyond the screen
            bar.sety(barHaftWidthUP)
    elif barDir == "Down":  # Move paddle down
        y = y - 10
        bar.sety(y)
        if y < barHaftWidthDown:  # Prevent paddle from going off-screen
            bar.sety(barHaftWidthDown)
    elif barDir == "Right":  # Move paddle right (horizontal)
        if x == 350:
            bar.setx(350)  # Prevent paddle from going past the right boundary
        elif x <= 350 and x >= 10:
            x = x + 10  # Move paddle to the right
            bar.setx(x)
        elif x >= -350 and x < -10:
            x = x + 10
            bar.setx(x)
    elif barDir == "Left":  # Move paddle left (horizontal)
        if x == -350:
            bar.setx(-350)  # Prevent paddle from going past the left boundary
        elif x >= -350 and x <= -10:
            x = x - 10  # Move paddle to the left
            bar.setx(x)
        elif x > 10 and x <= 350:
            x = x - 10
            bar.setx(x)

# Function to move the ball and detect screen boundaries
def moveBall():
    ball.setx(ball.xcor() + ball.dx)  # Move ball along x-axis
    ball.sety(ball.ycor() + ball.dy)  # Move ball along y-axis
    
    # Ball bounces off the right wall
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1  # Reverse direction along x-axis
    
    # Ball bounces off the left wall
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1  # Reverse direction along x-axis

    # Ball bounces off the bottom wall
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # Reverse direction along y-axis
    
    # Ball bounces off the top wall
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # Reverse direction along y-axis

# Function to detect collision between ball and paddles
def colDec(player):
    if (player.xcor() + 20 >= ball.xcor() >= player.xcor() - 20 and 
        player.ycor() + 60 >= ball.ycor() >= player.ycor() - 60):
        ball.dx *= -1  # Reverse ball's x-axis direction on collision
        ball.dy *= -1  # Reverse ball's y-axis direction on collision
        x = ball.xcor()  # Move ball slightly to avoid sticking
        if player == player1:
            x += 10  # Move away from Player 1
        else:
            x -= 10  # Move away from Player 2
        ball.setx(x)

# Assigning key bindings for player controls
screen.listen()  # Listen for key inputs
screen.onkeypress(partial(moveBar, bar=player1, barDir="UP"), "w")  # Move Player 1 paddle up
screen.onkeypress(partial(moveBar, bar=player1, barDir="Down"), "s")  # Move Player 1 paddle down
screen.onkeypress(partial(moveBar, bar=player1, barDir="Right"), "d")  # Move Player 1 paddle right
screen.onkeypress(partial(moveBar, bar=player1, barDir="Left"), "a")  # Move Player 1 paddle left

screen.onkeypress(partial(moveBar, bar=player2, barDir="UP"), "Up")  # Move Player 2 paddle up
screen.onkeypress(partial(moveBar, bar=player2, barDir="Down"), "Down")  # Move Player 2 paddle down
screen.onkeypress(partial(moveBar, bar=player2, barDir="Right"), "Right")  # Move Player 2 paddle right
screen.onkeypress(partial(moveBar, bar=player2, barDir="Left"), "Left")  # Move Player 2 paddle left

# Main game loop
while True:
    screen.update()  # Refresh the screen
    moveBall()  # Update ball's position
    colDec(player1)  # Check for collision with Player 1's paddle
    colDec(player2)  # Check for collision with Player 2's paddle

    # If Player 2 misses, Player 1 scores
    if ball.xcor() >= 350:
        score2 += 1  # Increment Player 2's score
        showScore.clear()  # Clear previous score display
        showScore.write(f"Player 1: {score1}        Player 2: {score2}", align="center", font=("Trebuchet MS", 30))
        ball.goto(0, 0)  # Reset ball position to the center
        ball.dx *= -1  # Reverse ball direction

    # If Player 1 misses, Player 2 scores
    if ball.xcor() <= -350:
        score1 += 1  # Increment Player 1's score
        showScore.clear()  # Clear previous score display
        showScore.write(f"Player 1: {score1}        Player 2: {score2}", align="center", font=("Trebuchet MS", 30))
        ball.goto(0, 0)  # Reset ball position to the center
        ball.dx *= -1  # Reverse ball direction
