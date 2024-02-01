import numpy as np
from yaml import full_load
from common._enum.ObjectType import ObjectType
from common._class.StageData import StageData

def load_stage(path: str):

    # yamlファイルからステージ情報を読み込む
    with open(path + "data.yaml") as f:
        data = full_load(f)    
    print(data)

    player_init_position = data["player_init_position"]
    goal_object_type = ObjectType(data["goal_object_type"])

    # CSVから本マップと物語マップを作成
    bookMap = np.loadtxt(path + "book.csv", delimiter=",", dtype=int)
    storyMap = np.loadtxt(path + "story.csv", delimiter=",", dtype=int)

    # ステージデータ作成
    stageData: StageData = StageData(player_init_position, goal_object_type, bookMap, storyMap)
    stageData._print()    
