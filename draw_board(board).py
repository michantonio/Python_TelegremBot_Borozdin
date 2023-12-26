def draw_board(board):
    # запустить цикл, который проходит по всем 3 строкам доски
    for i in range(3):
        # поставить разделители значений в строке
        print(" | ".join(board[i]))
        # поставить разделители строк
        print("---------")

def ask_and_make_move(player, board):
    # дать игроку возможность сделать ход, то есть ввести координаты
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y)
    # задать условие, которое проверяет,
    # находится ли координата в пределах поля и свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        # если свободно, записать значение игрока (Х или 0) в ячейку
        board[x][y] = player
    else:
        print("That spot is already taken. Try again.")
        ask_and_make_move(player, board)

def ask_and_make_move(player, board):
    x, y = ask_move(player, board)
    # координаты x, y взять из функции ask_move(player, board)
    make_move(player, board, x, y)

def ask_move(player, board):
    # дать игроку возможность сделать ход, то есть ввести координаты
    x, y = input(f"{player}, enter x and y coordinates (e.g. 0 0): ").strip().split()
    # преобразовать координаты в целые числа
    x, y = int(x), int(y)
    # задать условие, которое проверяет, свободно ли место
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
    # если клетка свободна, вернуть её координаты
        return(x, y)
    else:
        print("Клетка занята. Введите координаты еще раз.")
    return ask_move(player, board)

