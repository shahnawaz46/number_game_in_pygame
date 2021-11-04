import pygame 
import numbergame7
pygame.init()

width = 600
height = 650

white = (255,255,255)
black = (0,0,0)

window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Only for fun")

message_font = pygame.font.SysFont('sans-serif',40)



# game starting function when button is present
def startGame():

    img = pygame.image.load('background.jpg')
    img = pygame.transform.scale(img, (width, height))

    while True:

        window.blit(img, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            # condition is true after pressing mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()      #getting mouse position after mouse pressed

                #  condition true when mouse pressed on button
                if (100 < mouse_pos[0] < 220) and (320 < mouse_pos[1] <350):   
                    numbergame7.gameIsNowStart()
                    # print("game start")

                if (380 < mouse_pos[0] < 500) and (320 < mouse_pos[1] < 350):
                    pygame.quit()
                    quit()
                    # print("exit")


        #  calling printMessageOnScreen() function to print message on screen
        numbergame7.printMessageOnScreen("Random Box Game", black, 180,250, 40)
        numbergame7.printMessageOnScreen("(Develop by Search code)", black, 200, 280, 25)

        # calling drawButton() funtion to draw button
        numbergame7.drawButtons((60, 117, 186 ), 100 ,320, 120,30)
        #  calling printMessageOnScreen() function to print text on button
        numbergame7.printMessageOnScreen("Play", white, 130, 322, 40)

        numbergame7.drawButtons((60, 117, 186 ), 380 ,320, 120, 30)
        numbergame7.printMessageOnScreen("Quit", white, 410, 322, 40)


        # updating dispaly everytime 
        pygame.display.update()
        numbergame7.clock.tick(30)
        

startGame()