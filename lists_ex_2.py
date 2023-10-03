import random

list_1 = ["la calabaza", "la coliflor", "el brócoli", "la zanahoria", "el guineo", "el calabacín", "el pepino", "la ahuyama", "el pepinillo"]
list_2 = ["rodilla", "codo", "hombro", "tobillo", "cuello", "cumbamba", "cadera"]
list_3 = ["es supersónico", "es de hierro", "tiene problemas de colesterol", "es mala gente", "es intolerante a la lactosa", "tiene problemas de autoestima"]
name = input("Type your name: ")
random_1 = random.randint(0, len(list_1)-1)
random_2 = random.randint(0, len(list_2)-1)
random_3 = random.randint(0, len(list_2)-1)
print(f''' {name}, si te gusta {list_1[random_1]}, significa que tu {list_2[random_2]} {list_3[random_3]}''')