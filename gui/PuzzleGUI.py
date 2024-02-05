import pygame
import numpy as np
from PIL import Image

class PuzzleGUI:
    def __init__(self):
        # self.CELL_SIZE = 256
        self.CELL_SIZE = 128
        self.GRID_SIZE = 5 
        self.WIDTH = self.CELL_SIZE * self.GRID_SIZE
        self.HEIGHT = self.CELL_SIZE * self.GRID_SIZE

        # Pygameの初期化
        pygame.init()
        screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Puzzle Game")

        # パズルの初期化
        puzzle_array = np.random.randint(0, 2, size=(self.GRID_SIZE, self.GRID_SIZE))  # 仮の初期化

        # 画像の読み込み
        # image = pygame.image.load("stage_data/maptile/box.png")
        original_image = Image.open("stage_data/maptile/box.png")
        # 新しいサイズにリサイズ
        resized_image = original_image.resize((self.CELL_SIZE, self.CELL_SIZE))
        image = pygame.image.fromstring(resized_image.tobytes(), resized_image.size, resized_image.mode)


        # パズルの各セルを描画
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                x, y = col * self.CELL_SIZE, row * self.CELL_SIZE
                cell_rect = pygame.Rect(x, y, self.CELL_SIZE, self.CELL_SIZE)

                # numpyの要素に基づいて画像を描画
                if puzzle_array[row, col] == 1:
                    screen.blit(image, cell_rect)

                pygame.draw.rect(screen, (255, 255, 255), cell_rect, 1)  # グリッドを描画

        # 画面を更新
        pygame.display.flip()
        

