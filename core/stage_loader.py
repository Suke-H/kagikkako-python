import numpy as np
from yaml import full_load

from common._enum.ObjectType import ObjectType
from common._class.StageData import StageData

from components.Player import Player
from components.Map import Map
from components.Goal import Goal
from components.Object import Object

def load_stage(path: str) -> (Player, Map, Goal):

    # yamlファイルからステージ情報を読み込む
    with open(path + "data.yaml") as f:
        data = full_load(f)    

    player_init_position: list[int, int] = data["player_init_position"]
    pair = data["goal_object_pair"]
    goal_object_pair: list[ObjectType, ObjectType] = [ObjectType(pair[0]), ObjectType(pair[1])]

    # CSVから本マップと物語マップを作成
    bookMap = np.loadtxt(path + "book.csv", delimiter=",", dtype=int)
    storyMap = np.loadtxt(path + "story.csv", delimiter=",", dtype=int)

    # ステージデータ作成
    stageData = StageData(player_init_position, goal_object_pair, bookMap, storyMap)
    # stageData._print()    

    # マップ作成
    map = Map(stageData.bookMap, stageData.storyMap)
    map.print_object_map()
    map.print_word_map()

    # プレイヤー作成
    player_object = map.access_object(player_init_position)
    player = Player(stageData.player_init_position, player_object)
    player._print()

    # ゴール作成
    goal = Goal(stageData.goal_object_pair)
    goal._print()

    return (player, map, goal)

    
