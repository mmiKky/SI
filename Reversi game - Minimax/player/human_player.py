from player.player import PlayerInterface

class HumanPlayer(PlayerInterface):
    def __init__(self, symbol='X'):
        self.symbol = symbol

    def make_move(self, board=None):
        return self.__read_user_input()
        
    def __read_user_input(self):
        user_choice = input('Please type your move(format: row_nr col_nr; eg: 1 3): ')
        user_choice = user_choice.split()
        return int(user_choice[0]), int(user_choice[1])
