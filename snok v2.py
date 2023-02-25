import pygame
import sys
import random

level = [["r","b","r","b"],["b","r","b","r"],["r","b","r","b"],["b","r","b","r"]]
pygame.init()
screenSize = 800
cellCount = len(level)
cellSize = screenSize/cellCount
screen = pygame.display.set_mode((screenSize,screenSize))

red = pygame.Surface((cellSize,cellSize))
red.fill((200,0,0))

blue = pygame.Surface((cellSize,cellSize))
blue.fill((0,0,200))

player = pygame.Surface((cellSize/2,cellSize/2))
player.fill((0,200,0))
movex = 0
movey = 0

while True:
    events = pygame.event.get()
    
    screen.fill((0,0,0))
    for row in range(0,len(level)):
        for column in range(0,len(level[0])):
            if level[row][column] == "r":
                screen.blit(red,(column*cellSize, row*cellSize))
            elif level[row][column] == "b":
                screen.blit(blue,(column*cellSize, row*cellSize))

    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if movex > 0:
                    movex -= cellSize
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if movey < screenSize - cellSize:
                    movey += cellSize
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if movex < screenSize - cellSize:
                    movex += cellSize
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if movey > 0:
                    movey -= cellSize
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_z:
                print("Player x =", playerx,"player y =",playery)
                print("Enemy x =", enemyx,"enemy y =",enemyy)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(player,(cellSize/4 + movex,cellSize/4 + movey))



    pygame.display.update()