name = input("Write your name: ")
age = input("Type your age: ")
age_int = int(age)
years_left_to_apply = 22 - age_int
years_left_to_apply_str = str(years_left_to_apply)
country = input("Type your home country: ")
print("¡Hello, " + name + "! " + "Thank you for connecting from " + country + ". There are only " + years_left_to_apply_str + " years left so you can work with us.")