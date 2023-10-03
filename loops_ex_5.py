numero = int(input("Type an integer number: "))
numero_print = numero
contador = 2
lista_primos = ""

while contador <= numero :
    if numero % contador == 0:
        lista_primos += str(contador) + " "
        numero = numero / contador
    else:
        contador += 1

print(f'''La lista de números primos que descomponen al {numero_print} es {lista_primos}''')
