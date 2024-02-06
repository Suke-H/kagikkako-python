import pygame
import sys

from components.Player import Player
from components.Map import Map
from components.Goal import Goal
from common._enum.ObjectType import ObjectType
from common._enum.UserInput import UserInput
from core.stage_loader import load_stage, load_can_push_table
from core.user_input_receiver import respond_to_user_input
from core.action_decision_maker import decide_action
from core.action_sender import send_action
from gui.PuzzleGUI import PuzzleGUI

class GameManager:
    player: Player
    map: Map
    goal: Goal
    puzzleGUI: PuzzleGUI

    def start_game(self):
        """
        ゲームを開始する
        """
        # ステージの読み込み
        (self.player, self.map, self.goal) = load_stage("stage_data/")
        # GUIの初期化
        self.puzzleGUI = PuzzleGUI("stage_data/maptile/")
        # ゲームループの開始
        self.game_loop()

    def game_loop(self):
        """
        ゲームループ

        1. respond_to_user_input: ユーザーの入力を受け取る
        2. decide_action: ユーザーの入力から行動を決定する
        3. send_action: 行動を送信

        """
        # パズルの表示を更新
        self.puzzleGUI.update_display(self.map.object_map, self.map.player_map)
        # クロックの初期化
        clock = pygame.time.Clock()
        last_time = 0
        move_cooldown = 200
        # ループ開始
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # フレームレートの制御
            clock.tick(60)

            # ユーザーの入力を受け取る
            current_time = pygame.time.get_ticks()
            user_input = respond_to_user_input()
            if user_input == UserInput.NONE or current_time - last_time < move_cooldown:
                continue
            last_time = current_time

            # ユーザーの入力から行動を決定する
            actions = decide_action(user_input, self.map, self.player, self.goal)
            actions._print()

            # 行動を送信
            send_action(actions, self.player, self.map, self.goal)

            # パズルの表示を更新
            self.puzzleGUI.update_display(self.map.object_map, self.map.player_map)

            # ゴール判定
            if self.goal.is_goal:
                pygame.time.wait(2000)
                break
            