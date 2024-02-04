import numpy as np

from common._enum.ObjectType import ObjectType
from components.Object import Object
from components.Word import Word

class Map:
    def __init__(self, book_map: np.array, story_map: np.array):
        self.__book_map = book_map
        self.__story_map = story_map

        # オブジェクトマップの作成
        self.object_map = self.create_object_map(self.__book_map)
        # ワードマップの作成
        self.word_map = self.create_word_map(self.__story_map)

    def access_player_object(self, position: list[int, int]) -> Object:
        return self.object_map[position[1]][position[0]][0]
    
    def move_object(self, current_position: list[int, int], next_position: list[int, int]):
        object = self.access_object(current_position)
        self.object_map[current_position[1]][current_position[0]] = []
        self.object_map[next_position[1]][next_position[0]].append(object)

    def create_object_map(self, object_map: np.array) -> np.array:
        object_map = np.full_like(self.__book_map, None, dtype=object)
        for y in range(len(self.__book_map)):
            for x in range(len(self.__book_map[y])):
                object_map[y][x] = Map.convert_to_object(ObjectType(self.__book_map[y][x]), [x, y])

        return object_map
    
    def create_word_map(self, word_map: np.array) -> np.array:
        word_map = np.full_like(self.__story_map, None, dtype=object)
        for y in range(len(self.__story_map)):
            for x in range(len(self.__story_map[y])):
                word_map[y][x] = Map.convert_to_word(ObjectType(self.__story_map[y][x]), [x, y])

        return word_map

    def convert_to_object(object_type: ObjectType, position: list[int, int]) -> list:
        if (object_type == ObjectType.NONE):
            return []
        return [Object(object_type, position)]
    
    def convert_to_word(object_type: ObjectType, position: list[int, int]) -> Word:
        if (object_type == ObjectType.NONE):
            return []
        return [Word(object_type, position)]

    def print_object_map(self):
        print(" -- word map -- ")
        for y in range(len(self.object_map)):
            row = ""
            for x in range(len(self.object_map[y])):
                if len(self.object_map[y][x]) == 0:
                    row += "NONE "
                    continue
                mass = "["
                for i in range(len(self.object_map[y][x])):
                    row += self.object_map[y][x][i].object_state.object_type.name + ","
                mass += "] "
                row += mass

    def print_word_map(self):
        print(" -- word map -- ")
        for y in range(len(self.word_map)):
            row = ""
            for x in range(len(self.word_map[y])):
                mass = "["
                if len(self.word_map[y][x]) != 0:
                    for i in range(len(self.word_map[y][x])):
                        mass += self.word_map[y][x][i].word_state.word_type.name + ","
                mass += "] "
                row += mass
                # if (self.word_map[y][x] == None):
                #     row += "NONE "
                # else:
                #     row += self.word_map[y][x].word_state.object_type.name + " "

            print(row)
