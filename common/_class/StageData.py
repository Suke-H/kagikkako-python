import numpy as np
from common._enum.ObjectType import ObjectType

class StageData:
    """
    ステージ情報の形式

    Attributes
    ----------
    player_init_position : list[int, int]
        プレイヤーの初期位置
    goal_object_pair : list[ObjectType, ObjectType]
        ゴール条件となっているオブジェクトペア
    bookMap : np.array
        本のマップ（文字を配置）
    storyMap : np.array
        ストーリーのマップ（オブジェクトを配置）
    
    """
    def __init__(self, player_init_position: list[int, int], goal_object_pair: list[ObjectType, ObjectType], bookMap: np.array, storyMap: np.array):
        self.player_init_position = player_init_position
        self.goal_object_pair = goal_object_pair
        self.bookMap = bookMap
        self.storyMap = storyMap

    def _print(self):
        print("player_init_position: ", self.player_init_position)
        print("goal_object_type: ", self.goal_object_type)
        print("bookMap: ", self.bookMap)
        print("storyMap: ", self.storyMap)
