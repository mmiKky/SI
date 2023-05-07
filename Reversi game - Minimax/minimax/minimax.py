import game_tree.game_tree_generator as game_tree

DEPTH_MAX = 5
DEFAULT_MOVE_VALUE = 100000

class Minimax():
    def __init__(self):
        self.logic_guard = game_tree.logic_guard

    def evaluate_move(self, board, player_symbol):
        game_tree_root = game_tree.generate_game_tree(board, player_symbol, DEPTH_MAX)
        best_move_value = -DEFAULT_MOVE_VALUE-1

        for node in game_tree_root.children:
            move_value = self.__minimax(node, False)
            if move_value > best_move_value:
                best_move_value = move_value
                best_move = node.last_move
        return best_move

    def __minimax(self, node, maximizing_player):
        '''
        implementation of minimax algorithm; it is not limited to depth because game tree is 
        and it is not needed to limit it twice
        '''
        if node.children == {None}:
            return self.__heuristic_owned_fields(node.board, node.last_player)
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
    

    def __heuristic_owned_fields(self, board, player_symbol):
        '''heuristic measuring board value by difference between players discs'''
        player_discs_nr = self.logic_guard.get_number_of_points(board.get_2D_list(), player_symbol)
        oponent_discs_nr = self.logic_guard.get_number_of_points(board.get_2D_list(), board.get_oponent_symbol(player_symbol))
        return player_discs_nr - oponent_discs_nr
    
    def __heuristic_opponents_fields():
        pass

    def __heuristic_available_moves():
        pass
