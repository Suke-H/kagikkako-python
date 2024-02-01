# GameManagerを呼び出し、ゲームを開始する

from core.GameManager import GameManager

if __name__ == '__main__':
    # ゲームマネージャーを呼び出し、ゲームを開始する
    game_manager = GameManager()
    game_manager.start_game()
    