import numpy as np
from common._enum.ObjectType import ObjectType
from common._class.StageData import StageData

def load_stage():
    playerInitPosition = [1, 1]
    goalObjectType = ObjectType.I
    bookMap = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 1, 1, 1, 1, 1, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    storyMap = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 3, 4, 4, 4, 4, 4, 3, 0],
        [0, 3, 4, 4, 4, 4, 4, 3, 0],
        [0, 3, 4, 4, 4, 4, 4, 3, 0],
        [0, 3, 4, 4, 4, 4, 4, 3, 0],
        [0, 3, 4, 4, 4, 4, 4, 3, 0],
        [0, 3, 3, 3, 3, 3, 3, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    # ステージデータ作成
    stageData: StageData = StageData(playerInitPosition, goalObjectType, bookMap, storyMap)
    stageData._print()    
