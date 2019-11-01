# 处理游戏函数
import sys
import pygame
from bullet import Bullet


# 监视键盘按下事件
def check_keydown(event, ai_setting, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    if event.key == pygame.K_LEFT:
        ship.move_left = True

    if event.key == pygame.K_SPACE:
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
def update_screen(ai_setting, screen, ship, bullets):
    # 重绘
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 显示最近绘制屏幕
    pygame.display.flip()


def fire_bullet(ai_setting, screen, ship, bullets):
    new_bullet = Bullet(ai_setting, screen, ship)
    bullets.add(new_bullet)


def update_bullets(bullets):
    # 删除无效子弹
    # ??为何要copy
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
