from components.Player import Player
from components.Map import Map
from components.Goal import Goal
from common._class.Actions import Actions

def send_action(actions: Actions, player: Player, map: Map, goal: Goal):
    """
    決定した行動を、各コンポーネントに送信する

    Parameters
    ----------
    ( Actions, Player, Map, Goal )
        行動、プレイヤー、マップ、ゴールのインスタンス

    """
    # マップ上のプレイヤーを移動
    map.move_player(actions.player_action.current_position, actions.player_action.next_position)
    # オブジェクトを移動
    map.move_objects(actions.object_actions)
    map.print_player_and_object_map()

    # プレイヤーの行動を送信
    player.move(actions.player_action.next_position)
    # ゴール判定
    goal.update_goal(actions.is_goal)
