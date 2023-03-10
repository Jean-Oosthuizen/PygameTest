import pygame, sys, time

class tile():
    def __init__(self,colour,coordinates,size):
        self.colour = colour
        self.coordinates = coordinates
        self.size = size
        self.name = pygame.Surface((self.size,self.size))
        self.name.fill((self.colour))
def drawScreen():
    screen.fill((0,0,0))
    for row in range(len(level)):
        for column in range(len(level[0])):
            if level[row][column] == "d":
                screen.blit(cellD.name,(column*cellSize + 1, row*cellSize + 1))
            else:
                screen.blit(cellA.name,(column*cellSize + 1, row*cellSize + 1))
def eventHandler():
    global active
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and active == False: #life isn't active and you've clicked
            pos = pygame.mouse.get_pos()
            x = -1
            y = -1
            countx = 0
            county = 0
            while x == -1:
                if pos[0] < (countx * cellSize):
                    x = countx - 1
                    while y == -1:
                        if pos[1] < (county * cellSize):
                            y = county - 1
                        county +=1
                countx +=1
            if level[y][x] == "d":
                level[y][x] = "a"
            else:
                level[y][x] = "d"
            pygame.mixer.Sound.play(click)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if active == False:
                    active = True
                else:
                    active = False
            elif event.key == pygame.K_c and active == False: #life isn't active and you clear the screen
                clearLevel()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    drawScreen()
    pygame.display.update()
def nextGeneration():
    nextFrame = []
    for row in range(cellCount):
        nextRow = []
        for column in range(cellCount):
            #we have selected a tile to evaluate
            aCount = 0 #counts the number of living tiles surrounding our selected tile
            tile = level[row][column]
            for i in range(1,4):
                for j in range(1,4):
                    try:
                        if row+2-i < 0 or column+2-j < 0: #if the function is checking a negative array index, which would be on the opposite side of the level
                            pass
                        elif i == 2 and j ==2: #if the function is checking the tile being evaluated
                            pass
                        elif level[row+2-i][column+2-j] == "a": 
                            aCount += 1
                    except: #array index is out of range, which means this is a tile at the edge of the screen and it's trying to check a tile outside the screen
                        pass
            #d = dead, a = alive
            if tile == "a" and aCount in [2,3]:
                #The tile is alive and will stay alive
                nextRow.append("a")
            elif tile == "a" and aCount not in [2,3]:
                #The tile is alive but will die
                nextRow.append("d")
            elif tile == "d" and aCount == 3:
                #The tile is dead but will come alive
                nextRow.append("a")
            else:
                #the tile is dead and will stay dead
                nextRow.append(level[row][column])
        nextFrame.append(nextRow)
    return nextFrame
def createLevel(loops):
    level = []
    for i in range(loops):
        row = []
        for j in range(loops):
            row.append("d")
        level.append(row)
    return level
def clearLevel():
    for i in range(cellCount):
        for j in range(cellCount):
            level[i][j] = "d"

#main
pygame.init()
screenSize = 1000
cellSize = 10
cellCount = screenSize//cellSize

clock=pygame.time.Clock()
screen = pygame.display.set_mode((screenSize,screenSize))
click = pygame.mixer.Sound("click.wav")

#D = dead, A = alive
cellD = tile((40,40,40),(0,0),(cellSize - 1))
cellA = tile((255,255,255),(0,0),(cellSize -1))
generationTimer = 1
level = createLevel(cellCount)

active = False
drawScreen()
pygame.display.update()

while True:
    if active == True: #if life is active after spacebar has been pressed
        generationTimer+=1
        if generationTimer >= 3:
            generationTimer = 0
            level = nextGeneration()
            drawScreen()
            pygame.display.update()
    
    events = pygame.event.get()
    eventHandler()
    clock.tick(60)