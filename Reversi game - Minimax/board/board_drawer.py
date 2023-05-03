import colorama

colorama.init()
POSSIBLE_MOVE_CHAR = '\u2588'    

def draw_board(board):
    size = len(board)
    
    # columns
    print()
    print(" 0 1 2 3 4 5 6 7")
    print(" +-+-+-+-+-+-+-+-+")

    # rows
    print_color = colorama.Fore.WHITE
    for row in range(size):
        print(row, end="|")
        for col in range(size):
            symbol = board[row][col]
            if symbol == POSSIBLE_MOVE_CHAR:
                print_color = colorama.Fore.GREEN
            print(print_color + symbol, end='|')
            print_color = colorama.Fore.WHITE
        print(print_color + '\n +-+-+-+-+-+-+-+-+')


def draw_board_with_possible_moves(board, possible_moves_list):
    '''draws board with possible moves marked; it is not modifying original board'''
    temp_list = [row[:] for row in board]
    for (x, y) in possible_moves_list:
        temp_list[x][y] = POSSIBLE_MOVE_CHAR
    draw_board(temp_list)
