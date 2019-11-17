# /bin/etc/env Python3
# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_fuctions as gf



def run_game():
    """初始化游戏并创建一个窗口对象"""
    pygame.init()  # 初始化背景
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_height,
         ai_settings.screen_width))  # 创建一个显示窗口，使用实参创建一个窗口。
    pygame.display.set_caption("Alien Invasion")

    #设置北京颜色
    bg_color = (230,230,230)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    while True:  # 使用while循环来循环一个事件
        # 监听键盘鼠标事件
        # for event in pygame.event.get(
        # ):  # for循环做事件的循环。pygame.event.get()所有键盘鼠标事件豆浆促使for循环运行。
        #     if event.type == pygame.QUIT:  # 在for循环中，判断如果发生窗口关闭事件，则调用sys.exit()来退出游戏。
        #         sys.exit()  # 退出时，使用sys模块退出。
        gf.check_events(ai_settings, screen, ship, bullets)

        ship.update()

        gf.update_bullets(bullets)


        # 每次循环重新绘制屏幕ÒÒ
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # # 让最新的屏幕可见。
        # pygame.display.flip()  # 绘制一个空屏幕，并擦去旧屏幕。可以理解为刷新屏幕。
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
