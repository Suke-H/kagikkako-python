from common._enum.UserInput import UserInput
from common._class.Actions import Actions

from components.Player import Player

def decide_action(user_input: UserInput, player: Player) -> Actions:
    # プレイヤーの次の位置を計算
    current_position = player.player_state.position
    next_position = calc_next_position(current_position, user_input)

    # 行動を決定
    action = Actions(next_position)

    return action

def calc_next_position(position: list[int, int], user_input: UserInput) -> list[int, int]:
    next_position = position.copy()

    if user_input == UserInput.UP:
        next_position[1] -= 1
    elif user_input == UserInput.DOWN:
        next_position[1] += 1
    elif user_input == UserInput.LEFT:
        next_position[0] -= 1
    elif user_input == UserInput.RIGHT:
        next_position[0] += 1
    else:
        pass

    return next_position
    