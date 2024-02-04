from common._class.PlayerState import PlayerState
from common._enum.ObjectType import ObjectType
from components.Object import Object

class Player:
    def __init__(self, init_position: list[int, int], player_object: Object):
        self.player_state = PlayerState(position=init_position, is_goal=False, object_type=ObjectType.I, player_object=player_object)
        
    def transfer_player_object(self, next_object_type: ObjectType, next_player_object: Object):
        self.player_state.object_type = next_object_type
        self.player_state.player_object = next_player_object

    def move(self, next_player_position: list[int, int]):
        self.player_state.position = next_player_position

    def _print(self):
        print("position: ", self.player_state.position)
        print("is_goal: ", self.player_state.is_goal)
        print("object_type: ", self.player_state.object_type)
        print("player_object: ", self.player_state.player_object._print())
