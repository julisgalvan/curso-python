number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))
largest_number = number1
if number2 > largest_number: largest_number = number2
if number3 > largest_number: largest_number = number3
print("O maior número é: ", largest_number)
