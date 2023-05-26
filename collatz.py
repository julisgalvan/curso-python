def collatz_conjecture(n):
    count = 0
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    print(n)  # Imprime o último valor (1)
    return count

# Obtém o número do usuário
number = int(input("Digite um número natural: "))

# Executa a Conjectura de Collatz e conta o número de etapas
step_count = collatz_conjecture(number)

# Imprime o número de etapas necessárias para atingir o objetivo
print("Número de etapas:", step_count)