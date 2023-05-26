import random

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   {}   |   {}   |   {}   |".format(row[0], row[1], row[2]))
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        move = int(input("Digite seu movimento: "))
        row = (move - 1) // 3
        col = (move - 1) % 3
        if 1 <= move <= 9 and board[row][col] != "X" and board[row][col] != "O":
            board[row][col] = "O"
            break
        else:
            print("Movimento inválido. Tente novamente.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] != "X" and board[row][col] != "O":
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == sign:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == sign:
            return True
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True
    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = "X"

def main():
    board = [[str(i + j*3 + 1) for i in range(3)] for j in range(3)]
    board[1][1] = "X"

    display_board(board)

    while True:
        enter_move(board)
        display_board(board)
        if victory_for(board, "O"):
            print("Você ganhou!")
            break
        free_fields = make_list_of_free_fields(board)
        if not free_fields:
            print("Empate!")
            break
        draw_move(board)
        display_board(board)
        if victory_for(board, "X"):
            print("Você perdeu!")
            break

if __name__ == "__main__":
    main()