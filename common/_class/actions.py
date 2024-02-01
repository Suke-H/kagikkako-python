class Actions:
    def __init__(self, next_player_position: list[int, int]):
        self.next_player_position = next_player_position
    
    def _print(self):
        print(f"next_player_position: {self.next_player_position}")
