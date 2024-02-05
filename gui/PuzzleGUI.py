import pygame
from pygame.surface import Surface
import numpy as np
from PIL import Image
import yaml

from common._enum.ObjectType import ObjectType
from components.Object import Object

class PuzzleGUI:
    def __init__(self, maptile_path: str):
        self.CELL_SIZE = 128
        self.GRID_SIZE = 5 
        self.WIDTH = self.CELL_SIZE * self.GRID_SIZE
        self.HEIGHT = self.CELL_SIZE * self.GRID_SIZE

        # Pygameの初期化
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Puzzle Game")

        # マップタイルの準備
        self.maptile_table = self._prepare_images(maptile_path)

    def _prepare_images(self, maptile_path: str) -> dict[ObjectType, Surface]:
        # yaml読み込み
        with open(maptile_path + "info.yaml", "r") as f:
            maptile_info = yaml.full_load(f)

        # キー（数字）をObjectTypeに変換
        maptile_info = {ObjectType(key): value for key, value in maptile_info.items()}

        # マップタイルの準備
        maptile_table: dict[ObjectType, Surface] = {}
        for (object_type, image_name) in maptile_info.items():
            # 読み込み
            original_image = Image.open(maptile_path + image_name + ".png")
            # リサイズ
            resized_image = original_image.resize((self.CELL_SIZE, self.CELL_SIZE))
            # Surfaceに変換
            image = pygame.image.fromstring(resized_image.tobytes(), resized_image.size, resized_image.mode)

            maptile_table[object_type] = image

        return maptile_table
    
    def update_display(self, object_map: np.array, player_map: np.array):
        # 画面全体を黒色で塗りつぶす
        self.screen.fill((0, 0, 0))
        
        # パズルの各セルを描画
        for row in range(self.GRID_SIZE):
            for col in range(self.GRID_SIZE):
                x, y = col * self.CELL_SIZE, row * self.CELL_SIZE
                cell_rect = pygame.Rect(x, y, self.CELL_SIZE, self.CELL_SIZE)
                # グリッドを描画
                pygame.draw.rect(self.screen, (255, 255, 255), cell_rect, 1)  
                # オブジェクトを描画
                object: Object = object_map[row, col]
                if object != None:
                    image = self.maptile_table[object.object_state.object_type]
                    self.screen.blit(image, cell_rect)
                # プレイヤーを描画
                player: Object = player_map[row, col]
                if player != None:
                    image = self.maptile_table[player.object_state.object_type]
                    self.screen.blit(image, cell_rect)

        # 画面を更新
        pygame.display.update()
        
