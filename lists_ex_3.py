import random
inicio = input(f'''Si desea iniciar el juego, digite la palabra ""Apuesta": ''')

if inicio == "Apuesta":
    list_1 = ["♠", "♥", "♣", "♦️"]
    random_1 = list_1[random.randint(0, len(list_1)-1)]
    random_2 = list_1[random.randint(0, len(list_1)-1)]
    random_3 = list_1[random.randint(0, len(list_1)-1)]
    continuar = "y"
    while continuar == "y":
        list_1 = ["♠", "♥", "♣", "♦️"]
        random_1 = list_1[random.randint(0, len(list_1)-1)]
        random_2 = list_1[random.randint(0, len(list_1)-1)]
        random_3 = list_1[random.randint(0, len(list_1)-1)]
        if random_1 == random_2 and random_2 == random_3:
            print(f'''Has ganado, ya que obtuviste: {random_1} {random_2} {random_3}''')
            continuar = input(f'''Quieres seguir jugando? (y/n): ''')
        else:
            print(f'''No ganaste! Obtuviste {random_1} {random_2} {random_3}''')
            continuar = input(f'''Quieres seguir jugando? (y/n): ''')
    print(f'''Gracias por haber jugado!''')
else:
    print(f'''No dijitaste "Apuesta", te esperamos la próxima vez con ganas de ganar!''')