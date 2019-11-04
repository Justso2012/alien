# 处理游戏函数
import sys
import pygame
from bullet import Bullet
from alien import Alien


# 监视键盘按下事件
def check_keydown(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)


# 监视键盘释放事件
def check_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    if event.key == pygame.K_LEFT:
        ship.move_left = False


# 监视鼠标、键盘事件
def check_events(ai_setting, screen, ship, bullets):
    # 监视键盘、鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


# 更新屏幕
def update_screen(ai_setting, screen, ship, bullets, aliens):
    # 重绘
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    for alien in aliens.sprites():
        alien.blitme()

    # 显示最近绘制屏幕
    pygame.display.flip()


def fire_bullet(ai_setting, screen, ship, bullets):
    new_bullet = Bullet(ai_setting, screen, ship)
    bullets.add(new_bullet)


def update_bullets(bullets):
    # 删除无效子弹
    # ??为何要copy
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))

def create_alien(ai_setting, screen, aliens, alien_number):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width
    # 间隔一个空间
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    aliens.add(alien)


# 创建外星人s
def create_fleet(ai_setting, screen, aliens):
    alien = Alien(ai_setting, screen)
    alien_width = alien.rect.width

    # 计算可容纳外星人数量
    avaliable_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width))

    for alien_number in range(number_aliens_x):
        create_alien(ai_setting, screen, aliens, alien_number)
