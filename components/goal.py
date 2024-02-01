from common._enum.ObjectType import ObjectType

class Goal:
    def __init__(self, goal_object_type: ObjectType):
        self.goal_object_type = goal_object_type

    def _print(self):
        print("goal_object_type: ", self.goal_object_type)