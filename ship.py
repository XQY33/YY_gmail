import pygame
from settings import Settings

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings    #注意此处   别忘记创建ship的传入的ai_game对象的seetings的实例化对象   ...

        #加载飞船图像接近外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #每艘飞船都放在底部
        self.rect.midbottom = self.screen_rect.midbottom
        #飞船属性x中存储一个浮点数
        self.x = float(self.rect.x)

        #移动标志位
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志位调整飞船位置"""
        if self.moving_right and self.rect.right <self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x-= self.settings.ship_speed
        #更新对象  此处x坐标才是的对象左右移动的位置的实例化
        self.rect.x=self.x



    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image, self.rect)
