# /bin/etc/env Python
# -*- coding: utf-8 -*-
import pygame


class Ship():
    """初始化飞船并设置初始位置"""

    def __init__(self, ai_setings, screen):
        self.screen = screen
        self.ai_setings = ai_setings

        # 加载飞船并获取外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 飞船设置屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 飞船属性Center中存储小值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新飞船移动位置"""
        # 更新飞船的center 值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setings.ship_speed_factor

        # 根据self.center更新rect对象
        self.rect.centerx = self.center

    def blitme(self):
        """指定位置画飞船"""
        self.screen.blit(self.image, self.rect)
