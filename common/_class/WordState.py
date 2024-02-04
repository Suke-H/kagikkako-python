# ObjectType
from common._enum.ObjectType import ObjectType

class WordState:
    def __init__(self, word_type: ObjectType, position: list[int, int], is_player: bool):
        self.word_type = word_type
        self.position = position
        self.is_player = is_player

    def _print(self):
        print("WordState:")
        print("  word_type: ", self.word_type)
        print("  position: ", self.position)

