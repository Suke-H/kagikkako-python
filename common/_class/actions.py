class PlayerAction:
    """
    プレイヤーの行動

    Attributes
    ----------
    current_position : list[int, int]
        現在位置
    next_position : list[int, int]
        次の位置
    
    """
    def __init__(self, current_position: list[int, int], next_position: list[int, int]):
        self.current_position = current_position[:]
        self.next_position = next_position[:]

class ObjectAction:
    """
    オブジェクトの行動

    Attributes
    ----------
    current_position : list[int, int]
        現在位置
    next_position : list[int, int]
        次の位置
    
    """
    def __init__(self, current_position: list[int, int], next_position: list[int, int]):
        self.current_position = current_position[:]
        self.next_position = next_position[:]

class Actions:
    """
    ゲーム環境内の各コンポーネント（プレイヤー、オブジェクト、ゴール）に与える行動

    Attributes
    ----------
    player_action : PlayerAction
        プレイヤーの行動
    object_actions : list[ObjectAction]
        オブジェクトの行動
    is_goal : bool
        ゴールかどうか
    
    """
    def __init__(self, player_action: PlayerAction, object_actions: list[ObjectAction], is_goal: bool):
        self.player_action = player_action
        self.object_actions = object_actions[:]
        self.is_goal = is_goal

    def _print(self):
        print("current_position: ", self.player_action.current_position)
        print("next_position: ", self.player_action.next_position)