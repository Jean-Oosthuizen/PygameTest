import pygame
import sys
import random

pygame.init()
screenWidth = 800
screenHeight = 600
font = pygame.font.SysFont("Arial", 36)
screen = pygame.display.set_mode((screenWidth,screenHeight))

f = open("highscore.txt","r")
tempf = f.readlines()
highscore = tempf[0].strip()
f.close()
score = 0

player = pygame.Surface((50,50))
player.fill((170,0,170))

enemy = pygame.Surface((50,50))
enemy.fill((170,0,0))
enemyx = 50*random.randint(1, 15) - 25
enemyy = 50*random.randint(1, 11) - 25

movex = 0
movey = 0

while True:
    events = pygame.event.get()

    screen.fill((0,0,0))
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movex -= 50
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movey += 50
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movex += 50
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                movey -= 50
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_z:
                print("Player x =", playerx,"player y =",playery)
                print("Enemy x =", enemyx,"enemy y =",enemyy)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    playerx = screenWidth/2 -25 + movex
    playery = screenHeight/2 -25 + movey

    scoreplus = True
    while enemyx-50<playerx<enemyx+50 and enemyy-50<playery<enemyy+50:
        enemyx = 50*random.randint(1, 15) - 25
        enemyy = 50*random.randint(1, 11) - 25
        if scoreplus == True:
            score += 1
            if score > int(highscore):
                f = open("highscore.txt","w")
                f.write(str(score))
                f.close()

            scoreplus = False

    txtsurf = font.render("Your score is: "+str(score)+", high score is: "+str(highscore) , True, (255,255,255))
    screen.blit(txtsurf,(20,15))

    screen.blit(player,(playerx, playery)) #player drawn
    screen.blit(enemy,(enemyx, enemyy))

    pygame.display.update()