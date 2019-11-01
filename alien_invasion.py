import pygame
from settings import Settings
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():
    # 初始化
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # make a ship
    ship = Ship(ai_setting, screen)

    # make bullet group
    bullets = Group()

    while True:
        gf.check_events(ai_setting, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_setting, screen, ship, bullets)

        gf.update_bullets(bullets)

if __name__ == '__main__':
    run_game()
