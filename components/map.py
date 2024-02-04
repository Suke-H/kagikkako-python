import numpy as np

from common._enum.ObjectType import ObjectType
from common._class.Actions import ObjectAction
from components.Object import Object

import components.map.initialize_map as im
import components.map.print_map as pm


class Map:
    def __init__(self, book_map: np.array, story_map: np.array, player_object_type: ObjectType, can_push_table: dict[ObjectType, bool]):
        self.__book_map = book_map
        self.__story_map = story_map

        # オブジェクトマップの作成
        self.object_map = im.create_object_map(self.__story_map, can_push_table)
        # ワードマップの作成
        self.word_map = im.create_word_map(self.__book_map)
        # プレイヤーマップの初期化
        self.player_map = im.create_player_map(self.object_map, player_object_type)

    def access_object(self, position: list[int, int]) -> Object:
        return self.object_map[position[1]][position[0]]
    
    def access_player(self, position: list[int, int]) -> Object:
        return self.player_map[position[1]][position[0]]
    
    def move_objects(self, object_actions: list[ObjectAction]):
        current_positions = [object_action.current_position for object_action in object_actions]
        next_positions = [object_action.next_position for object_action in object_actions]

        # コピー
        objects = []
        for current in current_positions:
            objects.append(self.access_object(current))
        # 消去
        for current in current_positions:
            self.object_map[current[1]][current[0]] = None
        # 移動
        for (object, next) in zip(objects, next_positions):
            self.object_map[next[1]][next[0]] = object

    def move_player(self, current_position: list[int, int], next_position: list[int, int]):
        player = self.access_player(current_position)
        self.player_map[current_position[1]][current_position[0]] = None
        self.player_map[next_position[1]][next_position[0]] = player

    def transfer_player(self, current_player_position: list[int, int], next_player_position: list[int, int]):
        # 現在のPlayerオブジェクト：Playerマップ -> Objectマップ
        current_player_object = self.access_player_object(current_player_position)
        self.player_map[current_player_position[1]][current_player_position[0]] = None
        self.object_map[current_player_position[1]][current_player_position[0]] = current_player_object

        # 次のPlayerオブジェクト：Objectマップ -> Playerマップ
        next_player_object = self.access_object(next_player_position)
        self.object_map[next_player_position[1]][next_player_position[0]] = None
        self.player_map[next_player_position[1]][next_player_position[0]] = next_player_object

    def print_object_map(self):
        pm.print_object_map(self.object_map)    

    def print_word_map(self):
        pm.print_word_map(self.word_map)
    
    def print_player_map(self):
        pm.print_player_map(self.player_map)

    def print_player_and_object_map(self):
        pm.print_player_and_object_map(self.player_map, self.object_map)
