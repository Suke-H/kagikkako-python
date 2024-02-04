from components.Player import Player
from components.Map import Map
from common._class.Actions import Actions

def send_action(actions: Actions, player: Player, map: Map):
    # マップ上のプレイヤーを移動
    map.move_player(actions.current_position, actions.next_position)
    map.print_player_and_object_map()

    # プレイヤーの行動を送信
    player.move(actions.next_position)
