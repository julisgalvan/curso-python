my_list = [8, 10, 6, 2, 4]  # Lista para ordenar
swapped = True  # É um pouco falso, precisamos dele para entrar no loop while.
 
while swapped:
    swapped = False  # nenhuma troca até agora
    for i in range(len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True  # uma troca ocorreu!
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
 
print(my_list)