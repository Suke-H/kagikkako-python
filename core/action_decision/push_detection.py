import numpy as np

from common._class.Actions import ObjectAction
from components.Object import Object

def can_push(object_map: np.array, current_position: list[int, int], direction: list[int, int]) -> (bool, list[ObjectAction]):
    object_actions: list[ObjectAction] = []
    next_position = list(np.array(current_position) + np.array(direction))

    while True:
        # マップの外に出る場合は「押せない」
        if (next_position[0] < 0 or next_position[0] >= len(object_map[0])) or (next_position[1] < 0 or next_position[1] >= len(object_map)):
            return (False, [])
        # 次のマスにオブジェクトがある場合
        if (object_map[next_position[1]][next_position[0]] != None):
            next_object: Object = object_map[next_position[1]][next_position[0]]
            # そのオブジェクトが動かせない場合、「押せない」
            if (not next_object.object_state.can_push):
                return (False, [])
            # そのオブジェクトが動かせる場合、もう一度判定を行う
            else:
                object_actions.append(ObjectAction(current_position, next_position))
                push_object = next_object
                current_position = next_position[:]
                next_position = list(np.array(next_position) + np.array(direction))
        # 次のマスにオブジェクトがない場合、「押せる」
        else:
            object_actions.append(ObjectAction(current_position, next_position))
            return (True, object_actions)


