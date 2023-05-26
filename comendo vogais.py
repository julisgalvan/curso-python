# Solicita que o usuário insira uma palavra
user_word = input("Digite uma palavra: ")
# e atribua-a à variável user_word.
user_word = user_word.upper()

for letter in user_word:
    # Preenchao corpo do loop for.
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
        print(letter)