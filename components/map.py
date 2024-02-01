import numpy as np

from common._enum.ObjectType import ObjectType
from components.Object import Object
from components.Word import Word


class Map:
    def __init__(self, book_map: np.array, story_map: np.array):
        self.book_map = book_map
        self.story_map = story_map

        # オブジェクトマップの作成
        self.object_map = self.create_object_map(self.book_map)
        # ワードマップの作成
        self.word_map = self.create_word_map(self.story_map)

    def create_object_map(self, object_map: np.array) -> np.array:
        object_map = np.full_like(self.book_map, None, dtype=object)
        for y in range(len(self.book_map)):
            for x in range(len(self.book_map[y])):
                object_map[y][x] = Map.convert_to_object(ObjectType(self.book_map[y][x]), [x, y])

        return object_map
    
    def create_word_map(self, word_map: np.array) -> np.array:
        word_map = np.full_like(self.story_map, None, dtype=object)
        for y in range(len(self.story_map)):
            for x in range(len(self.story_map[y])):
                word_map[y][x] = Map.convert_to_word(ObjectType(self.story_map[y][x]), [x, y])

        return word_map

    def convert_to_object(object_type: ObjectType, position: list[int, int]) -> Object:
        if (object_type == ObjectType.NONE):
            return None
        return Object(object_type, position)
    
    def convert_to_word(object_type: ObjectType, position: list[int, int]) -> Word:
        if (object_type == ObjectType.NONE):
            return None
        return Word(object_type, position)

    def _print(self):
        print(" -- object map -- ")
        for y in range(len(self.object_map)):
            row = ""
            for x in range(len(self.object_map[y])):
                if (self.object_map[y][x] == None):
                    row += "NONE "
                else:
                    row += self.object_map[y][x].object_state.object_type.name + " "
            print(row)

        print(" -- word map -- ")
        for y in range(len(self.word_map)):
            row = ""
            for x in range(len(self.word_map[y])):
                if (self.word_map[y][x] == None):
                    row += "NONE "
                else:
                    row += self.word_map[y][x].word_state.object_type.name + " "
            print(row)
