import pygame
import sys
import random
import time

def loadLevel(): #reads from a template level and places it into a 2D array
    level = []

    f = open("level.txt","r")
    template = f.readlines()
    f.close()

    cols = len(template[0].strip())
    rows = len(template)
    
    for i in range(0,rows):
        line = template[i]
        tempRow = []
        for j in range(0,cols):
            if line[j] == "p":
                playerx = j
                playery = i
            tempRow.append(line[j])
        level.append(tempRow)
    return level, cols, playerx, playery

def drawBackground():
    screen.fill((0,0,0))
    for row in range(0,len(level)):
        for column in range(0,len(level[0])):
            if level[row][column] == "r":
                screen.blit(red,(column*cellSize, row*cellSize))
            elif level[row][column] == "b":
                screen.blit(blue,(column*cellSize, row*cellSize))
            elif level[row][column] == "k":
                screen.blit(key,(column*cellSize, row*cellSize))
            elif level[row][column] == "d":
                screen.blit(door,(column*cellSize, row*cellSize))
            elif level[row][column] == "e":
                screen.blit(end,(column*cellSize, row*cellSize))
            elif level[row][column] == "p":
                screen.blit(startBlock,(column*cellSize, row*cellSize))

def inputAndCollision(playerx,playery):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                if level[playery][playerx-1] != "x" and not (level[playery][playerx-1] == "d" and keyUp == False):
                    playerx -= 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                if level[playery+1][playerx] != "x" and not (level[playery+1][playerx] == "d" and keyUp == False):
                    playery += 1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                if level[playery][playerx+1] != "x" and not (level[playery][playerx+1] == "d" and keyUp == False):
                    playerx += 1
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                if level[playery-1][playerx] != "x" and not (level[playery-1][playerx] == "d" and keyUp == False):
                    playery -= 1
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    return playerx, playery

pygame.init()

font = pygame.font.SysFont("Arial", 36)
screenSize = 800
level, cellCount, playerx, playery = loadLevel()
cellSize = screenSize/cellCount
screen = pygame.display.set_mode((screenSize,screenSize))

red = pygame.Surface((cellSize,cellSize))
red.fill((200,0,0))

blue = pygame.Surface((cellSize,cellSize))
blue.fill((0,0,200))

player = pygame.Surface((cellSize/2,cellSize/2))
player.fill((0,200,0))
playerx = 1
playery = 1

key = pygame.Surface((cellSize,cellSize))
key.fill((190,190,0))

door = pygame.Surface((cellSize,cellSize))
door.fill((90,90,0))
keyUp = False #tracks if the key has been picked up yet or not

end = pygame.Surface((cellSize,cellSize))
end.fill((0,255,0))
endLevel = False

startBlock = pygame.Surface((cellSize,cellSize))
startBlock.fill((255,255,255))

startTime = time.time()
while endLevel == False:
    events = pygame.event.get()
    drawBackground()
    playerx, playery = inputAndCollision(playerx,playery)

    if level[playery][playerx] == "k": #checks if the player should pick up a key, replaces key with door item
        level[playery][playerx] = "d"
        keyUp = True

    screen.blit(player,(cellSize/4 + playerx*cellSize,cellSize/4 + playery*cellSize)) #draws player
    if level[playery][playerx] == "e": #checks to see if the player is at the end of the level
        text = font.render("You took "+str(round((time.time()-startTime),3))+" seconds.",True,(255,255,255))
        screen.blit(text,(screenSize/2-50,screenSize/2))
        endLevel = True
    pygame.display.update()
time.sleep(3)
pygame.quit()
sys.exit()