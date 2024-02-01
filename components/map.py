import numpy as np

class Map:
    def __init__(self, bookMap: np.array, storyMap: np.array):
        self.bookMap = bookMap
        self.storyMap = storyMap

    def _print(self):
        print("bookMap: ", self.bookMap)
        print("storyMap: ", self.storyMap)
        