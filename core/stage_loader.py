import numpy as np
from yaml import full_load
from common._enum.ObjectType import ObjectType
from common._class.StageData import StageData

def load_stage(path: str):

    # yamlファイルからステージ情報を読み込む
    with open(path + "data.yaml") as f:
        data = full_load(f)    
    print(data)

    playerInitPosition = data["playerInitPosition"]
    goalObjectType = data["goalObjectType"]

    # CSVから本マップと物語マップを作成
    bookMap = np.loadtxt(path + "book.csv", delimiter=",", dtype=int)
    storyMap = np.loadtxt(path + "story.csv", delimiter=",", dtype=int)

    # ステージデータ作成
    stageData: StageData = StageData(playerInitPosition, goalObjectType, bookMap, storyMap)
    stageData._print()    
