number = input("Type a number: ")
number_lenght = len(number)-1
inv_number = ""
while number_lenght >= 0:
    inv_number += number[number_lenght]
    number_lenght -= 1
print(f'''The inverse number is: {inv_number}''')