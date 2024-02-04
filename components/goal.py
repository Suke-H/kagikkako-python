from common._enum.ObjectType import ObjectType

class Goal:
    def __init__(self, goal_object_pair: list[ObjectType, ObjectType]):
        self.goal_object_pair = goal_object_pair

    def _print(self):
        print("goal_object_pair: ", self.goal_object_pair)
        
    # def check_goal(self, object_type: ObjectType) -> bool:
    #     return object_type in self.goal_object_pair