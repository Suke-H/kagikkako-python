import numpy as np
from common._class.Actions import Actions
from common._enum.ObjectType import ObjectType
from common._class.ObjectState import ObjectState
from components.Object import Object

def chack_object(next_position: list[int, int], object_map: np.array) -> ObjectType:
    next_object: Object = object_map[next_position[0]][next_position[1]]
    if (next_object == None):
        return None

    return next_object.object_state.object_type
