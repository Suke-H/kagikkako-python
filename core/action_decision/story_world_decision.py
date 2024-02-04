import numpy as np
from common._class.Actions import Actions
from common._enum.ObjectType import ObjectType
from common._class.ObjectState import ObjectState
from components.Object import Object

from components.Goal import Goal
from components.Player import Player

def can_move(next_position: list[int, int], object_map: np.array, player: Player, goal: Goal) -> (bool, bool):
    object_state_at_next_position: ObjectState = _chack_object_state(next_position, object_map)

    if (object_state_at_next_position == None):
        return (True, False)
    else:
        player_type: ObjectType = player.player_state.object_type
        object_type: ObjectType = object_state_at_next_position.object_type
        is_goal = goal.is_touch_with_goal_pair(player_type, object_type)
        return (True, is_goal)

def _chack_object_state(next_position: list[int, int], object_map: np.array) -> ObjectState:
    next_object: Object = object_map[next_position[1]][next_position[0]]
    if (next_object == None):
        return None

    return next_object.object_state
