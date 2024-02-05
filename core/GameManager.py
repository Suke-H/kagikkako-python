
from components.Player import Player
from components.Map import Map
from components.Goal import Goal

from common._enum.ObjectType import ObjectType

from core.stage_loader import load_stage, load_can_push_table
from core.user_input_receiver import respond_to_user_input
from core.action_decision_maker import decide_action
from core.action_sender import send_action

from gui.PuzzleGUI import PuzzleGUI

class GameManager:
    player: Player
    map: Map
    goal: Goal

    def start_game(self):
        (self.player, self.map, self.goal) = load_stage("stage_data/")

        PuzzleGUI()
        
        self.game_loop()

    def game_loop(self):
        while True:
            # ユーザーの入力を受け取る
            user_input = respond_to_user_input()
            print(user_input)

            # ユーザーの入力から行動を決定する
            actions = decide_action(user_input, self.map, self.player, self.goal)
            actions._print()

            # 行動を送信
            send_action(actions, self.player, self.map, self.goal)

            # ゴール判定
            if self.goal.is_goal:
                break