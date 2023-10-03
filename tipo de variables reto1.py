user_name = input("introduce your username: ")
birth_year = input("Introduce your birth year: ")
birth_year_int = int(birth_year)
age = 2023 - birth_year_int
age_str = str(age)
print("¡Hola, " + user_name + "! " + "At the age of " + age_str + " you are entering this platform for the first time.")