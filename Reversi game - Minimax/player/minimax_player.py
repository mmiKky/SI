from player.player import PlayerInterface
from minimax.minimax import Minimax

class MinimaxPlayer(PlayerInterface):
    def __init__(self, symbol='O'):
        self.symbol = symbol
        self.minimax = Minimax()

    def make_move(self, board):
        return self.minimax.evaluate_move(board, self.symbol)
