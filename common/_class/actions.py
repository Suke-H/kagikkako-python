class PlayerAction:
    def __init__(self, current_position: list[int, int], next_position: list[int, int]):
        self.current_position = current_position[:]
        self.next_position = next_position[:]

class ObjectAction:
    def __init__(self, current_position: list[int, int], next_position: list[int, int]):
        self.current_position = current_position[:]
        self.next_position = next_position[:]

class Actions:
    def __init__(self, player_action: PlayerAction, object_actions: list[ObjectAction], is_goal: bool):
        self.player_action = player_action
        print("player_action: ", self.player_action)
        self.object_actions = object_actions[:]
        self.is_goal = is_goal

    def _print(self):
        print("current_position: ", self.player_action.current_position)
        print("next_position: ", self.player_action.next_position)