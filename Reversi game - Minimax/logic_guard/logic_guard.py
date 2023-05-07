
class LogicGuard():

    def validate_move(self, board_2D_list, player_symbol, move):
        row, col = move
        board_size = len(board_2D_list)

        if row >= board_size or col >= board_size or row < 0 or col < 0:
            return False

        if board_2D_list[row][col] != ' ':
            return False

        for row_delta in range(-1, 2):
            for col_delta in range(-1, 2):
                if row_delta == 0 and col_delta == 0:
                    continue
                curr_row, curr_col = row + row_delta, col + col_delta
                found_opponent = False
                while curr_row >= 0 and curr_row < board_size and curr_col >= 0 and curr_col < board_size:
                    if board_2D_list[curr_row][curr_col] == ' ':
                        break
                    if board_2D_list[curr_row][curr_col] == player_symbol:
                        if found_opponent:
                            return True
                        break
                    found_opponent = True
                    curr_row, curr_col = curr_row + row_delta, curr_col + col_delta
        return False

    def generate_possible_moves(self, board_2D_list, player_symbol):
        board_size = len(board_2D_list)
        possible_moves = []

        for row in range(board_size):
            for col in range(board_size):
                move = (row, col)
                if board_2D_list[row][col] == ' ' and self.validate_move(board_2D_list, player_symbol, move):
                    possible_moves.append(move)
        return possible_moves

    def is_game_over_for_player(self, board_2D_list, player_symbol):
        '''checks if game is over due to no more available moves'''

        return self.generate_possible_moves(board_2D_list, player_symbol) == []

    def get_number_of_points(self, board_2D_list, player_symbol):
        points = 0
        for row in board_2D_list:
            for symbol in row:
                if symbol == player_symbol:
                    points += 1
        return points
