my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Cria uma nova lista vazia para armazenar os elementos exclusivos
unique_list = []

# Itera sobre cada elemento da lista original
for num in my_list:
    # Verifica se o elemento já existe na lista única
    if num not in unique_list:
        # Adiciona o elemento à lista única
        unique_list.append(num)

# Imprime a lista com os elementos exclusivos
print("A lista com os elementos exclusivos aqui:")
print(unique_list)
