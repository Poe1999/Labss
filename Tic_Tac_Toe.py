import random

board = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

def show_board():
    print("\n   0   1   2")
    for row_num, row in enumerate(board):
        print(row_num, end="  ")
        print(" | ".join(row))
        if row_num < 2:
            print("  -----------")

def check_win(symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
 # если один и тот же символ стоит в одной стоке
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if all(cell == symbol for cell in column):
            return True
 # если один и тот же символ стоит в столбце
    diagonal1 = [board[i][i] for i in range(3)]
    diagonal2 = [board[i][2 - i] for i in range(3)]

    return all(cell == symbol for cell in diagonal1) or all(cell == symbol for cell in diagonal2)
 # если один и тот же символ в диагоналит
def computer_move(): # ход компьютера
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_cells.append((row, col))

    if len(empty_cells)>0:
       return random.choice(empty_cells) # случайно выбирает свободную клетку

player = "X"
computer = "O"
while True:
    show_board()

    if player == "X":
        try:
            row, col = map(int, input("Ваш ход: "))
            if board[row][col] != " ":
                print("Уже занято")
                continue
            board[row][col] = "X"
        except:
            print("Ввдеите две цифры 0-2")
            continue
    else:
        row, col = computer_move()
        board[row][col] = "O"

    if check_win(player):
        show_board()
        print("Вы выиграли!" if player == "X" else "Компьюиер выиграл!")
        break

    if all(cell != " " for row in board for cell in row):
        show_board()
        print("It's a tie!")
        break

    player, computer = computer, player  # смена хода