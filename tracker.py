import pygame
import random

pygame.init()
pygame.font.init()

BLUE = (0, 0 ,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

displayInfo = pygame.display.Info()
font = pygame.font.SysFont("Ariel", 90)
screenWidth = displayInfo.current_w
screenHeight = displayInfo.current_h
radius = 50
x = random.randint(0 + radius, screenWidth - radius)
y = random.randint(0 + radius, screenHeight - radius)

window = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption("Aim Tracker")

class Button:
    def __init__(self, buttonY, text, color):
        self.buttonY = buttonY
        self.text = text
        self.color = color
    
    def drawButton(self):
        pygame.draw.rect(window, self.color, (2, self.buttonY, 450, 55))
        window.blit(font.render(self.text, True, BLACK), (1, self.buttonY))

modeButton = Button(65, "Mode: Percent", BLUE)
radiusButton = Button(125, "Radius: Set", BLUE)
displayModeButton = Button(185, "Fullscreen", BLUE)
colorButton = Button(245, "Colors", BLUE)

def openMenu():
    menuIsOpen = True

    window.fill(WHITE)
    window.blit(font.render("Settings", True, BLACK), (2, 0))
    modeButton.drawButton()
    radiusButton.drawButton()
    displayModeButton.drawButton()
    colorButton.drawButton()

    while menuIsOpen:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menuIsOpen = False

                    window.fill(WHITE)

            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

openMenu()

while True:
    pygame.time.delay(100)

    """x = random.randint(0 + radius, screenWidth - radius)"""

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                x = random.randint(0 + radius, screenWidth - radius)
                y = random.randint(0 + radius, screenHeight - radius)

                openMenu()

        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.draw.circle(window, (255, 0 , 0), (x, y), radius)

    pygame.display.update()
