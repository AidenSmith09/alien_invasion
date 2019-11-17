# /bin/etc/env Python
# -*- coding: utf-8 -*-


class Settings():
    """用于存储本游戏的所有设置项"""

    def __init__(self):
        """初始化游戏设置"""
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed_factor = 1.5

        # 子弹速度
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
