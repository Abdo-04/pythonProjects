import pygame
from bird import Bird
from obsticale import obstacle
pygame.init()

clock = pygame.time.Clock()

window = pygame.display.set_mode((864, 512))
pygame.display.set_caption("Megz Level 2 - Flappy Bird")

bgImg = pygame.image.load("assets/Objects/background-day.png").convert()

pipeTop = pygame.image.load("assets/Objects/pipe-green.png").convert()
pipeBottom = pygame.transform.rotate(pipeTop, 180)

bird = Bird(50,10)
obsticale =[obstacle (870),obstacle (1270),obstacle (1670)]

running = True
while running:
    events = pygame.event.get()
    for i in range(len(events)):
        if events[i].type == pygame.QUIT:
            running = False
        elif events[i].type == pygame.KEYDOWN:
            if events[i].key == pygame.K_SPACE:
                bird.up()

    onScreen = bird.update()
    if onScreen ==False :
        onScreen = False

    for i in range(len(obsticale)):
        obsticale[i].update()
    rectBird = bird.getRect()
    for i in range(len(obsticale)):
        rectobstacle = obsticale[i].getRect()
        if rectBird.colliderect(rectobstacle[0]) or rectBird.colliderect((rectobstacle[1])):
            running = False

    window.blit(bgImg, (0,0))
    window.blit(bgImg, (288,0))
    window.blit(bgImg, (576,0))

    bird.draw(window)

    for i in range(len(obsticale)):
        obsticale[i].draw(window)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


num = 0
while num>= 0 and num<=99 :
    