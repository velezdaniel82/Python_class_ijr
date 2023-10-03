object = input("Write an object ")
lenght = len(object)
initial = object[0]
upper_initial = initial.upper()
last = object[lenght-1]
upper_last = last.upper()
upper_initial_and_last_object = upper_initial + object[1:lenght - 1] + upper_last
print(f'''¡Hola, {upper_initial_and_last_object}!''')