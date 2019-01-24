import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 设置飞船图形及其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部中心
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动标志位
        self.moving_right = False
        self.moving_left = False

        # 在飞船的center属性中存储小数
        self.center = float(self.rect.centerx)

    def update(self):
        """根据标志调整飞船的位置"""

        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.center

    def blitme(self):
        # 在制定位置绘制飞船
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """ 让飞船在屏幕上居中 """
        self.center = self.screen_rect.centerx
