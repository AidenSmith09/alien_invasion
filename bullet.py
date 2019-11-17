# /bin/etc/env Python
# -*- coding: utf-8 -*-
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """对飞船发射的子弹进行管理"""

    def __init__(self, ai_settings, screen, ship):
        """在飞船所处位置创建一个子弹对象"""
        super(Bullet, self).__init__()  # Python2.7语法，也被适用于Python3
        self.screen = screen

        # 在0，0处创建一个子弹的矩形，再设置正确的位置
        # 子弹不基于图像，所以必须使用Pygame.Rect()方法创建一个矩形。

        self.rect = pygame.Rect(
            0,
            0,
            ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # 将子弹的的centerx设置为飞创的rect.centerx
        self.rect.top = ship.rect.top  # 子弹的top值设置为飞船的rect的top值，让子弹看起来相从飞船中射出。

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)  # 使用Y坐标存储小数，子弹速度做微调。

        self.color = ai_settings.bullet_color  # 子弹颜色
        self.speed_factor = ai_settings.bullet_speed_factor  # 子弹速度


    def update(self):
        """向上移动的子弹"""
        self.y -= self.speed_factor # 子弹向上移动，意味则子弹与上壁的值不断减少。所以从 self.y 减去 self.speed_factor的值
        self.rect.y = self.y

    def draw_bullet(self):
        """屏幕上填绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
