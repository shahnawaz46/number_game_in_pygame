import pygame
import random
from playerwinthegame import winnerPlayer

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


message_font = pygame.font.SysFont('sans-serif',40)

# print message on screen
def printMessageOnScreen(message, color, x_pos,y_pos):
    text = message_font.render(message, True, color)
    window.blit(text, [x_pos,y_pos])    # window.blit means show message on screen


# create button
def drawButtons(color, button_x_pos, button_y_pos):
    button_width = 120
    button_height = 30

    # draw rectangle box
    pygame.draw.rect(window, color, [button_x_pos, button_y_pos, button_width, button_height])


# player 1
player_1_x_pos = 25
player_1_y_pos = 525

def player1Move():
    global player_1_x_pos, player_1_y_pos

    pygame.time.delay(50)

    if player_1_y_pos in [525,425,325,225,125]:
        if player_1_x_pos == 525:
            player_1_y_pos -= 50
            player_1_x_pos -= 50

        player_1_x_pos += 50

    elif player_1_y_pos in [475,375,275,175,75]:
        if player_1_x_pos == 75:
            player_1_y_pos -= 50
            player_1_x_pos += 50

        player_1_x_pos -= 50

    if player_1_x_pos == 75 and player_1_y_pos == 25:
        winnerPlayer("player 1 win the game")

# player 2
player_2_x_pos = 25
player_2_y_pos = 525

def player2Move():
    global player_2_x_pos, player_2_y_pos

    pygame.time.delay(50)

    if player_2_y_pos in [525,425,325,225,125]:
        if player_2_x_pos == 525:       # when player reach in the last then change the Y-axis position
            player_2_y_pos -= 50
            player_2_x_pos -= 50

        player_2_x_pos += 50    # now increasing the player poistion in +ve X-axis direction

    elif player_2_y_pos in [475,375,275,175,75]:
        if player_2_x_pos == 75:    # when player reach in the last then change the Y-axis position
            player_2_y_pos -= 50
            player_2_x_pos += 50

        player_2_x_pos -= 50    # now increasing the player position in -ve X-axis direction

    if player_2_x_pos == 75 and player_2_y_pos == 25:
        winnerPlayer("Player 2 win the game")

clock = pygame.time.Clock()
# game start funtion after user click on play button
def gameIsNowStart():
    player_1_steps = 0
    player_2_steps = 0

    x = 0
    y = 0

    clicked = True
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            # condition is true after pressing mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()      #getting mouse position after mouse pressed

                #  condition true when mouse pressed on button
                if (100 < mouse_pos[0] < 220) and (580 < mouse_pos[1] < 610) and clicked:
                    player_1_steps = random.randint(1,6)
                    x = 0
                    clicked = False
                    print(player_1_steps)

                elif (380 < mouse_pos[0] < 500) and (580 < mouse_pos[1] < 610) and (not clicked):
                    player_2_steps = random.randint(1,6)
                    y = 0
                    clicked = True
                    print(player_2_steps)

        # fill screen with color
        window.fill(white)

        # calling drawLine() function to print lines on screen
        drawLine()

        # calling printNumber() function to print numbers on box
        printNumber(black, 65,65)

        # player 1 button
        drawButtons(black,100, 580)    # calling drawButton() funtion to draw button
        printMessageOnScreen("Player 1", white, 105, 582)   #  calling printMessageOnScreen() function to print message on button

        # player 2 button
        drawButtons(black,380, 580)
        printMessageOnScreen("Player 2", white, 385, 582)

        if x < player_1_steps:
            player1Move()       # call player1move() function to move player 1 position
            x += 1

        elif y < player_2_steps:
            player2Move()       # call player2move() function to move player 2 position
            y += 1


        # player_1 shape
        pygame.draw.circle(window, (199, 0, 57), [player_1_x_pos,player_1_y_pos],15)
        # window.blit(pygame.font.SysFont('Arial',15,bold='Bold').render('1',False, black), [player_1_x_pos-4, player_1_y_pos-9])

        # player_2 shape
        pygame.draw.circle(window, (255, 195, 0), [player_2_x_pos,player_2_y_pos],15)
        # window.blit(pygame.font.SysFont('Arial',15,bold='Bold').render('2',False, black), [player_2_x_pos-4, player_2_y_pos-9])

        pygame.display.update()
        clock.tick(30)


gameIsNowStart()