from board.board import Board
from player.human_player import HumanPlayer
from player.minimax_player import MinimaxPlayer
from player.minimax_alfa_beta_player import MinimaxAlfaBetaPlayer
from logic_guard.logic_guard import LogicGuard
import board.board_drawer as board_drawer
import game_tree.game_tree_generator as game_tree


def print_menu():
    print('Available games:')
    print('1. human vs human')
    print('2. human vs minimax')
    print('3. human vs minimax - alfa beta')
    print('4. minimax vs miniax')
    print('5. minimax vs minimax - alfa beta')
    print('6. minimax - alfa beta vs minimax - alfa beta')


def read_game_mode():
    return int(input('Please type your choice: '))


def choose_players(menu_option):
    match menu_option:
        case 1:
            return HumanPlayer('X'), HumanPlayer('Y')
        case 2:
            return HumanPlayer(), MinimaxPlayer()
        case 3:
            return HumanPlayer(), MinimaxAlfaBetaPlayer()
        case 4:
            return MinimaxPlayer('X'), MinimaxPlayer('Y')
        case 5:
            return MinimaxPlayer(), MinimaxAlfaBetaPlayer()
        case 6:
            return MinimaxAlfaBetaPlayer('X'), MinimaxAlfaBetaPlayer('Y')
        case _:
            print('Invalid menu option')


def run_game(board, player1, player2):
    board_2D_list = board.get_2D_list()
    logic_guard = LogicGuard()
    is_game_over_for_player1 = False
    is_game_over_for_player2 = False

    def perform_one_round(player):
        nonlocal is_game_over_for_player1
        nonlocal is_game_over_for_player2
        possible_moves = logic_guard.generate_possible_moves(board_2D_list, player.symbol)
        board_drawer.draw_board_with_possible_moves(board_2D_list, possible_moves)
        print(player.symbol + ' player move')
        
        move = player.make_move(board)
        while not logic_guard.validate_move(board_2D_list, player.symbol, move):
            print('Invalid move')
            move = player.make_move(board)
        board.add_move(player.symbol, move)
        is_game_over_for_player1 = logic_guard.is_game_over_for_player(board_2D_list, player1.symbol)
        is_game_over_for_player2 = logic_guard.is_game_over_for_player(board_2D_list, player2.symbol)

    def choose_winner():
        player1_points = logic_guard.get_number_of_points(board_2D_list, player1.symbol)
        player2_points = logic_guard.get_number_of_points(board_2D_list, player2.symbol)
        if player1_points > player2_points:
            print(f'{player1.symbol} won! ({player1_points}:{player2_points})')
        elif player2_points > player1_points:
            print(f'{player2.symbol} won! ({player2_points}:{player1_points})')
        else:
            print('draw')

    # game loop
    while (not is_game_over_for_player1) and (not is_game_over_for_player2):
        if not is_game_over_for_player1:
            perform_one_round(player1)

        if not is_game_over_for_player2:
            perform_one_round(player2)
    board_drawer.draw_board(board_2D_list)
    choose_winner()


if __name__ == '__main__':
    print_menu()
    menu_option = read_game_mode()
    player1, player2 = choose_players(menu_option)

    board = Board(player1.symbol, player2.symbol)
    run_game(board, player1, player2)


    # drawer tests
    # board = [    [" ", " ", " ", " ", " ", " ", " ", " "],
    # [" ", " ", " ", " ", " ", " ", " ", " "],
    # [" ", " ", " ", " ", " ", " ", " ", " "],
    # [" ", " ", " ", "X", "O", " ", " ", " "],
    # [" ", " ", " ", "O", "X", " ", " ", " "],
    # [" ", " ", " ", " ", " ", " ", " ", " "],
    # [" ", " ", " ", " ", " ", " ", " ", " "],
    # [" ", " ", " ", " ", " ", " ", " ", " "]]
    
    # board_drawer.draw_board(board)
    # board_drawer.draw_board_with_possible_moves(board, [(3, 5), (6, 1)])
    # board_drawer.draw_board(board)