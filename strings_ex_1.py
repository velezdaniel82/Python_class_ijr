phrase = "Me encanta Python"
upper_phrase = phrase.upper()
lower_phrase = phrase.lower()
first_letters_phrase = phrase[0:5]
phrase_without_word = phrase.replace("Python", "JavaScript")
lenght = len(phrase)
print(f'''Su frase tiene {lenght} caracteres. Aquí está en mayúsculas: {upper_phrase} y aquí está en minúsculas: {lower_phrase}. Estos son los primeros 5 caracteres de su frase: {first_letters_phrase}. Esta es su frase sin la palabra Python: {phrase_without_word}.''')