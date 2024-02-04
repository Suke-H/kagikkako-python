import numpy as np
from common._class.Actions import Actions, ObjectAction, PlayerAction
from common._enum.ObjectType import ObjectType
from common._class.ObjectState import ObjectState
from components.Object import Object

from components.Goal import Goal
from components.Player import Player

import core.action_decision.push_detection as pd

def can_move(current_position: list[int, int], next_position: list[int, int], object_map: np.array, player: Player, goal: Goal) -> (bool, bool, list[ObjectAction]):
    object_state_at_next_position: ObjectState = _chack_object_state(next_position, object_map)

    nomove_player_action: PlayerAction = PlayerAction(current_position, current_position)
    move_player_action: PlayerAction = PlayerAction(current_position, next_position)
    is_goal: bool = False # ゴールに到達しているか
    object_actions: list[ObjectAction] = [] # オブジェクトの行動

    # 次の位置にオブジェクトがない場合
    if (object_state_at_next_position == None):
        return Actions(move_player_action, object_actions, is_goal) # (移動可能, オブジェクトの行動はない, ゴールに到達していない)
    
    """ 次の位置にオブジェクトがある場合 """
    # ゴールに到達しているか確認
    is_goal = goal.is_touch_with_goal_pair(player.player_state.object_type, object_state_at_next_position.object_type)
    can_push: bool = False # 押せるか

    #　次の位置にオブジェクトがあり、押せるオブジェクトの場合
    if (object_state_at_next_position.can_push):
        # マップ全体を見て、「押せる」か確認
        direction = list(np.array(next_position) - np.array(current_position))
        (can_push, object_actions) = pd.can_push(object_map, next_position, direction)
        print("can_push: ", can_push)
        print("object_actions: ", object_actions)

    # 押せる場合
    if (can_push):
        return Actions(move_player_action, object_actions, is_goal)

    # 押せない場合
    return Actions(nomove_player_action, object_actions, is_goal)

def _chack_object_state(next_position: list[int, int], object_map: np.array) -> ObjectState:
    next_object: Object = object_map[next_position[1]][next_position[0]]
    if (next_object == None):
        return None

    return next_object.object_state
