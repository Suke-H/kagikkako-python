import numpy as np

def print_object_map(object_map: np.array):
    print(" -- object map -- ")
    for y in range(len(object_map)):
        row = ""
        for x in range(len(object_map[y])):
            if (object_map[y][x] == None):
                row += "NONE "
            else:
                row += object_map[y][x].object_state.object_type.name + " "
        print(row)

def print_word_map(word_map: np.array):
    print(" -- word map -- ")
    for y in range(len(word_map)):
        row = ""
        for x in range(len(word_map[y])):
            if (word_map[y][x] == None):
                row += "NONE "
            else:
                row += word_map[y][x].word_state.object_type.name + " "
        print(row)

def print_player_map(player_map: np.array):
    print(" -- player map -- ")
    for y in range(len(player_map)):
        row = ""
        for x in range(len(player_map[y])):
            if (player_map[y][x] == None):
                row += "NONE "
            else:
                row += player_map[y][x].object_state.object_type.name + " "
        print(row)

def print_player_and_object_map(player_map: np.array, object_map: np.array):
    print(" -- player and object map -- ")
    for y, (players, objects) in enumerate(zip(player_map, object_map)):
        row = ""
        for x, (player, object) in enumerate(zip(players, objects)):
            if player != None and object != None:
                row += player.object_state.object_type.name + "&" + object.object_state.object_type.name + " "
            elif player != None:
                row += player.object_state.object_type.name + " "
            elif object != None:
                row += object.object_state.object_type.name + " "
            else:
                row += "NONE "
            
        print(row)