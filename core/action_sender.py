from components.Player import Player
from components.Map import Map
from common._class.Actions import Actions

def send_action(actions: Actions, player: Player, map: Map):

    # プレイヤーの行動を送信
    player.move(actions.next_player_position)
