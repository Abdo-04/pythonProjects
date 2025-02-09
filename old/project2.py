import pygame
pygame.init()

window = pygame.display.set_mode((800, 400))
class Player():
    def __init__(self,x,y):
        self.x=x
        self.y=y
player = Player(400,200)
pygame.display.flip()

isRunning = True
while isRunning:
    events = pygame.event.get()
    for i in range(len(events)):
        if events[i].type == pygame.QUIT:
            isRunning = False
        elif events[i].type == pygame.KEYDOWN:
            if events[i].key == pygame.K_DOWN:
                player.y = player.y - 10
            elif events[i].type == pygame.K_UP:
                player.y = player.y + 10
            elif events[i].type == pygame.K_LEFT:
                player.x = player.x - 10
            elif events[i].type == pygame.K_RIGHT:
                player.x = player.x + 10

    window.fill((0,0,0))
    pygame.draw.circle(window, (117, 207, 217), (player.x, player.y), 20)
    pygame.draw.circle(window, (166, 136, 194), (300, 100), 20)
    pygame.display.flip()


