import numpy as np

from common._class.Actions import Actions
from components.Map import Map

from core.action_decision.book_world_decision import transfer_to_object
from core.action_decision.story_world_decision import chack_object


def decide_to_move(current_position: list[int, int], next_position: list[int, int], map: Map) -> Actions:

    # マップの外に出ようとしている場合は移動しない
    if not is_inside_map(next_position, map.word_map):
        return Actions(current_position)

    # 本の文字を踏んだか判定
    next_word_state = transfer_to_object(next_position, map.word_map)

    # 踏んだ場合の処理
    # ...

    # オブジェクトがあるか判定
    next_object_state = chack_object(next_position, map.object_map)

    # オブジェクトがある場合の処理
    # ...

    # 何もない場合は移動する
    return Actions(next_position)
    

def is_inside_map(next_position: list[int, int], map: np.array) -> bool:
    x , y = next_position[0], next_position[1]
    if ( x >= 0 and x < len(map) ) and ( y >= 0 and y < len(map[0]) ):
        return True
    else:
        return False