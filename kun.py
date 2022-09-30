import pygame


class Kun(pygame.sprite.Sprite):
    '''坤坤'''

    def __init__(self, image0, image1, position, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image0 = pygame.transform.scale(image0, (101, 103))
        self.image1 = pygame.transform.scale(image1, (101, 103))
        self.image = self.image0
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.setPosition(position)
        self.is_hammer = False

    def setPosition(self, pos):
        '''设置位置'''
        self.rect.left, self.rect.top = pos

    def setBeHammered(self):
        '''设置被击中'''
        self.is_hammer = True

    def draw(self, screen):
        '''显示在屏幕上'''
        if self.is_hammer:
            self.image = self.image1
        screen.blit(self.image, self.rect)

    def reset(self):
        '''重置'''
        self.image = self.image0
        self.is_hammer = False
