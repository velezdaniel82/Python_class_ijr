phrase = input("Type a reprehensible phrase: ")
initial = phrase[0]
lenght = len(phrase)
new_phrase = phrase.replace(phrase, "%&/&%!")
print(f'''Oh, {new_phrase}''')