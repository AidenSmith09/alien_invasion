# /bin/etc/env Python
# -*- coding: utf-8 -*-

import sys
import pygame

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen,ship):
    """每次循环重新绘制屏幕"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 让最新的屏幕可见。
    pygame.display.flip()  # 绘制一个空屏幕，并擦去旧屏幕。可以理解为刷新屏幕。