from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("| " * 3, "|", sep="")
        for col in range(3):
            print("| " + str(board[row][col]) + " ", end="")
        print("|")
        print("| " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    ok = False  # suposição falsa - precisamos dela para entrar no loop
    while not ok:
        move = input("Digite seu movimento: ")
        ok = len(move) == 1 and move >= '1' and move <= '9'  # a entrada do usuário é válida?
        if not ok:
            print("Movimento ruim - repita sua entrada!")  # não, não é - faça a entrada novamente
            continue
        move = int(move) - 1  # número da célula de 0 a 8
        row = move // 3  # linha da célula
        col = move % 3  # coluna da célula
        sign = board[row][col]  # verifique o quadrado selecionado
        ok = sign not in ['O', 'X']
        if not ok:  # está ocupado - para a entrada novamente
            print("Campo já ocupado - repita sua entrada!")
            continue
        board[row][col] = 'O'  # definir '0' no quadrado selecionado


def make_list_of_free_fields(board):
    free = []  # a lista está vazia inicialmente
    for row in range(3):  # iterar pelas linhas
        for col in range(3):  # iterar pelas colunas
            if board[row][col] not in ['O', 'X']:  # o celular está livre?
                free.append((row, col))  # sim, é - anexar nova tupla à lista
    return free


def victory_for(board, sgn):
    if sgn == "X":  # estamos procurando por X?
        who = 'me'  # sim - é a lateral do computador
    elif sgn == "O":  # ... ou para O?
        who = 'you'  # sim - é o nosso lado
    else:
        who = None  # nós não deveríamos cair aqui!
    cross1 = cross2 = True  # para diagonais
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # verificar linha rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # verificar coluna rc
            return who
        if board[rc][rc] != sgn:  # verificar 1ª diagonal
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # verificar 1ª diagonal
            cross1 = False
        if board[rc][2 - rc] != sgn:  # verificar 2ª diagonal
            cross2 = False
        if cross1 or cross2:
            return who