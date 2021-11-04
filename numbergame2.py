import pygame


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

            # print one time number and increase Y position
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


# player 1
player_1_x_pos = 25
player_1_y_pos = 525

def playerMove():
    global player_1_x_pos, player_1_y_pos, player_steps

    # delay the time 0.3 second
    pygame.time.delay(300)

    # player move in the forward direction
    if player_1_y_pos in [525,425,325,225,125]:
        if player_1_x_pos == 525:   # when player reach in the last position then change the Y-axis position
            player_1_y_pos -= 50
            player_1_x_pos -= 50

        player_1_x_pos += 50    # now increasing the player position in +ve X-axis direction

    # player move in backward direction
    elif player_1_y_pos in [475,375,275,175,75]:
        if player_1_x_pos == 75:    # when player reach in the last position then change the Y-axis position
            player_1_y_pos -= 50
            player_1_x_pos += 50

        player_1_x_pos -= 50    # now increasing the player position in -ve X-axis direction


clock = pygame.time.Clock()
# game start funtion after user click on play button
def gameIsNowStart():
    player_steps = 0
    button_press = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit
                quit()

            # after keyboard button press condition become true
            if event.type == pygame.KEYDOWN:
                button_press = event.key    # event.key return button value
                
                # condition true when button value in the list
                if button_press in [1073741913,1073741914,1073741915,1073741916,1073741917,1073741918]:
                    player_steps = 1073741912       # button 1 have value = 1073741913
                                                    # button 2 have value = 1073741914  so on
                else:
                    player_steps = 0
                    button_press = 0

        # fill screen with color
        window.fill(white)

        # calling drawLine() function to print lines on screen
        drawLine()

        # calling printNumber() function to print numbers on box
        printNumber(black, 65,65)

        # condition true when player_steps less than button_press value
        if player_steps < button_press:
            playerMove()
            player_steps += 1

        # player_1 shape
        pygame.draw.circle(window, (134, 185, 247), [player_1_x_pos,player_1_y_pos],15)

        # updating the display
        pygame.display.update()
        clock.tick(30)

gameIsNowStart()