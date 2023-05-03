
class LogicGuard():
    def __init__(self, board):
        self.board = board

    def validate_move(self, player_symbol, move):
        row, col = move
        board = self.board

        if row >= len(board) or col >= len(board) or row < 0 or col < 0:
            return False

        if board[row][col] != ' ':
            return False

        #TODO change names
        for row_delta in range(-1, 2):
            for col_delta in range(-1, 2):
                # print(str(d_row) + ' ' + str(d_col))
                if row_delta == 0 and col_delta == 0:
                    continue
                curr_row, curr_col = row + row_delta, col + col_delta
                found_opponent = False
                while curr_row >= 0 and curr_row < len(board) and curr_col >= 0 and curr_col < len(board[0]):
                    if board[curr_row][curr_col] == ' ':
                        break
                    if board[curr_row][curr_col] == player_symbol:
                        if found_opponent:
                            return True
                        break
                    found_opponent = True
                    curr_row, curr_col = curr_row + row_delta, curr_col + col_delta
        return False

    def generate_possible_moves(self, player_symbol):
        board = self.board
        board_size = len(board)
        possible_moves = []

        for row in range(board_size):
            for col in range(board_size):
                move = (row, col)
                if board[row][col] == " " and self.validate_move(player_symbol, move):
                    possible_moves.append(move)
        return possible_moves

    def is_game_over_for_player(self, player_symbol):
        '''checks if game is over due to no more available moves'''

        return self.generate_possible_moves(player_symbol) == []

    def get_number_of_points(self, player_symbol):
        points = 0
        for row in self.board:
            for symbol in row:
                if symbol == player_symbol:
                    points += 1
        return points

    # def choose_winner(self):
    #     player_points = {}

    #     def increase_counter(player_symbol):
    #         if player_symbol in player_points:
    #             player_points[player_symbol] += 1
    #         else:
    #             player_points[player_symbol] = 1

    #     for row in self.board:
    #         for symbol in row:
    #             if symbol != ' ':
    #                 increase_counter(symbol)
    #     highest_points = 0
    #     winner = ''
    #     for player_symbol, points in player_points:
    #         if points > highest_points:
    #             highest_points = points
