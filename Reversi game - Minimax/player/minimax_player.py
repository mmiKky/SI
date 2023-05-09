from player.player import PlayerInterface
from minimax.minimax import Minimax

class MinimaxPlayer(PlayerInterface):
    def __init__(self, symbol='O', strategy_nr=0):
        self.symbol = symbol
        self.__minimax = Minimax(strategy_nr)
        self.__tree_depth = 4

    def make_move(self, board):
        return self.__minimax.evaluate_move(board, self.symbol, self.__tree_depth)
