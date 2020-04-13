import os
import random


def clear(): return os.system('cls')  # on Windows System


board_numbered = ["3", "2", "1",
                  "6", "5", "4",
                  "9", "8", "7"]

board_clean = ["", "", "",
               "", "", "",
               "", "", ""]


def display_board(board):
    board = map_cells_board(board)

    line_limiter = 0
    current_line = ""

    board = board[::-1]

    print(" ___ ___ ___ ")

    for item in board:

        current_line += item
        line_limiter += 1

        if(line_limiter >= 3):
            line_limiter = 0
            current_line = current_line.replace("||", "|")
            print("|   |   |   |")
            print(current_line)
            print("|___|___|___|")
            current_line = ""


def map_cells_board(board):
    return list(map(makecell, board))


def makecell(str_cell_val):
    if(str_cell_val == "" or str_cell_val == None):
        return f'|   |'
    else:
        return f'| {str_cell_val} |'


def player_input():
    player1 = None
    player2 = None
    while player1 != 'X' and player1 != "O" and player1 != "R":
        player1 = input(
            "Пожалуйста выберите 'X' или 'O' или 'R' для случайного: ")

    if(player1 == 'R'):
        player1 = choose_first()

    if(player1 == 'X'):
        player2 = 'O'
    elif(player1 == 'O'):
        player2 = 'X'

    return player1, player2


def place_marker(board, marker, position):
    for cell_index, cell in enumerate(board):
        if(cell.isnumeric()):
            if(int(cell) == position):
                board[cell_index] = marker
                return board
    return board


def win_check(board, mark):
    for count_i in range(3):
        # Горизонтальные линии
        if (board[0+count_i*3] == mark and
            board[1+count_i*3] == mark and
                board[2+count_i*3] == mark):
            return True

        # Вертикальные линии
        if (board[0+count_i] == mark and
            board[3+count_i] == mark and
                board[6+count_i] == mark):
            return True

    # Наискосок линии
    if(board[0] == mark
            and board[4] == mark
            and board[8] == mark):
        return True

    if(board[2] == mark
            and board[4] == mark
            and board[6] == mark):
        return True

    return False


def choose_first():
    random_result = random.randint(0, 1)
    if(random_result == 0):
        return 'O'
    elif (random_result == 1):
        return 'X'


def space_check(board, position):    
    return board[position] != 'X' and board[position] != 'O'


def full_board_check(board):
    for item in board:
        if(item != 'X' and item != 'O'):
            return False

    return True


def convert_position(position):
    global board_numbered

    for index, item in enumerate(board_numbered):
        if(item == position):
            return index


def player_choice(board):
    is_space = False

    while(not is_space):
        position = '0'
        while not position in '123456789' or position is None or position == '':
            position = input('Пожалуйста введите число от 1 до 9: ')

        position_array = convert_position(position)
        is_space = space_check(board, position_array)

    return int(position)


def replay():
    need_restart = None
    while(need_restart != 'Y' and need_restart != 'N'):
        need_restart = input("Вы хотите сыграть ещё партию? 'Y' или 'N': ")

    if(need_restart == 'Y'):
        return True
    elif (need_restart == 'N'):
        return False


def player_phase(current_board, mark, first_go, second_go):

    chosen_id = player_choice(current_board)
    clear()
    current_board = place_marker(current_board, mark, chosen_id)
    mark_won = win_check(current_board, mark)
    full_board = full_board_check(current_board)
    display_board(current_board)
    if(mark_won):
        if(mark == 'X'):
            print("Победили крестики - Игрок № "+str(first_go))
        else:
            print("Победили нолики - Игрок № "+str(second_go))

    if(full_board and not mark_won):
        print("Ничья")

    game_on = not mark_won and not full_board

    return game_on, current_board


if __name__ == "__main__":
    while True:
        current_board=[]
        current_board.clear()
        clear()
        print("Крестики-нолики для двоих")
        player1, player2 = player_input()

        if(player1 == 'X'):
            first_go = 1
            second_go = 2
            print("Первый игрок - крестики, второй - нолики")
        else:
            first_go = 2
            second_go = 1
            print("Первый игрок - нолики, второй - крестики")

        current_board = board_numbered.copy()
        display_board(current_board)
        game_on = True

        while game_on:
            print("Ход Игрока №"+str(first_go))
            game_on, current_board = player_phase(
                current_board, 'X', first_go, second_go)

            if(game_on):         
                print("Ход Игрока №"+str(second_go))
                game_on, current_board=player_phase(
                    current_board,'O',first_go,second_go)

        if(not replay()):
            break           
  