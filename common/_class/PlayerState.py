from common._enum.ObjectType import ObjectType

class PlayerState:
    def __init__(self, position: list[int, int], is_goal: bool, object_type: ObjectType):
        self.position = position
        self.is_goal = is_goal
        self.object_type = object_type