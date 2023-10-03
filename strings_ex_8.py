dad = input("Type the full name of the father: ")
mom = input("Type the full name of the mother: ")
child = input("Type the first name of the child: ")

first_digit_lastname_1 = dad.find(" ")
lenght = len(dad)
first_lastname = dad[first_digit_lastname_1:lenght]

first_digit_lastname_2 = mom.find(" ")
lenght_2 = len(mom)
second_lastname = mom[first_digit_lastname_2:lenght_2]

full_name = child + " " + first_lastname + " " + second_lastname

print(f'''The child's full name is: {full_name}''')