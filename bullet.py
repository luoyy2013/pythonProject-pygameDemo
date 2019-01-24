import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射的子弹进行管理的类"""
    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # 在(0, 0)处创建一个表示子弹的矩形,再设置其正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹的位置
        self.y = float(self.rect.y)
        self.speed_factor = ai_settings.bullet_speed_factor
        self.color = ai_settings.bullet_color

    def update(self):
        """子弹的移动"""
        # 更新子弹的位置
        self.y -= self.speed_factor
        # 更新子弹的rect位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
