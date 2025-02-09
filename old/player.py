import pygame
pygame.init():
window = pygame.display.set_mode((800, 400))
class Player:
    def _init_(self, x, y):
        self.__x = x
        self._y = y

    def move(self, key):
        if key == pygame.KEY_LEFT:
            self.__moveLeft()
        elif key == pygame.KEY_RIGHT:
            self.__moveRight()

    def __moveRight(self):
        self.__x = self.__x + 10
        if self.__x > 1080:
            self.__x = 1080

    def __moveLeft(self):
        self.__x = self.__x - 10
        if self.__x < 0:
            self.__x = 0

    def output(self):
        window.fill((0, 0, 0))
        pygame.draw.circle(window, (117, 207, 217), (self.x, self.y), 20)
        pygame.draw.circle(window, (166, 136, 194), (300, 100), 20)
        pygame.display.flip()


class FlyingPlayer(Player):
    def _init_(self, x, y):
        super()._init_(x, y)

    def move(self, key):
        super().move(key)
        if key == pygame.KEY_UP :
            self.__moveUp()
        elif key == pygame.KEY_DOWN:
            self.__moveDown()

    def __moveUp(self):
        self._y = self._y - 10
        if self._y < 0:
            self._y = 0
    def __moveDown(self):
        self._y = self._y + 10
        if self._y > 720:
            self._y = 720