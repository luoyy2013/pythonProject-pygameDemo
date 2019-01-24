class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        # 初始化统计信息
        self.ai_settings = ai_settings
        self.game_active = False
        self.high_score = 0
        self.reset_stats()


    def reset_stats(self):
        """游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ships_limit

        # 得分
        self.score = 0
        self.level = 1



