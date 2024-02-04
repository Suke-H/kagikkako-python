from common._enum.ObjectType import ObjectType
from components.Object import Object
class PlayerState:
    def __init__(self, position: list[int, int], is_goal: bool, object_type: ObjectType, player_object: Object):
        self.position = position
        self.is_goal = is_goal
        self.object_type = object_type
        self.player_object = player_object
