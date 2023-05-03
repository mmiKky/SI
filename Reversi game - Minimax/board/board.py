
class Board:
    def __init__(self, symbol1, symbol2):
        self.BOARD_SIZE = 8
        self.__board = []
        for row_nr in range(self.BOARD_SIZE):
            self.__board.append([])
            for elem_nr in range(self.BOARD_SIZE):
                self.__board[row_nr].append(' ')
        self.__draw_init_symbols(symbol1, symbol2)

    def add_move(self, player_symbol, move):
        (row, col) = move
        self.__board[row][col] = player_symbol
        self.__flip_discs(player_symbol, move)

    def get_2D_list(self):
        return self.__board
    
    def __flip_discs(self, player_symbol, move):
        (row, col) = move
        board = self.__board

        discs_to_flip = []

        for row_delta in range(-1, 2):
            for col_delta in range(-1, 2):
                if row_delta == 0 and col_delta == 0:
                    continue
                curr_row, curr_col = row + row_delta, col + col_delta
                found_opponent = False
                potential_discs_to_flip = []
                while curr_row >= 0 and curr_row < len(board) and curr_col >= 0 and curr_col < len(board[0]):
                    if board[curr_row][curr_col] == ' ':
                        break
                    if board[curr_row][curr_col] == player_symbol:
                        if found_opponent:
                            potential_discs_to_flip.append((curr_row, curr_col))
                            discs_to_flip.extend(potential_discs_to_flip)
                        break
                    potential_discs_to_flip.append((curr_row, curr_col))
                    found_opponent = True
                    curr_row, curr_col = curr_row + row_delta, curr_col + col_delta
        for row, col in discs_to_flip:
            board[row][col] = player_symbol

    def __draw_init_symbols(self, symbol1, symbol2):
        self.__board[self.BOARD_SIZE//2-1][self.BOARD_SIZE//2-1] = symbol1
        self.__board[self.BOARD_SIZE//2][self.BOARD_SIZE//2] = symbol1

        self.__board[self.BOARD_SIZE//2-1][self.BOARD_SIZE//2] = symbol2
        self.__board[self.BOARD_SIZE//2][self.BOARD_SIZE//2-1] = symbol2
