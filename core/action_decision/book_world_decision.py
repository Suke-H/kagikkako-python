import numpy as np
from common._class.Actions import Actions
from common._enum.ObjectType import ObjectType
from components.Word import Word

def transfer_to_object(next_position: list[int, int], word_map: np.array) -> ObjectType:
    next_word: Word = word_map[next_position[0]][next_position[1]]

    if (next_word == None):
        return None

    return next_word.word_state.object_type