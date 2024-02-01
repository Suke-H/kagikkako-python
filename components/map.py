import numpy as np

from common._enum.ObjectType import ObjectType
from components.Object import Object

class Map:
    def __init__(self, book_map: np.array, story_map: np.array):
        self.book_map = book_map
        self.story_map = story_map

        # オブジェクトマップの作成
        self.object_map = self.create_object_map(self.book_map)

    def create_object_map(self, object_map: np.array) -> np.array:
        object_map = np.full_like(self.book_map, None, dtype=object)
        for y in range(len(self.book_map)):
            for x in range(len(self.book_map[y])):
                object_map[y][x] = Map.convert_to_object(ObjectType(self.book_map[y][x]), [x, y])

        return object_map

    def convert_to_object(object_type: ObjectType, position: list[int, int]) -> Object:
        if (object_type == ObjectType.NONE):
            return None
        return Object(object_type, position)

    def _print(self):
        for y in range(len(self.object_map)):
            row = ""
            for x in range(len(self.object_map[y])):
                if (self.object_map[y][x] == None):
                    row += "NONE "
                else:
                    row += self.object_map[y][x].object_state.object_type.name + " "
            print(row)
