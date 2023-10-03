name = input("Type the name of the author: ")
initial_name = name[0]
upper_initial_name = initial_name.upper()
lenght_name = len(name)
upper_initial_name = upper_initial_name + name[1:lenght_name]

lastname = input("Type the lastname of the author: ")
initial_lastname = lastname[0]
upper_initial_lastname = initial_lastname.upper()
lenght_lastname= len(lastname)
upper_initial_lastname = upper_initial_lastname + lastname[1:lenght_lastname]

year = input("Type the year of the publication: ")

title = input("Type the title of the publication: ")
initial_title = title[0]
upper_initial_title = initial_title.upper()
lenght_title = len(title)
upper_initial_title = upper_initial_title + title[1:lenght_title]

city = input("Type the city of the publication: ")
initial_city = city[0]
upper_initial_city = initial_city.upper()
lenght_city = len(city)
upper_initial_city = upper_initial_city + city[1:lenght_city]

editorial = input("Type the name of the editorial: ")
initial_editorial = editorial[0]
upper_initial_editorial = initial_editorial.upper()
lenght_editorial = len(editorial)
upper_initial_editorial = upper_initial_editorial + editorial[1:lenght_editorial]

print(f'''{upper_initial_lastname}, {initial_name}. ({year}). {upper_initial_title}. {upper_initial_city}: {upper_initial_editorial}''')