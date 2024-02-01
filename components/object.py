from common._class.ObjectState import ObjectState
from common._enum.ObjectType import ObjectType

class Object:
    def __init__(self, object_type: ObjectType, position: list[int, int]):
        self.object_state = ObjectState(object_type, position, False)        

    def _print(self):
        print("object_state: ", self.object_state.object_type)
