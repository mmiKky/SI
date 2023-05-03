from board.board import Board
from player.human_player import HumanPlayer
from player.minimax_player import MinimaxPlayer
from player.minimax_alfa_beta_player import MinimaxAlfaBetaPlayer
import board.board_drawer as board_drawer
from logic_guard.logic_guard import LogicGuard


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
            return MinimaxPlayer(), MinimaxPlayer()
        case 5:
            return MinimaxPlayer(), MinimaxAlfaBetaPlayer()
        case 6:
            return MinimaxAlfaBetaPlayer(), MinimaxAlfaBetaPlayer()
        case _:
            print('Invalid menu option')


def run_game(board, player1, player2):
    board_2D_list = board.get_2D_list()
    logic_guard = LogicGuard(board_2D_list)
    is_game_over_for_player1 = False
    is_game_over_for_player2 = False

    def perform_one_round(player):
        possible_moves = logic_guard.generate_possible_moves(player.symbol)
        board_drawer.draw_board_with_possible_moves(board_2D_list, possible_moves)
        move = player.make_move()
        while not logic_guard.validate_move(player.symbol, move):
            print('Invalid move')
            move = player.make_move()
        board.add_move(player.symbol, move)
        board_drawer.draw_board(board_2D_list)
        is_game_over_for_player1 = logic_guard.is_game_over_for_player(player1.symbol)
        is_game_over_for_player2 = logic_guard.is_game_over_for_player(player2.symbol)

    def choose_winner():
        player1_points = logic_guard.get_number_of_points(player1.symbol)
        player2_points = logic_guard.get_number_of_points(player2.symbol)
        if player1_points > player2_points:
            print(player1.symbol + ' won!')
        elif player2_points > player1_points:
            print(player2.symbol + ' won!')
        else:
            print('draw')

    # game loop
    while (not is_game_over_for_player1) and (not is_game_over_for_player2):
        if not is_game_over_for_player1:
            perform_one_round(player1)

        if not is_game_over_for_player2:
            perform_one_round(player2)
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