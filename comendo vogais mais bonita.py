user_word = input("Digite uma palavra: ")

user_word = user_word.upper()

word_without_vowels = ""

for letter in user_word:
    # Completa o corpo do loop.
        if letter == 'A':
            continue
        elif letter == 'E':
            continue
        elif letter == 'I':
            continue
        elif letter == 'O':
            continue
        elif letter == 'U':
            continue
        else:
            word_without_vowels += letter
        # Imprima a palavra atribuída a word_without_vowels.
print(word_without_vowels)
