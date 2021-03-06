import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button


def run_game():
    # 创建游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.screen_title)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    stats = GameStats(ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建得分面板
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "play")

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets, play_button, stats, aliens)

        if stats.game_active:
            ship.update()
            gf.update_bullets(bullets, aliens, ai_settings, screen, ship, stats, sb)
            gf.update_aliens(ai_settings, stats, screen, aliens, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, play_button, stats, sb)


run_game()
