import pygame
class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像接近外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #每艘飞船都放在底部
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
