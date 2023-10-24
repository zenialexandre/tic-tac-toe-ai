import numpy
import math
import copy
import game_helper
import constants

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.deepcopy(game_helper.board_matrix)
    minimax_decision(generic_player_handler, board_matrix_clone, None, 0)

def minimax_decision(generic_player_handler, board_matrix_clone, possible_move, depth):
    if (possible_move != None and not is_terminal_state(board_matrix_clone)):
        board_matrix_clone[possible_move[0], possible_move[1]] = generic_player_handler[constants.CURRENT_SYMBOL]
    elif (is_terminal_state(board_matrix_clone)):
        pass

    if (numpy.count_nonzero(board_matrix_clone == '-') == 1):
        return 0
    elif (generic_player_handler[constants.MAX_PLAYER] == constants.AI):
        utiliy_number = -math.inf

        for possible_move in get_possible_moves_on_context(board_matrix_clone):
            utiliy_number = max(utiliy_number, minimax_decision(generic_player_handler, board_matrix_clone, possible_move))

        return utiliy_number
    else:
        utiliy_number = math.inf
        pass

def max_value():
    pass

def min_value():
    pass

def is_terminal_state(board_matrix_cloned, generic_player_handler):
    return game_helper.check_winning_scenarios(board_matrix_cloned, generic_player_handler[constants.CURRENT_SYMBOL])

def get_possible_moves_on_context(board_matrix_clone):
    possible_moves_on_context = []

    for i in range(3):
        for j in range(3):
            if (board_matrix_clone[i][j] == '-'):
                possible_moves_on_context.append([i, j])

    return possible_moves_on_context
