import pygame
import random
class obstacle :
    def __init__(self,x):
        self.__x=x
        self.__yGap = random.randint(200,400)
        self.__imgBottom = pygame.image.load("assets/objects/pipe-green.png").convert()
        self.__imgTop = pygame.transform.rotate(self.__imgBottom,180)

    def getRect(self):
        return [self.__imgBottom.get_rect(x=self.__x, y=self.__yGap + 80),
                self.__imgTop.get_rect(x=self.__x, y=self.__yGap - 80 - 320)]

    def update(self):
        self.__x = self.__x - 5
        if self.__x<0 :
            self.__x=1670
            self.__yGap = random.randint(200, 400)

    def draw(self,window):
        window.blit(self.__imgTop, (self.__x, self.__yGap - 80 - 320))
        window.blit(self.__imgBottom, (self.__x, self.__yGap + 80))


