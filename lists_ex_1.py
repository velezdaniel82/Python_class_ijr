import random
list_1 = ["piedra", "papel", "tijera"]
player_option = input(f'''Type your pick "piedra", "papel", or "tijera": ''')
machine_option = list_1[random.randint(0, len(list_1)-1)]

if player_option == machine_option:
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces el resultado es un empate''')

elif player_option == "piedra" and machine_option == "tijera":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces ganaste''')

elif player_option == "piedra" and machine_option == "papel":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces perdiste''')

elif player_option == "tijera" and machine_option == "piedra":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces perdiste''')

elif player_option == "tijera" and machine_option == "papel":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces ganaste''')

elif player_option == "papel" and machine_option == "tijera":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces perdiste''')

elif player_option == "papel" and machine_option == "piedra":
    print(f''' Tú elegiste {player_option}, y la máquina eligió {machine_option}, entonces perdiste''')