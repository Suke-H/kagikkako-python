import numpy as np
from common._enum.ObjectType import ObjectType

class StageData:
    def __init__(self, playerInitPosition: list[int, int], goalObjectType: ObjectType, bookMap: np.array, storyMap: np.array):
        self.playerInitPosition = playerInitPosition
        self.goalObjectType = goalObjectType
        self.bookMap = bookMap
        self.storyMap = storyMap

    def _print(self):
        print("playerInitPosition: ", self.playerInitPosition)
        print("goalObjectType: ", self.goalObjectType)
        print("bookMap: ", self.bookMap)
        print("storyMap: ", self.storyMap)
