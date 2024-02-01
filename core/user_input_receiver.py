from common._enum.UserInput import UserInput

def respond_to_user_input():
    """
    ユーザーの入力を待つ
    """
    # ユーザーの入力を受け付ける
    user_key_input = input("Please input your move(WASD): ")
    user_key_input = user_key_input.lower()
    # 入力された文字列に応じて、UserInputの値を返す
    user_input = get_user_input(user_key_input)

    return user_input

def get_user_input(user_input: UserInput):
    """
    入力された文字列に応じて、UserInputの値を返す
    """ 

    if user_input == "w":
        return UserInput.UP
    elif user_input == "s":
        return UserInput.DOWN
    elif user_input == "a":
        return UserInput.LEFT
    elif user_input == "d":
        return UserInput.RIGHT
    else:
        return UserInput.NONE
