import numpy as np

from common._enum.ObjectType import ObjectType

class Goal:
    def __init__(self, goal_object_pair: list[ObjectType, ObjectType]):
        self.goal_object_pair = goal_object_pair
        self.is_goal = False

    def _print(self):
        print("goal_object_pair: ", self.goal_object_pair)

    def update_goal(self, is_goal: bool):
        self.is_goal = is_goal
        if self.is_goal:
            self.goal_message()

    # def detect(self, player_map: np.array, object_map: np.array):
    #     self.is_goal = self.detect_goal(player_map, object_map)
    #     if self.is_goal:
    #         self.goal_message()
        
    # def detect_goal(self, player_map: np.array, object_map: np.array) -> bool:
    #     for (players, objects) in zip(player_map, object_map):
    #         for (player, object) in zip(players, objects):
    #             if player != None and object != None:
    #                 # 組み合わせが一致したらゴール
    #                 if (self._is_pair_matched(player.object_state.object_type, object.object_state.object_type)):
    #                     return True
                    
    #     return False
    
    def is_touch_with_goal_pair(self, player_type: ObjectType, object_type: ObjectType) -> bool:
        return self._is_pair_matched(player_type, object_type)
        
    def _is_pair_matched(self, player_type: ObjectType, object_type: ObjectType) -> bool:
        if player_type == self.goal_object_pair[0] and object_type == self.goal_object_pair[1]:
            return True
        else:
            return False
    
    def goal_message(self):
        print("ゴール！")

