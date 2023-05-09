import game_tree.game_tree_generator as game_tree
from time import time

DEFAULT_MOVE_VALUE = 100000

class Minimax():
    def __init__(self, strategy_nr=0):
        self.logic_guard = game_tree.logic_guard
        self.__strategy_nr = strategy_nr

    def evaluate_move(self, board, player_symbol, depth):
        game_tree_root = game_tree.generate_game_tree(board, player_symbol, depth)
        print('tree generated')
        best_move_value = -DEFAULT_MOVE_VALUE-1

        start_time = time()
        for node in game_tree_root.children:
            move_value = self.__minimax(node, False)
            if move_value > best_move_value:
                best_move_value = move_value
                best_move = node.last_move
        print('choose move time: ' + str(time() - start_time))
        return best_move
    
    def evaluate_move_alfa_beta(self, board, player_symbol, depth):
        game_tree_root = game_tree.generate_game_tree(board, player_symbol, depth)
        print('tree generated')
        best_move_value = -DEFAULT_MOVE_VALUE-1

        start_time = time()
        for node in game_tree_root.children:
            move_value = self.__minimax_alfa_beta(node, -DEFAULT_MOVE_VALUE, DEFAULT_MOVE_VALUE, False)
            if move_value > best_move_value:
                best_move_value = move_value
                best_move = node.last_move
        print('choose move time: ' + str(time() - start_time))
        return best_move

    def __minimax(self, node, maximizing_player):
        '''
        implementation of minimax algorithm; it is not limited to depth because game tree is 
        and it is not needed to limit it twice
        '''
        if node.children == {None}:
            return self.__calculate_heuristic(node.board, node.last_player)
        if maximizing_player:
            value = -DEFAULT_MOVE_VALUE
            for child in node.children:
                value = max(value, self.__minimax(child, False))
            return value
        else:
            value = DEFAULT_MOVE_VALUE
            for child in node.children:
                value = min(value, self.__minimax(child, True))
            return value
    
    def __minimax_alfa_beta(self, node, alfa, beta, maximizing_player):
        '''
        implementation of minimax algorithm; it is not limited to depth because game tree is 
        and it is not needed to limit it twice
        '''
        if node.children == {None}:
            return self.__calculate_heuristic(node.board, node.last_player)
        if maximizing_player:
            value = -DEFAULT_MOVE_VALUE
            for child in node.children:
                value = max(value, self.__minimax_alfa_beta(child, alfa, beta, False))
                if value > beta:
                    break
                alfa = max(alfa, value)
            return value
        else:
            value = DEFAULT_MOVE_VALUE
            for child in node.children:
                value = min(value, self.__minimax_alfa_beta(child, alfa, beta, True))
                if value < alfa:
                    break
                beta = min(beta, value)
            return value

    def __calculate_heuristic(self, board, player_symbol):
        match self.__strategy_nr:
            case 0: return self.__heuristic_owned_fields(board, player_symbol)
            case 1: return self.__heuristic_opponents_fields(board, player_symbol)
            case 2: return self.__heuristic_available_moves(board, player_symbol)

    def __heuristic_owned_fields(self, board, player_symbol):
        '''heuristic measuring board value by difference between players discs'''
        player_discs_nr = self.logic_guard.get_number_of_points(board.get_2D_list(), player_symbol)
        oponent_discs_nr = self.logic_guard.get_number_of_points(board.get_2D_list(), board.get_oponent_symbol(player_symbol))
        return player_discs_nr - oponent_discs_nr
    
    def __heuristic_opponents_fields(self, board, player_symbol):
        '''heuristic measuring number of fields which cannot be get by an oponent'''
        return board.BOARD_SIZE**2 - len(
            self.logic_guard.generate_possible_moves(board.get_2D_list(), board.get_oponent_symbol(player_symbol)))

    def __heuristic_available_moves(self, board, player_symbol):
        '''heuristic measuring number of available moves'''
        return len(self.logic_guard.generate_possible_moves(board.get_2D_list(), player_symbol))
