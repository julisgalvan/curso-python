secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, querido!   |
| Insira um número inteiro e        |
| tente adivinhar o número que tenho|
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

number = int(input("Digite um número e descubra: "))

while number != secret_number:
    if number != secret_number:
        print("Ha Ha! Você está preso no meu loop!")
    number = int(input("Digite um número e descubra: "))

print("Muito bem, querido! Você está livre agora.")