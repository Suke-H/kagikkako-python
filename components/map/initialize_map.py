import numpy as np    

from common._enum.ObjectType import ObjectType
from components.Object import Object
from components.Word import Word

def create_object_map(source_map: np.array) -> np.array:
        object_map = np.full_like(source_map, None, dtype=object)
        for y in range(len(source_map)):
            for x in range(len(source_map[y])):
                object_map[y][x] = convert_to_object(ObjectType(source_map[y][x]), [x, y])

        return object_map
    
def create_word_map(source_map: np.array) -> np.array:
    word_map = np.full_like(source_map, None, dtype=object)
    for y in range(len(source_map)):
        for x in range(len(source_map[y])):
            word_map[y][x] = convert_to_word(ObjectType(source_map[y][x]), [x, y])

    return word_map

def create_player_map(object_map: np.array, player_object_type: ObjectType) -> np.array:
    player_map = np.full_like(object_map, None, dtype=object)

    for y in range(len(player_map)):
        for x in range(len(player_map[y])):
            if (object_map[y][x] == None):
                continue
            if (object_map[y][x].object_state.object_type == player_object_type):
                player_map[y][x] = object_map[y][x]
                object_map[y][x] = None

    return player_map

def convert_to_object(object_type: ObjectType, position: list[int, int]) -> Object:
    if (object_type == ObjectType.NONE):
        return None
    return Object(object_type, position)

def convert_to_word(object_type: ObjectType, position: list[int, int]) -> Word:
    if (object_type == ObjectType.NONE):
        return None
    return Word(object_type, position)

