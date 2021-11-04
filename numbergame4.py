import pygame
import random
from playerwinthegame import winnerPlayer
from win32api import MessageBox

pygame.init()

width = 600
height = 650

white = (255,255,255)
black = (0,0,0)

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Only for fun")


# drawing lines Vertically and horizontally
def drawLine():
    x1, y1, x2, y2 = 50, 50, 550, 50 
    for _ in range(11):
        # draw horizontal line
        pygame.draw.line(window, black, [x1,y1], [x2,y2], 3)
        # draw vertical line
        pygame.draw.line(window, black, [y1,x1], [y2,x2], 3)
        # increase the Y-axis position
        y1 += 50
        y2 += 50

                
number_font = pygame.font.SysFont('Arial',20)

# box_draw = [130,250,90,370,250]

# printing number in the box
def printNumber(color, x_pos, y_pos):
    x = 1
    num = 100
    while num > 0:
        if x <= 20:
            text = number_font.render(str(num), True, color)

            # print number from left to right
            if x<=10:
                window.blit(text, [x_pos, y_pos])
                x_pos += 50     # increase X-axis position

            # increase Y-axis position
            if x == 11:
                y_pos += 50

            # print number from right to left
            if x>10 and x<=20:
                x_pos -= 50     # decrease X-axis position
                window.blit(text, [x_pos, y_pos])
        
            x += 1
            num = int(num)-1

        # increasing Y position and reset X position
        else:
            x = 1
            # x_pos = 50
            y_pos += 50



# print message on screen
def printMessageOnScreen(message, color, x_pos, y_pos, font_size):
    message_font = pygame.font.SysFont('sans-serif', font_size)

    text = message_font.render(message, True, color)
    window.blit(text, [x_pos,y_pos])    # window.blit means show message on screen


# create button
def drawButtons(color, button_x_pos, button_y_pos, button_width, button_height):

    # draw rectangle box
    pygame.draw.rect(window, color, [button_x_pos, button_y_pos, button_width, button_height])


# player 1
player_1_x_pos = 25
player_1_y_pos = 525

def player1ForwardMove():
    global player_1_x_pos, player_1_y_pos

    pygame.time.delay(200)

    # player move in the forward direction
    if player_1_y_pos in [525,425,325,225,125]:
        if player_1_x_pos == 525:   # when player reach in the last position then change the Y-axis position
            player_1_y_pos -= 50
            player_1_x_pos -= 50

        player_1_x_pos += 50    # now increasing the player postion in +ve X-axis direction

    # player move in the backwards direction
    elif player_1_y_pos in [475,375,275,175,75]:
        if player_1_x_pos == 75:    # when player reach in the last then change the Y-axis position
            player_1_y_pos -= 50
            player_1_x_pos += 50

        player_1_x_pos -= 50    # now increasing the player postion in -ve X-axis direction
    
    if player_1_x_pos == 75 and player_1_y_pos == 25:
        winnerPlayer("player 1 win the game")


def player1BackwardsMove():
    global player_1_x_pos, player_1_y_pos

    # delay the time 0.3 second
    pygame.time.delay(100)

    # player move in the backwards direction
    if player_1_y_pos in [525,425,325,225,125]:
        if player_1_x_pos == 65:   # when player reach in the last position then change the Y-axis position
            player_1_y_pos += 50
            player_1_x_pos += 50

        player_1_x_pos -= 50    # now increasing the player position in -ve X-axis direction

    # player move in forward direction
    elif player_1_y_pos in [475,375,275,175,75]:
        if player_1_x_pos == 525:    # when player reach in the last position then change the Y-axis position
            player_1_y_pos += 50
            player_1_x_pos -= 50

        player_1_x_pos += 50    # now increasing the player position in +ve X-axis direction


# player 2
player_2_x_pos = 25
player_2_y_pos = 525

def player2ForwardMove():
    global player_2_x_pos, player_2_y_pos
    
    pygame.time.delay(200)

    if player_2_y_pos in [525,425,325,225,125]:
        if player_2_x_pos == 525:
            player_2_y_pos -= 50
            player_2_x_pos -= 50

        player_2_x_pos += 50

    elif player_2_y_pos in [475,375,275,175,75]:
        if player_2_x_pos == 75:
            player_2_y_pos -= 50
            player_2_x_pos += 50

        player_2_x_pos -= 50

    if player_2_x_pos == 75 and player_2_y_pos == 25:
        winnerPlayer("Player 2 win the game")


def player2BackwardsMove():
    global player_2_x_pos, player_2_y_pos

    pygame.time.delay(100)

    if player_2_y_pos in [525,425,325,225,125]:
        if player_2_x_pos == 65:
            player_2_y_pos += 50
            player_2_x_pos += 50

        player_2_x_pos -= 50

    elif player_2_y_pos in [475,375,275,175,75]:
        if player_2_x_pos == 525:
            player_2_y_pos += 50
            player_2_x_pos -= 50

        player_2_x_pos += 50


# variables for player forward move, backward move, forward steps and backward steps 
player_1_f_move = 100
player_2_f_move = 100

player_1_b_move = 0
player_2_b_move = 0

player_1_f_steps = 0
player_2_f_steps = 0

player_1_b_steps = 0
player_2_b_steps = 0

def checkPlayerIsOnTheColorBox():
    global player_1_f_move, player_2_f_move
    global player_1_b_move, player_2_b_move

    global player_1_f_steps, player_2_f_steps
    global player_1_b_steps, player_2_b_steps

    # check player_1_x_pos to the box position
    if (player_1_f_move == player_1_f_steps) and ((player_1_x_pos == 225 and player_1_y_pos == 475) or (player_1_x_pos == 475 and player_1_y_pos == 375) or (player_1_x_pos == 125 and player_1_y_pos == 275) or (player_1_x_pos == 375 and player_1_y_pos == 175) or (player_1_x_pos == 175 and player_1_y_pos == 75)):
        
        random_num = random.randint(1,6)

        msg = random.choice([f"You are Lucky, You are going to {random_num} step forward",f"You are Unlucky, You are going to {random_num} step backword"])
        MessageBox(None,msg,"Warning!")     # print message on screen by MessageBox

        if "Lucky" in msg:
            player_1_f_move = 0
            player_1_f_steps = random_num
            # print("f1")

        elif "Unlucky" in msg:
            player_1_b_move = 0
            player_1_b_steps = random_num
            # print("b1")
    
    #check player_2_postion to the box position
    elif (player_2_f_move == player_2_f_steps) and ((player_2_x_pos == 225 and player_2_y_pos == 475) or (player_2_x_pos == 475 and player_2_y_pos == 375) or (player_2_x_pos == 125 and player_2_y_pos == 275) or (player_2_x_pos == 375 and player_2_y_pos == 175) or (player_2_x_pos == 175 and player_2_y_pos == 75)):
        
        random_num = random.randint(1,6)

        msg = random.choice([f"You are Lucky, You are going to {random_num} step forward",f"You are Unlucky, You are going to {random_num} step backword"])
        MessageBox(None,msg,"Warning!")
        
        if "Lucky" in msg:
            player_2_f_move = 0
            player_2_f_steps = random_num
            # print("f2")

        elif "Unlucky" in msg:
            player_2_b_move = 0
            player_2_b_steps = random_num
            # print("b2")


clock = pygame.time.Clock()
# game start funtion after user click on play button
def gameIsNowStart():
    global player_1_f_move, player_2_f_move
    global player_1_f_steps, player_2_f_steps

    global player_1_b_move, player_2_b_move
    global player_1_b_steps, player_2_b_steps
    
    player_step = 0

    clicked = True

    x = 1

    while True:
        # fill screen with color
        window.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            # condition is true after pressing mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()      #getting mouse position after mouse pressed

                #  condition true, when mouse pressed on button and clicked == True
                if (100 < mouse_pos[0] < 220) and (580 < mouse_pos[1] < 610) and clicked:
                    player_1_f_steps = random.randint(1,6)
                    player_1_f_move = 0
                    player_step = player_1_f_steps
                    clicked = False     # now assign False to the clicked variable

                #  condition true, when mouse pressed on button and clicked == False
                elif (380 < mouse_pos[0] < 500) and (580 < mouse_pos[1] < 610) and not clicked:
                    player_2_f_steps = random.randint(1,6)
                    player_2_f_move = 0
                    player_step = player_2_f_steps
                    clicked = True      # now assign True to the clicked variable


        # calling drawLine() function to print lines on screen
        drawLine()

        # calling printNumber() function to print numbers on box
        printNumber(black, 65,65)

        # draw black box 
        drawButtons(black, 200, 450, 50, 50)
        drawButtons(black, 450, 350, 50, 50)
        drawButtons(black, 100, 250, 50, 50)
        drawButtons(black, 350, 150, 50, 50)
        drawButtons(black, 150, 50, 50, 50)


        # call checkPlayerIsOnTheColorBox() function to check player_pos to the box position
        checkPlayerIsOnTheColorBox()


        # condition true when player 1 pressed button
        if player_1_f_move < player_1_f_steps:
            player1ForwardMove()       # call player1ForwardMove() function to move player 1 position
            player_1_f_move += 1    
        

        # condition true when player_1_pos in the box position
        if player_1_b_move < player_1_b_steps:
            player1BackwardsMove()      # call player1BackwardsMove() function to move player 1 position
            player_1_b_move += 1


        # condition true when player 2 pressed button
        if player_2_f_move < player_2_f_steps:
            player2ForwardMove()       # call player2ForwardMove() function to move player 2 position
            player_2_f_move += 1

        # condition true when player_2_pos in the box position
        if player_2_b_move < player_2_b_steps:
            player2BackwardsMove()      # call player2BackwardsMove() function to move player 1 position
            player_2_b_move += 1

        # printing player step on screen
        printMessageOnScreen(str(player_step), black, 290, 580, 40)

        # player 1 button
        drawButtons((0,0,0),100, 580, 120, 30)    # calling drawButton() funtion to draw button
        printMessageOnScreen("Player 1", (255,255,255), 105, 582, 40)   #  calling printMessageOnScreen() function to print message on button

        # player 2 button
        drawButtons((0,0,0),380, 580, 120, 30)
        printMessageOnScreen("Player 2", (255,255,255), 385, 582, 40)

        # player_1 shape
        pygame.draw.circle(window, (199, 0, 57), [player_1_x_pos,player_1_y_pos],15)
        printMessageOnScreen("1",white, player_1_x_pos-4, player_1_y_pos-6,20)

        # player_2 shape
        pygame.draw.circle(window, (255, 195, 0), [player_2_x_pos,player_2_y_pos],15)
        printMessageOnScreen("2",white, player_2_x_pos-4, player_2_y_pos-6,20)

        pygame.display.update()
        clock.tick(30)


gameIsNowStart()