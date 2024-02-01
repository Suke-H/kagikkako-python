from common._class.WordState import WordState
from common._enum.ObjectType import ObjectType

class Word:
    def __init__(self, word_type: ObjectType, position: list[int, int]):
        self.word_state = WordState(word_type, position)

    def _print(self):
        print("Word:")
        print("  word_type: ", self.word_type)
        print("  position: ", self.position)
