import pygame, sys, time

class cell():
    def __init__(self,colour,coordinates,size):
        self.colour = colour
        self.coordinates = coordinates
        self.size = size
        self.name = pygame.Surface((self.size,self.size))
        self.name.fill((self.colour))
    def __str__(self):
        return f"This object has a colour of {self.colour}. It is at coordinates: {self.coordinates}"
def drawScreen():
    screen.fill((0,0,0))
    for row in range(len(level)):
        for column in range(len(level[0])):
            if level[row][column] == "a":
                screen.blit(cellA.name,(column*cellSize + 1, row*cellSize + 1))
            if level[row][column] == "b":
                screen.blit(cellB.name,(column*cellSize + 1, row*cellSize + 1))
def eventHandler():
    global ready
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN and ready == False:
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
            if level[y][x] == "a":
                level[y][x] = "b"
            else:
                level[y][x] = "a"
            pygame.mixer.Sound.play(click)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:
                if ready == False:
                    ready = True
                else:
                    ready = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
def nextGeneration():
    nextFrame = []
    for row in range(cellCount):
        nextRow = []
        for column in range(cellCount):
            #we have selected a tile to evaluate
            bCount = 0
            cell = level[row][column]
            for i in range(1,4):
                for j in range(1,4):
                    try:
                        if row+2-i < 0 or column+2-j < 0:
                            pass
                        elif i == 2 and j ==2:
                            pass
                        elif level[row+2-i][column+2-j] == "b":
                            bCount += 1
                    except:
                        pass
            if cell == "b" and bCount in [2,3]:# a = dead, b = alive
                note = "The cell at "+str(column+1)+"x, "+str(row+1)+"y is alive and will stay alive"
                nextRow.append("b")
            elif cell == "b" and bCount not in [2,3]:
                note = "The cell at "+str(column+1)+"x, "+str(row+1)+"y is alive but will die"
                nextRow.append("a")
            elif cell == "a" and bCount == 3:
                note = "The cell at "+str(column+1)+"x, "+str(row+1)+"y is dead but will come alive"
                nextRow.append("b")
            else:
                nextRow.append(level[row][column])
        nextFrame.append(nextRow)
    return nextFrame
def createLevel(loops):
    level = []
    for i in range(loops):
        row = []
        for j in range(loops):
            row.append("a")
        level.append(row)
    return level



#main
pygame.init()
screenSize = 100
cellSize = 20
tickSpeed = 0.1
cellCount = screenSize//cellSize

screen = pygame.display.set_mode((screenSize,screenSize))
click = pygame.mixer.Sound("click.wav")

cellA = cell((40,40,40),(0,0),(cellSize - 1))
cellB = cell((255,255,255),(0,0),(cellSize -1))

level = createLevel(cellCount)

ready = False
while True:
    if ready == True:
        level = nextGeneration()
        time.sleep(tickSpeed)
    drawScreen()
    events = pygame.event.get()
    eventHandler()
    pygame.display.update()