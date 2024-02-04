class Actions:
    def __init__(self, current_position: list[int, int], next_position: list[int, int]):
        self.current_position = current_position[:]
        self.next_position = next_position[:]

    def _print(self):
        print("current_position: ", self.current_position)
        print("next_position: ", self.next_position)
