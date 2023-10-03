number_1 = int(input(f'''Type the first number: '''))
number_2 = int(input(f'''Type the second number: '''))
if number_1 % 2 == 0 :
   number_1_type = "es par" 
else :
   number_1_type = "es impar"
if number_2 % 2 == 0 :
   number_2_type = "es par" 
else :
   number_2_type = "es impar"
suma = number_1 + number_2
if suma % 2 == 0 :
   suma_type = "par" 
else :
   suma_type = "impar"
print(f''' El primer número {number_1_type} y el segundo número {number_2_type}. El resultado de la suma de dichos números es {suma} y es un número {suma_type}.''')