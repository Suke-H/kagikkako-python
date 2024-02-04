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
    with open(path + "1/data.yaml") as f:
        data = full_load(f)    

    player_init_position: list[int, int] = data["player_init_position"]
    pair = data["goal_object_pair"]
    goal_object_pair: list[ObjectType, ObjectType] = [ObjectType(pair[0]), ObjectType(pair[1])]

    # CSVから本マップと物語マップを作成
    bookMap = np.loadtxt(path + "1/book.csv", delimiter=",", dtype=int)
    storyMap = np.loadtxt(path + "1/story.csv", delimiter=",", dtype=int)

    # ステージデータ作成
    stageData = StageData(player_init_position, goal_object_pair, bookMap, storyMap)
    # stageData._print()    

    # can push表を読み込む
    can_push_table = load_can_push_table(path)

    # マップ作成
    map = Map(stageData.bookMap, stageData.storyMap, ObjectType.I, can_push_table)
    map.print_object_map()
    map.print_word_map()
    map.print_player_map()

    # プレイヤー作成
    player_object = map.access_player(player_init_position)
    player = Player(stageData.player_init_position, player_object)
    # player._print()

    # ゴール作成
    goal = Goal(stageData.goal_object_pair)
    goal._print()

    return (player, map, goal)

def load_can_push_table(path: str) -> dict[ObjectType, bool]:
    with open(path + "can_push.yaml") as f:
        data = full_load(f)

    # キー（文字列）をObjectTypeに変換
    table = {ObjectType(key): value for key, value in data.items()}
    return table
    