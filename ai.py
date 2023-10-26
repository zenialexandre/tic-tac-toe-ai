import math
import copy
import numpy
import game_helper
import board_helper
import constants

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.copy(game_helper.board_matrix)
    symbol = constants.CURRENT_SYMBOL if (len(board_helper.drawed_symbols) == 0) else board_helper.drawed_symbols[-1]
    best_score = -math.inf
    best_possible_move = { 'row_position': 0, 'column_position': 0 }

    for i in range(3):
        for j in range(3):
            if (board_matrix_clone[i][j] == '-'):
                board_matrix_clone[i][j] = symbol
                is_max = True if generic_player_handler[constants.MAX_PLAYER] == constants.AI else False
                score = minimax_decision(generic_player_handler, board_matrix_clone, is_max, symbol)
                game_helper.board_matrix[i][j] = '-'

                if (score > best_score):
                    best_score = score
                    best_possible_move[constants.ROW_POSITION] = i
                    best_possible_move[constants.COLUMN_POSITION] = j

    ai_quadrant = get_ai_quadrant(best_possible_move)
    board_helper.draw_symbol(pygame, display_surface, generic_player_handler, True, ai_quadrant, None, board_lines_color)
    game_helper.fill_board_matrix(board_helper.drawed_symbols, True, ai_quadrant, None)
    grid_quadrants[ai_quadrant][constants.IS_FILLED] = True
    game_helper.search_for_winner(game_state_handler, grid_quadrants, board_helper.drawed_symbols)

def minimax_decision(generic_player_handler, board_matrix_clone, is_max, symbol) -> int:
    winner = check_winner(board_matrix_clone, symbol)

    if (winner == True):
        return winner

    if (is_max == True):
        best_score_max = -math.inf

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = generic_player_handler[constants.CURRENT_SYMBOL]
                    best_score_max = max(minimax_decision(generic_player_handler, board_matrix_clone, False, constants.CURRENT_SYMBOL), best_score_max)
                    board_matrix_clone[i][j] = '-'

        return best_score_max
    else:
        best_score_min = math.inf
        symbol_min = constants.O_SYMBOL if (generic_player_handler[constants.CURRENT_SYMBOL] == constants.X_SYMBOL) else constants.X_SYMBOL

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = symbol_min
                    best_score_min = min(minimax_decision(generic_player_handler, board_matrix_clone, True, symbol_min), best_score_min)
                    board_matrix_clone[i][j] = '-'

        return best_score_min

def get_ai_quadrant(best_possible_move) -> str:
    quadrant = constants.FIRST_QUADRANT

    if (best_possible_move[constants.ROW_POSITION] == 0 and best_possible_move[constants.COLUMN_POSITION] == 0):
        return quadrant
    elif (best_possible_move[constants.ROW_POSITION] == 0 and best_possible_move[constants.COLUMN_POSITION] == 1):
        quadrant = constants.SECOND_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 0 and best_possible_move[constants.COLUMN_POSITION] == 2):
        quadrant = constants.THIRD_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 1 and best_possible_move[constants.COLUMN_POSITION] == 0):
        quadrant = constants.FOURTH_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 1 and best_possible_move[constants.COLUMN_POSITION] == 1):
        quadrant = constants.FIFTH_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 1 and best_possible_move[constants.COLUMN_POSITION] == 2):
        quadrant = constants.SIXTH_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 2 and best_possible_move[constants.COLUMN_POSITION] == 0):
        quadrant = constants.SEVENTH_QUADRANT
    elif (best_possible_move[constants.ROW_POSITION] == 2 and best_possible_move[constants.COLUMN_POSITION] == 1):
        quadrant = constants.EIGHTH_QUADRANT
    else:
        quadrant = constants.NINTH_QUADRANT

    return quadrant

def check_winner(board_matrix_clone, symbol) -> int:
    if ((board_matrix_clone[0][0] == symbol and board_matrix_clone[0][1] == symbol and board_matrix_clone[0][2] == symbol) \
        or (board_matrix_clone[1][0] == symbol and board_matrix_clone[1][1] == symbol and board_matrix_clone[1][2] == symbol) \
        or (board_matrix_clone[2][0] == symbol and board_matrix_clone[2][1] == symbol and board_matrix_clone[2][2] == symbol)):
        return 1
    elif ((board_matrix_clone[0][0] == symbol and board_matrix_clone[1][0] == symbol and board_matrix_clone[2][0] == symbol) \
        or (board_matrix_clone[0][1] == symbol and board_matrix_clone[1][1] == symbol and board_matrix_clone[2][1] == symbol) \
        or (board_matrix_clone[0][2] == symbol and board_matrix_clone[1][2] == symbol and board_matrix_clone[2][2] == symbol)):
        return 1
    elif ((board_matrix_clone[0][0] == symbol and board_matrix_clone[1][1] == symbol and board_matrix_clone[2][2] == symbol) \
        or (board_matrix_clone[0][2] == symbol and board_matrix_clone[1][1] == symbol and board_matrix_clone[2][0] == symbol)):
        return 1
    elif (numpy.count_nonzero(board_matrix_clone == '-') == 0):
        return 0
    else:
        return -1
