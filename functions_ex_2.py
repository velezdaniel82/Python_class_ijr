import random

player_name = input("Type your name: ")

score = 0

def player_selection():
    player_selection_v = input(f'''Type your pick "piedra", "papel", or "tijera": ''')
    return player_selection_v

def machine_selection():
    list_1 = ["piedra", "papel", "tijera"]
    machine_selection_v = list_1[random.randint(0, len(list_1)-1)]
    return machine_selection_v

def compare(player_selection_v, machine_selection_v):
    
    global score

    if player_selection_v == machine_selection_v:
        print(f''' Tú elegiste {player_selection_v}, y la máquina eligió {machine_selection_v}, entonces el resultado es un empate''')
        repeat_game = input("Would you like to play again? (y/n): ")
        if repeat_game == "y":
            compare(player_selection(), machine_selection())
        else: 
            result(score)
    
    elif (player_selection_v == "piedra" and machine_selection_v == "tijera") or (player_selection_v == "tijera" and machine_selection_v == "papel") or (player_selection_v == "papel" and machine_selection_v == "piedra"):
        print(f''' Tú elegiste {player_selection_v}, y la máquina eligió {machine_selection_v}, entonces ganaste''')
        score += 1
        repeat_game = input("Would you like to play again? (y/n): ")
        if repeat_game == "y":
            compare(player_selection(), machine_selection())
        else: 
            result(score)
    
    elif (player_selection_v == "piedra" and machine_selection_v == "papel") or (player_selection_v == "tijera" and machine_selection_v == "piedra") or (player_selection_v == "papel" and machine_selection_v == "tijera"):
        print(f''' Tú elegiste {player_selection_v}, y la máquina eligió {machine_selection_v}, entonces perdiste''')
        repeat_game = input("Would you like to play again? (y/n): ")
        if repeat_game == "y":
            compare(player_selection(), machine_selection())
        else: 
            result(score)

def result(score):
   result_v = print(f'''{player_name}, ¡thanks for playing! Your final score was {score} points''')
   return result_v

compare(player_selection(), machine_selection())