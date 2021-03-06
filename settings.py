class Settings:
    """存储游戏设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.screen_title = "Alien Invasion"

        # 飞船设置
        self.ships_limit = 1

        # 子弹设置

        self.bullet_width = 3000
        self.bullet_height = 1
        self.bullet_color = (255, 60, 60)
        self.bullet_allowed = 5

        # 外星人设置
        self.fleet_drop_speed = 10

        # 游戏节奏
        self.speedup_scale = 1.1

        # 外星人点数提高的速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ 初始化随游戏进行而变化的设置 """
        self.alien_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_points = 50

        # fleet_direction表示移动方向，1向右移，-1向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """ 提高速度设置 """
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


