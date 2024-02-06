import numpy as np

from common._enum.ObjectType import ObjectType

class Goal:
    """
    ゴール

    Attributes
    ----------
    goal_object_pair : list[ObjectType, ObjectType]
        ゴール条件となっているオブジェクトペア
    is_goal : bool
        ゴールしたかどうか
    """
    def __init__(self, goal_object_pair: list[ObjectType, ObjectType]):
        self.goal_object_pair = goal_object_pair
        self.is_goal = False

    def _print(self):
        print("goal_object_pair: ", self.goal_object_pair)

    def update_goal(self, is_goal: bool):
        """
        ゴールの状態を更新する
        """
        self.is_goal = is_goal
        if self.is_goal:
            self.goal_message()

    def is_touch_with_goal_pair(self, player_type: ObjectType, object_type: ObjectType) -> bool:
        """
        ゴールペア同士が接触したかを判定
        """
        return self._is_pair_matched(player_type, object_type)
        
    def _is_pair_matched(self, player_type: ObjectType, object_type: ObjectType) -> bool:
        if player_type == self.goal_object_pair[0] and object_type == self.goal_object_pair[1]:
            return True
        else:
            return False
    
    def goal_message(self):
        print("ゴール！")

