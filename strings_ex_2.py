name = input("Type your name ")
initial = name[0]
upper_initial = initial.upper()
lenght = len(name)
upper_initial_name = upper_initial + name[1:lenght]
print(f'''¡Hola, {upper_initial_name}!''')