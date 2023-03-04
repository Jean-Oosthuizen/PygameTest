import pygame, sys

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
    for row in range(0,len(level)):
        for column in range(0,len(level[0])):
            if level[row][column] == "a":
                screen.blit(cellA.name,(column*cellSize + 1, row*cellSize + 1))
            if level[row][column] == "b":
                screen.blit(cellB.name,(column*cellSize + 1, row*cellSize + 1))
def eventHandler():
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
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
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


pygame.init()
screenSize = 500
screen = pygame.display.set_mode((screenSize,screenSize))

cellSize = 50
cellA = cell((40,40,40),(0,0),(48))
cellB = cell((255,255,255),(0,0),(48))

click = pygame.mixer.Sound("click.wav")

level = [["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a"],]


while True:

    drawScreen()
    events = pygame.event.get()
    eventHandler()
    pygame.display.update()