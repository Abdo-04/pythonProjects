import pygame
class Bird:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__direction = 5
        self.__img = pygame.image.load("assets/Objects/yellowbird-upflap.png").convert()
        self.__count=0

    def getRect(self):
        return self.__img.get_rect(x=self.__x, y=self.__y)
    def up(self):
        self.__direction = -5
        self.__count= 0

    def update(self):
        self.__y= self.__y + self.__direction
        self.__count = self.__count + 1
        if self.__count > 30:
           self.__direction = 5
        if self.__y <0 or self.__y>512:
            return False
        else:
            return True

    def draw(self,window):
        window.blit(self.__img,(self.__x,self.__y))
