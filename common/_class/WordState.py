# ObjectType
from common._enum.ObjectType import ObjectType

class WordState:
    def __init__(self, object_type: ObjectType, position: list[int, int]):
        self.object_type = object_type
        self.position = position

    def _print(self):
        print("WordState:")
        print("  word_type: ", self.word_type)
        print("  position: ", self.position)

