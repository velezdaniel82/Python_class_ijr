calculate = input("Define the operation without spaces: ")

if calculate.find("+") != -1 :
    last_digit_number_1 = calculate.find("+")
    number_1 = calculate[0 : last_digit_number_1]
    number_1_int = int(number_1)

elif calculate.find("*") != -1 :
    last_digit_number_1 = calculate.find("*")
    number_1 = calculate[0 : last_digit_number_1]
    number_1_int = int(number_1)

elif calculate.find("-") != -1 :
    last_digit_number_1 = calculate.find("-")
    number_1 = calculate[0 : last_digit_number_1]
    number_1_int = int(number_1)

elif calculate.find("/") != -1 :
    last_digit_number_1 = calculate.find("/")
    number_1 = calculate[0 : last_digit_number_1]
    number_1_int = int(number_1)

else :
    print("You did not define an accepted operation.")

first_digit_number_2 = last_digit_number_1 + 1
lenght_calculate = len(calculate)
last_digit_number_2 = lenght_calculate
number_2 = calculate[first_digit_number_2 : last_digit_number_2]
number_2_int = int(number_2)

if calculate.find("+") != -1 :
    operation = number_1_int + number_2_int

elif calculate.find("*") != -1 :
    operation = number_1_int * number_2_int

elif calculate.find("-") != -1 :
    operation = number_1_int - number_2_int

elif calculate.find("/") != -1 :
    operation = number_1_int / number_2_int

operation_str = str(operation)

print(f'''The result of the operation is: {operation_str}''')