from components.Player import Player
from components.Map import Map
from components.Goal import Goal
from common._class.Actions import Actions

def send_action(actions: Actions, player: Player, map: Map, goal: Goal):
    # マップ上のプレイヤーを移動
    map.move_player(actions.current_position, actions.next_position)
    map.print_player_and_object_map()

    # プレイヤーの行動を送信
    player.move(actions.next_position)

    # ゴール判定
    goal.update_goal(actions.is_goal)
