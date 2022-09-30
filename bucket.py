import pygame


class Bucket(pygame.sprite.Sprite):
    '''锤子类'''

    def __init__(self, image0, image1, position):
        pygame.sprite.Sprite.__init__(self)
        self.image0 = image0
        self.image1 = image1
        self.image = self.image0
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image1)
        self.rect.left, self.rect.top = position
        # 用于显示锤击时的特效
        self.hammer_count = 0
        self.hammer_last_time = 4
        self.is_hammering = False

    def setPosition(self, pos):
        '''设置位置'''
        self.rect.centerx, self.rect.centery = pos

    def setHammering(self):
        '''设置hammering'''
        self.is_hammering = True

    def draw(self, screen):
        '''显示在屏幕上'''
        if self.is_hammering:
            self.image = self.image1
            self.hammer_count += 1
            if self.hammer_count > self.hammer_last_time:
                self.is_hammering = False
                self.hammer_count = 0
        else:
            self.image = self.image0
        screen.blit(self.image, self.rect)
