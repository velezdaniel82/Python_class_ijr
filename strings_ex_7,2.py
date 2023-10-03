sum = input("Define the sum: ")

#first_digit_number_1 = sum[0]
#first_digit_number_1_int = int(first_digit_number_1)
last_digit_number_1 = sum.find("+")
number_1 = sum[0 : last_digit_number_1]
number_1_int = int(number_1)

print(number_1_int)

first_digit_number_2 = last_digit_number_1 + 1
#first_digit_number_2_int = int(first_digit_number_2)
lenght_sum = len(sum)
last_digit_number_2 = lenght_sum
#last_digit_number_2_int = int(last_digit_number_2)
number_2 = sum[first_digit_number_2 : last_digit_number_2]
number_2_int = int(number_2)

print(number_2_int)

operation = number_1_int + number_2_int
operation_str = str(operation)

print(f'''The result of the operation is: {operation_str}''')