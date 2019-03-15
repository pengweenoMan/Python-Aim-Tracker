import pygame
import random

pygame.init()

gameIsRunning = True
radius = 50
x = random.randint(0 + radius, 800 - radius)
y = random.randint(0 + radius, 800 - radius)

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Aim Tracker")

def openMenu():
    menuIsOpen = True

    while menuIsOpen:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menuIsOpen = False
        
        pygame.draw.rect(window, (0, 0, 255), (50, 50))

openMenu()

while gameIsRunning:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                openMenu()

        if event.type == pygame.QUIT:
            gameIsRunning = False

    pygame.draw.circle(window, (255, 0 , 0), (x, y), radius)

    pygame.display.update()