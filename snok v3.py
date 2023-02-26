import pygame

class player():
    def __init__(self,colour,health,coordinates,size):
        self.colour = colour
        self.health = health
        self.coordinates = coordinates
        self.size = size
        self.name = pygame.Surface(self.size)
        self.name.fill((0,200,0))
    def __str__(self):
        return f"This object{self.colour} has {self.health} hp. It is at coordinates: {self.coordinates}"

def inputAndCollision(playerx,playery):
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                playerx -= 10
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                playery += 10
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                playerx += 10
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                playery -= 10
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    return playerx, playery

pygame.init()
screen = pygame.display.set_mode((500,500))

level = [["a","b"],["b","a"]]

p1 = player((0,200,0), 100, (50,20), (50,50))
print(p1)

while True:
    screen.fill((0,0,0))
    events = pygame.event.get()
    p1.coordinates = inputAndCollision(p1.coordinates[0],p1.coordinates[1])
    screen.blit(p1.name,p1.coordinates)
    pygame.display.update()