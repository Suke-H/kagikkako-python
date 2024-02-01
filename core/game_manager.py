from core.stage_loader import load_stage
from core.user_input_receiver import respond_to_user_input

def start_game():
    load_stage("stage_data/1/")
    game_loop()

def game_loop():
    while True:
        user_input = respond_to_user_input()
        print(user_input)
