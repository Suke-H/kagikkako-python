class Actions:
    def __init__(self, current_position: list[int, int], next_position: list[int, int], is_goal: bool = False):
        self.current_position = current_position[:]
        self.next_position = next_position[:]
        self.is_goal = is_goal

    def _print(self):
        print("current_position: ", self.current_position)
        print("next_position: ", self.next_position)
