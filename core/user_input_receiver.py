import pygame

from common._enum.UserInput import UserInput

def respond_to_user_input() -> UserInput:
    """
    ユーザーの入力を待つ
    """


    # ユーザーの入力を受け付ける
    # user_key_input = input("Please input your move(WASD): ")
    # user_key_input = user_key_input.lower()
    # 入力された文字列に応じて、UserInputの値を返す
    # user_input = get_user_input(user_key_input)

    # ユーザーの入力を受け付ける
    keys = pygame.key.get_pressed()
    user_input = get_user_input(keys)

    return user_input

def get_user_input(keys) -> UserInput:
    """
    入力された文字列に応じて、UserInputの値を返す
    """ 

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        return UserInput.UP
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        return UserInput.DOWN
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        return UserInput.LEFT
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        return UserInput.RIGHT
    else:
        return UserInput.NONE

# def get_user_input(user_input: UserInput) -> UserInput:
#     """
#     入力された文字列に応じて、UserInputの値を返す
#     """ 

#     if user_input == "w":
#         return UserInput.UP
#     elif user_input == "s":
#         return UserInput.DOWN
#     elif user_input == "a":
#         return UserInput.LEFT
#     elif user_input == "d":
#         return UserInput.RIGHT
#     else:
#         return UserInput.NONE
