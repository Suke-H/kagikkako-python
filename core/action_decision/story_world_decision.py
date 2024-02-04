import numpy as np
from common._class.Actions import Actions
from common._enum.ObjectType import ObjectType
from common._class.ObjectState import ObjectState
from components.Object import Object

def can_move(next_position: list[int, int], object_map: np.array) -> bool:
    next_object_state: ObjectState = _chack_object_state(next_position, object_map)

    if (next_object_state == None):
        return True
    else:
        return False

def _chack_object_state(next_position: list[int, int], object_map: np.array) -> ObjectState:
    next_object: Object = object_map[next_position[1]][next_position[0]]
    if (next_object == None):
        return None

    return next_object.object_state
