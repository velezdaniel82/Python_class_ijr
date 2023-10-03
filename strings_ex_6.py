name = input("Type your name: ")
lastname = input ("Type your lastname: ")
initial_name = name[0]
upper_initial_name = initial_name.upper()
lenght_name = len(name)
upper_initial_name = upper_initial_name + name[1:lenght_name]

initial_lastname = lastname[0]
upper_initial_lastname = initial_lastname.upper()
lenght_lastname= len(lastname)
upper_initial_lastname = upper_initial_lastname + lastname[1:lenght_lastname]

print(f'''{upper_initial_lastname}, {upper_initial_name}.''')