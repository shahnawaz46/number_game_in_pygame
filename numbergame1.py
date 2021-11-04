import pygame


pygame.init()

width = 500
height = 500

white = (255,255,255)
black = (0,0,0)

window = pygame.display.set_mode((width,height))

# drawing lines Vertically and horizontally
def drawLine():
    x1, y1, x2, y2 = 40, 40, 440, 40 
    for _ in range(11):
        # draw horizontal line
        pygame.draw.line(window, black, [x1,y1], [x2,y2], 3)
        # draw vertical line
        pygame.draw.line(window, black, [y1,x1], [y2,x2], 3)
        # increase the Y-axis position
        y1 += 40
        y2 += 40

                
number_font = pygame.font.SysFont(None,20)

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
                x_pos += 40

            # print one time number and increase Y position
            if x == 11:
                y_pos += 40

            # print number from right to left
            if x>10 and x<=20:
                x_pos -= 40
                window.blit(text, [x_pos, y_pos])
        
            x += 1
            num = int(num)-1

        # increasing Y position and reset X position
        else:
            x = 1
            x_pos = 50
            y_pos += 40


player_1_x_pos = 20
player_1_y_pos = 420

def forwadMovement(event):
    global player_1_x_pos, player_1_y_pos

    # print(player_1_x_pos, player_1_y_pos)
    if player_1_x_pos == 420:
        player_1_y_pos -= 40
        return

    if event.key == pygame.K_KP_1:
        player_1_x_pos += 40
    elif event.key == pygame.K_KP_2:
        player_1_x_pos += 80
    elif event.key == pygame.K_KP_3:
        player_1_x_pos += 120
    elif event.key == pygame.K_KP_4:
        player_1_x_pos += 160
    elif event.key == pygame.K_KP_5:
        player_1_x_pos += 200
    elif event.key == pygame.K_KP_6:
        player_1_x_pos += 240


def backwordMovement(event):
    global player_1_x_pos, player_1_y_pos

    if player_1_x_pos == 60:
        player_1_y_pos -= 40
        return

    if event.key == pygame.K_KP_1:
        player_1_x_pos -= 40
    elif event.key == pygame.K_KP_2:
        player_1_x_pos -= 80
    elif event.key == pygame.K_KP_3:
        player_1_x_pos -= 120
    elif event.key == pygame.K_KP_4:
        player_1_x_pos -= 160
    elif event.key == pygame.K_KP_5:
        player_1_x_pos -= 200
    elif event.key == pygame.K_KP_6:
        player_1_x_pos -= 240


clock = pygame.time.Clock()

# game start funtion after user click on play button
def gameIsNowStart():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if player_1_y_pos in [420,340,260,180,100]:
                    forwadMovement(event)
                elif player_1_y_pos in [380,300,220,140,60]:
                    backwordMovement(event)

        # fill screen with color
        window.fill(white)

        # calling drawLine() function to print lines on screen
        drawLine()

        # calling printNumber() function to print numbers on box
        printNumber(black, 50,55)

        # player shape
        pygame.draw.circle(window, (134, 185, 247), [player_1_x_pos,player_1_y_pos],10)


        pygame.display.update()

        clock.tick(30)

gameIsNowStart()