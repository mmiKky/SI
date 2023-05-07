from board.board import Board
from logic_guard.logic_guard import LogicGuard

logic_guard = LogicGuard()
prev_player = ''


def generate_game_tree(board, player_symbol, depth, previous_move=None):
    if depth == 0:
        return None

    possible_moves = logic_guard.generate_possible_moves(board.get_2D_list(), player_symbol)
    oponent_symbol = board.get_oponent_symbol(player_symbol)

    root = Node(board, previous_move, oponent_symbol)    
    for move in possible_moves:
        new_board = Board(player_symbol, oponent_symbol, board)
        new_board.add_move(player_symbol, move)
        child = generate_game_tree(new_board, oponent_symbol, depth - 1, previous_move=move)
        root.add_child(child)
    return root


class Node:
    def __init__(self, board, last_move, last_player):
        self.board = board
        self.last_move = last_move
        self.last_player = last_player
        self.children = set()

    def add_child(self, child):
        self.children.add(child)
        