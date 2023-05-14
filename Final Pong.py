#Arinjay Singh
#Introduction to Computer Science
#December 19, 2019
#Final Project
##############################
#Pong
#An arcade game of table tennis with 2D graphics
#The ball increases speed every time its hit by a paddle
#The speed of the ball resets every time a player scores
#First player to 3 points wins
##############################

#Import turtle module
import turtle

#Import time module
import time

#Create window
wn = turtle.Screen()
#Set the width to 720 and the height to 520
wn.setup(width = 720, height = 520)
#Turn off turtle animations
wn.tracer(0)

#Pong
#Create a turtle for the pong title
pong = turtle.Turtle()
#Make the pong title's shape blank
pong.shape("blank")
#Pick up the pong title
pong.up()
#Move the position of the pong title down 50
pong.goto(0,-50)
#Write "Pong" in the middle of the screen
pong.write("Pong", font = ("Bookman Old Style", 100, "bold"), align = "center")
#2 second pause
time.sleep(2)
#Clear the pong title's writing
pong.clear()

#Player Names
#Player 1
#Ask for Player 1's name
player1 = wn.textinput("Player 1 name", "Player 1: ")
#Player 2
#Ask for Player 2's name
player2 = wn.textinput("Player 2 name", "Player 2: ")

#Introduce Players
#Create turtle for the intro
intro = turtle.Turtle()
#Make the intro's shape blank
intro.shape("blank")
#Write the players' names
intro.write("{} vs {}".format(player1, player2), font = ("Bookman Old Style", 35, "bold"), align = "center")
#2 second pause
time.sleep(2)
#Clear the writing from the intro
intro.clear()

#Countdown from 3
#Set countdown number to 3
countdown_num = 3
#For loop that repeats 3 times
for x in range(3):
    #Create turtle for the countdown
    countdown = turtle.Turtle()
    #Make the countdown's shape blank
    countdown.shape("blank")
    #Write the current countdown number in the middle of the screen
    countdown.write(countdown_num, font = ("Bookman Old Style", 35, "bold"), align = "center")
    #Subtract 1 from the countdown number every time the loop repeats
    countdown_num -= 1
    #1 second pause
    time.sleep(1)
    #Clear all of the countdown's writing
    countdown.clear()

#Paddles
#Player 1
#Create a turtle for Player 1's paddle
paddle1 = turtle.Turtle()
#Make Player 1's paddle a square
paddle1.shape("square")
#Stretch Player 1's paddle vertically by a ratio of 4
paddle1.shapesize(4,1)
#Pick up Player 1's paddle
paddle1.up()
#Move the position of Player 1's paddle to the left side of the screen
paddle1.goto(-315,0)
#Player 2
#Create a turtle for Player 2's paddle
paddle2 = turtle.Turtle()
#Make Player 2's paddle a square
paddle2.shape("square")
#Stretch Player 2's paddle vertically by a ratio of 4
paddle2.shapesize(4,1)
#Pick up Player 2's paddle
paddle2.up()
#Move the position of Player 2's paddle to the right side of the screen
paddle2.goto(315,0)

#Ball
#Create a turtle for the ball
ball = turtle.Turtle()
#Make the ball's shape a square
ball.shape("square")
#Pick up the ball
ball.up()
#Set the ball's default movement to 1
default_move = 1
#The ball's x-movement is how much the ball's x-coordinate is shifted every time the game is updated
#Set the ball's x-movement to default
ball_xmove = default_move
#The ball's y-movement is how much the ball's y-coordinate is shifted every time the game is updated
#Set the ball's y-movement to default
ball_ymove = default_move

#Line
#Create a turtle for the dashed line in the middle of the screen
line = turtle.Turtle()
#Make the line's shape blank
line.shape("blank")
#Set the line's width to 5
line.pensize(5)
#Pick up the line
line.up()
#Move the line's position to the top of the screen
line.goto(0, 237.5)
#Put the line down
line.down()
#Turn the line's direction 90 degrees to the right
line.right(90)
#For loop that repeats 10 times
for x in range(10):
    #Move the line forward 25 with the line down
    line.forward(25)
    #Pick up the line
    line.up()
    #Move the line forward 25 with the line up
    line.forward(25)
    #Put down the line
    line.down()

#Borders
#Create a turtle for the border
border = turtle.Turtle()
#Make the border's shape blank
border.shape("blank")
#Set the border's with to 5
border.pensize(5)
#Pick up the border
border.up()
#Move the border's position to the top left of the screen
border.goto(-360,260)
#Put down the border
border.down()
#For loop that repeats 2 times
for x in range(2):
    #Move the border forward 720
    #Creates the top and bottom borders
    border.forward(720)
    #Turn the border's direction 90 degrees to the right
    border.right(90)
    #Move the border turtle forward 520
    #Creates the left and right borders
    border.forward(520)
    #Turn the border's direction 90 degrees to the right
    border.right(90)

#Score
#Set Player 1's score to 0 to start game
player1_score = 0
#Set Player 2's score to 0 to start game
player2_score = 0
#Player 1 Score
#Create a turtle for Player 1's score 
score1 = turtle.Turtle()
#Make the shape of Player 1's score blank
score1.shape("blank")
#Pick up Player 1's score
score1.up()
#Move the position of Player 1's score to the top of the screen
score1.goto(-50,205)
#Write Player 1's score
score1.write(player1_score, font = ("Bookman Old Style", 20, "bold"), align = "center")
#Player 1 Name
#Create a turtle for Player 1's name
name1 = turtle.Turtle()
#Make the shape of Player 1's name blank
name1.shape("blank")
#Pick up Player 1's name
name1.up()
#Move the position of Player 1's name to the left of their score
name1.goto(-75,205)
#Write Player 1's name
name1.write(player1, font = ("Bookman Old Style", 20, "bold"), align = "right")
#Player 2 Score
#Create a turtle for Player 2's score
score2 = turtle.Turtle()
#Make the shape of Player 2's score blank
score2.shape("blank")
#Pick up Player 2's score
score2.up()
#Move the position of Player 2's score to the top of the screen
score2.goto(50,205)
#Write player 2's score
score2.write(player2_score, font = ("Bookman Old Style", 20, "bold"), align = "center")
#Player 2 Name
#Create a turtle for Player 2's name
name2 = turtle.Turtle()
#Make the shape of Player 2's name blank
name2.shape("blank")
#Pick up Player 2's name
name2.up()
#Move the position of Player 2's name to the right of their score
name2.goto(75,205)
#Write Player 2's name
name2.write(player2, font = ("Bookman Old Style", 20, "bold"), align = "left")

#Create file to track the scoring of each player
#Open a data file called "Pong.txt" for writing
gamehistory = open("Pong.txt", "w")
#Write the names of the players at the top of the text file
gamehistory.write("{} vs {}\n".format(player1, player2))
#Write "Game History:" in the text file
gamehistory.write("\nScore History:\n")

#Moving Paddle Functions
#Player 1
#Function that moves Player 1's paddle up
def Paddle1Up():
    #Increase the y-coordinate of Player 1's paddle by 30
    paddle1.goto(paddle1.xcor(),paddle1.ycor() + 30)
#Function that moves Player 1's paddle down
def Paddle1Down():
    #Decrease the y-coordinate of Player 1's paddle by 30
    paddle1.goto(paddle1.xcor(),paddle1.ycor() - 30)
#Player 2
#Function that moves Player 2's paddle up
def Paddle2Up():
    #Increase the y-coordinate of Player 2's paddle by 30
    paddle2.goto(paddle2.xcor(),paddle2.ycor() + 30)
#Function that moves Player 2's paddle down
def Paddle2Down():
    #Decrease the y-coordinate of Player 2's paddle by 30
    paddle2.goto(paddle2.xcor(),paddle2.ycor() - 30)

#Keyboard Events
#Set focus on turtle screen to collect key events
wn.listen()
#Player 1 Controls
#Call Paddle1Up function when the "w" key is pressed
#Move Player 1's paddle up
wn.onkey(Paddle1Up, "w")
#Call Paddle1Down function when the "s" key is pressed
#Move Player 1's paddle down
wn.onkey(Paddle1Down, "s")
#Player 2 Controls
#Call Paddle2Up function when the "Up" key is pressed
#Move Player 2's paddle up
wn.onkey(Paddle2Up, "Up")
#Call Paddle2Down function when the "Down" key is pressed
#Move Player 2's paddle down
wn.onkey(Paddle2Down, "Down")

#Updating Game
while True:
    #Update screen
    wn.update()
    #Shift the x-coordinate of the ball by the ball's x-movement value
    #Shift the y-coordinate of the ball by the ball's y-movement value
    ball.goto(ball.xcor() + ball_xmove, ball.ycor() + ball_ymove)
    #Ball Hitting A Wall
    #Top wall
    #If the ball's y-coordinate is greater than 250
    if ball.ycor() > 250:
        #Multiply the ball's y-movement by -1 reversing its vertical movement
        ball_ymove *= -1
    #Bottom wall
    #If the ball's y-coordinate is less than -250
    if ball.ycor() < -250:
        #Multiply the ball's y-movement by -1 reversing its vertical movement
        ball_ymove *= -1
    #Prevent Paddles from going off screen
    #Player 1
    #If the top edge of Player 1's paddle reaches the edge of the screen
    if paddle1.ycor() + 40 > 260:
        #Keep Player 1's paddle on screen
        paddle1.goto(paddle1.xcor(),220)
    #If the bottom edge of Player 1's paddle reaches the edge of the screen
    if paddle1.ycor() - 40 < -260:
        #Keep Player 1's paddle on screen
        paddle1.goto(paddle1.xcor(),-220)
    #Player 2
    #If the top edge of Player 2's paddle reaches the edge of the screen
    if paddle2.ycor() + 40 > 260:
        #Keep Player 2's paddle on screen
        paddle2.goto(paddle2.xcor(),220)
    #If the bottom edge of Player 2's paddle reaches the edge of the screen
    if paddle2.ycor() - 40 < -260:
        #Keep Player 2's paddle on screen
        paddle2.goto(paddle2.xcor(),-220)
    #Ball Hitting A Paddle
    #Player 1
    #If the ball's x-coordinate is inside Player 1's paddle
    if ball.xcor() < -305 and ball.xcor() > -325:
        #And if the ball's y-coordinate is also inside Player 1's paddle
        if ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40:
            #Then move the position of the ball to the right edge of Player 1's paddle
            ball.goto(-305,ball.ycor())
            #Multiply the ball's x-movement by -1 reversing its horizontal movement
            ball_xmove *= -1
            #Increase speed of the ball every time it's hit
            #X-movement
            #If the ball's x-movement is positive 
            if ball_xmove > 0:
                #Increase the ball's x-movement by 1/10 of default speed
                ball_xmove += default_move/10
            #If it's negative
            else:
                #Decrease the ball's x-movement by 1/10 of default speed
                ball_xmove -= default_move/10
            #Y-movement
            #If the ball's y-movement is positive
            if ball_ymove > 0:
                #Increase the ball's y-movement by 1/10 of default speed
                ball_ymove += default_move/10
            #If it's negative
            else:
                #Decrease the ball's y-movement by 1/10 of default speed
                ball_ymove -= default_move/10
    #Player 2
    #If the ball's x-coordinate is inside Player 2's paddle
    if ball.xcor() > 305 and ball.xcor() < 325:
        #And if the ball's y-coordinate is also inside Player 2's paddle
        if ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40:
            #Then move the position of the ball to the left edge of Player 2's paddle
            ball.goto(305,ball.ycor())
            #Multiply the ball's x-movement by -1 reversing its horizontal movement
            ball_xmove *= -1
            #Increase speed of the ball every time it's hit
            #X-movement
            #If the ball's x-movement is positive
            if ball_xmove > 0:
                #Increase the ball's x-movement by 1/10 of default speed
                ball_xmove += default_move/10
            #If it's negative
            else:
                #Decrease the ball's x-movement by 1/10 of default speed
                ball_xmove -= default_move/10
            #Y-movement
            #If the ball's y-movement is positive
            if ball_ymove > 0:
                #Increase the ball's y-movement by 1/10 of default speed
                ball_ymove += default_move/10
            #If it's negative
            else:
                #Decrease the ball's y-movement by 1/10 of default speed
                ball_ymove -= default_move/10
    #Scoring
    #If the ball's x-coordinate passes Player 2's paddle, Player 1 scores
    if ball.xcor() > 350:
        #Add 1 point to Player 1's score
        player1_score += 1
        #Clear Player 1's previous score
        score1.clear()
        #Write Player  1's updated score
        score1.write(player1_score, font = ("Bookman Old Style", 20, "bold"), align = "center")
        #Write Player 1 scored in the game history text file
        gamehistory.write("\n{} Scores!\n".format(player1))
        #Write how many total points Player 1 has
        gamehistory.write("{}: {}   ".format(player1, player1_score))
        #Write how many total points Player 2 has
        gamehistory.write("{}: {}\n".format(player2, player2_score))
        #Reset the ball's position to the middle of the screen
        ball.goto(0,0)
        #Multiply the ball's x-movement by -1 reversing its horizontal movement
        ball_xmove *= -1
        #Resetting the speed of the ball
        #If the ball's x-movement is positive
        if ball_xmove > 0:
            #Reset the ball's x-movement to default
            ball_xmove = default_move
        #If it's negative
        else:
            #Reset the ball's x-movement to the opposite of default
            ball_xmove = default_move * -1
        #If the ball's y-movement is positive
        if ball_ymove > 0:
            #Reset the ball's y-movement to default
            ball_ymove = default_move
        #If it's negative
        else:
            #Reset the ball's y-movement to the opposite of default
            ball_ymove = default_move * -1
    #If the ball's x-coordinate passes Player 1's paddle, Player 2 scores
    if ball.xcor() < -350:
        #Add 1 point to Player 2's score
        player2_score += 1
        #Clear Player 2's previous score
        score2.clear()
        #Write Player 2's updated score
        score2.write(player2_score, font = ("Bookman Old Style", 20, "bold"), align = "center")
        #Write Player 2 scored in the game history text file
        gamehistory.write("\n{} Scores!\n".format(player2))
        #Write how many total points Player 1 has
        gamehistory.write("{}: {}   ".format(player1, player1_score))
        #Write how many total points Player 2 has
        gamehistory.write("{}: {}\n".format(player2, player2_score))
        #Reset the ball's position to the middle of the screen
        ball.goto(0,0)
        #Multiply the ball's x-movement by -1 reversing its horizontal movement
        ball_xmove *= -1
        #Resetting the speed of the ball
        #If the ball's x-movement is positive
        if ball_xmove > 0:
            #Reset the ball's x-movement to default
            ball_xmove = default_move
        #If it's negative
        else:
            #Reset the ball's x-movement to the opposite of default
            ball_xmove = default_move * -1
        #If the ball's y-movement is positive
        if ball_ymove > 0:
            #Reset the ball's y-movement to default
            ball_ymove = default_move
        #If it's negative
        else:
            #Reset the ball's y-movement to the opposite of default
            ball_ymove = default_move * -1
    #If one of the players gets 3 points the game is over
    if player1_score == 3 or player2_score == 3:
        #Close the game history text file
        gamehistory.close()
        #Break the while loop
        break

#Clear screen
wn.clear()

#Winning Screen
#Create a turtle for the winning screen
winner = turtle.Turtle()
#Make the winner's shape blank
winner.shape("blank")
#If Player 1 had 3 points
if player1_score == 3:
    #Write Player 1 wins
    winner.write("{} Wins!".format(player1), font = ("Bookman Old Style", 35, "bold"), align = "center")
#If Player 2 had 3 points
elif player2_score == 3:
    #Write Player 2 wins
    winner.write("{} Wins!".format(player2), font = ("Bookman Old Style", 35, "bold"), align = "center")

#2 second pause
time.sleep(2)

#Clear screen
wn.clear()

#Game History
#Open the game history text file
with open("Pong.txt", "r") as gamehistory:
    #Create a turtle for the game history
    history = turtle.Turtle()
    #Make the game history's shape blank
    history.shape("blank")
    #Pick up the game history
    history.up()
    #Move the position of the game history to the bottom of the page
    history.goto(0,-210)
    #Write the entire game history text file
    history.write(gamehistory.read(), font = ("Bookman Old Style", 15, "normal"), align = "center")
    
