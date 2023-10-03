username = "Daniel"
password = "dgdgd gdg"
lenght = len(password)
if lenght > 6 and lenght < 10 and password.find(" ") == -1:
   print(f'''Username and password correctly created!''')
else : 
   print(f'''Wrong lenght of the password.''')