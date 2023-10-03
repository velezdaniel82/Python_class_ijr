phrase = input("Type a phrase: ")
amount_of_words = 1
for i in phrase : 
    if i == " ":
            amount_of_words +=1
print(f'''La cantidad de palabras en su frase es de {amount_of_words} palabras.''')