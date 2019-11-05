import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_setting, screen)

    # make  group
    bullets = Group()
    aliens = Group()

    stats = GameStats(ai_setting)

    # make a play button
    play_button = Button(ai_setting, screen, "Play")

    while True:
        gf.check_events(ai_setting, screen, ship, bullets, stats, play_button)
        print("active:", stats.game_active)

        ship.update()
        bullets.update()
        aliens.update()
        gf.create_fleet(ai_setting, screen, aliens)
        gf.update_screen(ai_setting, screen, ship, bullets, aliens, stats, play_button)

        gf.update_bullets(bullets)


if __name__ == '__main__':
    run_game()
