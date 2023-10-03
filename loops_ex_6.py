numero_1 = 11
numero_2 = 12

contador = 2
min_com_mult = ""

while not(contador % numero_1 == 0 and contador % numero_2 == 0):
    contador += 1

min_com_mult += str(contador)

print(f'''El mínimo común múltiplo de {numero_1} y {numero_2} es {min_com_mult}''')