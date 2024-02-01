
from components.Player import Player
from components.Map import Map
from components.Goal import Goal

from core.stage_loader import load_stage
from core.user_input_receiver import respond_to_user_input
from core.action_decision_maker import decide_action
from core.action_sender import send_action

class GameManager:
    player: Player
    map: Map
    goal: Goal

    def start_game(self):
        (self.player, self.map, self.goal) = load_stage("stage_data/1/")
        self.game_loop()

    def game_loop(self):
        while True:
            # ユーザーの入力を受け取る
            user_input = respond_to_user_input()
            print(user_input)

            # ユーザーの入力から行動を決定する
            actions = decide_action(user_input, self.player, self.map)
            actions._print()

            # 行動を送信
            send_action(actions, self.player, self.map)