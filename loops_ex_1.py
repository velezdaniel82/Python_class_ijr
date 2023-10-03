numero_secreto = 7
adivinanza = int(input("Ingrese su adivinanza: "))
while numero_secreto != adivinanza: 
    adivinanza = int(input("No adivinaste! Intenta digitando otro número: "))
print("Adivinaste el número secreto!")