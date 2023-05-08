from player.player import PlayerInterface
from minimax.minimax import Minimax

class MinimaxAlfaBetaPlayer(PlayerInterface):
    def __init__(self, symbol='A'):
        self.symbol = symbol
        self.minimax = Minimax()

    def make_move(self, board):
        return self.minimax.evaluate_move_alfa_beta(board, self.symbol)
    