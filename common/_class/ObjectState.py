
from common._enum.ObjectType import ObjectType

class ObjectState:
    def __init__(self, object_type: ObjectType, position: list[int, int], is_player: bool, can_push: bool):
        self.object_type = object_type
        self.position = position
        self.is_player = is_player
        self.can_push = can_push

    def _print(self):
        print("ObjectState:")
        print("  object_type: ", self.object_type)