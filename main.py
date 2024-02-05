# GameManagerを呼び出し、ゲームを開始する

from core.GameManager import GameManager
from core.gm import main

if __name__ == '__main__':
    # ゲームを開始する
    game_manager = GameManager()
    game_manager.start_game()

    # main()
    