import pygame
from pygame.locals import *
import sys


def main():
    # ゲームの初期化
    pygame.init()

    # ゲーム画面のサイズ
    width, height = 800, 600

    # ゲーム画面の作成
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Simple Game")

    # プレイヤーオブジェクトの初期化
    player_size = 50
    player_x = width // 2 - player_size // 2
    player_y = height // 2 - player_size // 2
    player_speed = 5

    # メインゲームループ
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # プレイヤーの移動
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < width - player_size:
            player_x += player_speed
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= player_speed
        if keys[pygame.K_DOWN] and player_y < height - player_size:
            player_y += player_speed

        # ゲーム画面をクリア
        screen.fill((0, 0, 0))

        # プレイヤーを描画
        pygame.draw.rect(screen, (255, 0, 0), (player_x, player_y, player_size, player_size))

        # 画面を更新
        pygame.display.flip()

        # フレームレートの制御
        clock.tick(60)

    # ゲームの終了
    pygame.quit()
    sys.exit()
