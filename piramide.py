def calcular_altura_piramide(blocos):
    altura = 0
    camadas = 0

    while blocos >= camadas + 1:
        camadas += 1
        blocos -= camadas
        altura += 1

    return altura

# Exemplo de uso
blocos = int(input("Digite o número de blocos: "))
altura = calcular_altura_piramide(blocos)
print("A altura da pirâmide:", altura)