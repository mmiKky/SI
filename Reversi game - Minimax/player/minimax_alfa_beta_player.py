from player.player import PlayerInterface
from minimax.minimax import Minimax

class MinimaxAlfaBetaPlayer(PlayerInterface):
    def __init__(self, symbol='A', strategy_nr=0):
        self.symbol = symbol
        self.__minimax = Minimax(strategy_nr)
        self.__tree_depth = 4

    def make_move(self, board):
        return self.__minimax.evaluate_move_alfa_beta(board, self.symbol, self.__tree_depth)
    