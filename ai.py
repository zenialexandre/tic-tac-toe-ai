import math
import copy
import numpy
import game_helper
import board_helper
import constants

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.deepcopy(game_helper.board_matrix)
    is_max = True if (generic_player_handler[constants.MAX_PLAYER] == constants.AI) else False
    #best_possible_move = { 'row_position': 0, 'column_position': 0 }

    if (is_max == True):
        symbol = generic_player_handler[constants.CURRENT_SYMBOL]
    elif (not is_max and generic_player_handler[constants.CURRENT_SYMBOL] == constants.X_SYMBOL):
        symbol = constants.O_SYMBOL
    elif (not is_max and generic_player_handler[constants.CURRENT_SYMBOL] == constants.O_SYMBOL):
        symbol = constants.X_SYMBOL

    if (numpy.count_nonzero(board_matrix_clone == '-') > 0):
        score = minimax_decision(generic_player_handler, board_matrix_clone, is_max, symbol, numpy.count_nonzero(board_matrix_clone == '-'))

    execute_ai_actions(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, score, board_lines_color)

def execute_ai_actions(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, score, board_lines_color):
    ai_quadrant = get_ai_quadrant(score[0], score[1])
    board_helper.draw_symbol(pygame, display_surface, generic_player_handler, True, ai_quadrant, None, board_lines_color)
    game_helper.fill_board_matrix(board_helper.drawed_symbols, True, ai_quadrant, None)
    grid_quadrants[ai_quadrant][constants.IS_FILLED] = True
    game_helper.search_for_winner(game_state_handler, grid_quadrants, board_helper.drawed_symbols)

def minimax_decision(generic_player_handler, board_matrix_clone, is_max, symbol, depth) -> [int, int, int]:
    winner = check_winner(board_matrix_clone, symbol)
    best_score_minimax = []

    if (winner == True):
        return winner

    if (is_max == True):
        best_score_minimax.extend([-1, -1, -math.inf])
        symbol_max = generic_player_handler[constants.CURRENT_SYMBOL]
        symbol_inverted = constants.O_SYMBOL if (symbol_max == constants.X_SYMBOL) else constants.X_SYMBOL

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = symbol
                    best_score_minimax[2] = max(best_score_minimax[2], minimax_decision(generic_player_handler, board_matrix_clone, False, symbol_inverted, depth - 1)[2])
                    best_score_minimax[0] = i
                    best_score_minimax[1] = j
                    board_matrix_clone[i][j] = '-'

                    if (best_score_minimax[2] > -math.inf):
                        return best_score_minimax
    else:
        best_score_minimax.extend([-1, -1, math.inf])
        symbol_min = constants.O_SYMBOL if (symbol == constants.X_SYMBOL) else constants.X_SYMBOL
        symbol_inverted = constants.O_SYMBOL if (symbol_min == constants.X_SYMBOL) else constants.X_SYMBOL

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = symbol_min
                    best_score_minimax[2] = min(best_score_minimax[2], minimax_decision(generic_player_handler, board_matrix_clone, True, symbol_inverted, depth - 1)[2])
                    best_score_minimax[0] = i
                    best_score_minimax[1] = j
                    board_matrix_clone[i][j] = '-'
                    
                    if (best_score_minimax[2] < math.inf):
                        return best_score_minimax

def get_ai_quadrant(score) -> str:
    quadrant = constants.FIRST_QUADRANT

    if (score[0] == 0 and score[1] == 0):
        pass
    elif (score[0] == 0 and score[1] == 1):
        quadrant = constants.SECOND_QUADRANT
    elif (score[0] == 0 and score[1] == 2):
        quadrant = constants.THIRD_QUADRANT
    elif (score[0] == 1 and score[1] == 0):
        quadrant = constants.FOURTH_QUADRANT
    elif (score[0] == 1 and score[1] == 1):
        quadrant = constants.FIFTH_QUADRANT
    elif (score[0] == 1 and score[1] == 2):
        quadrant = constants.SIXTH_QUADRANT
    elif (score[0] == 2 and score[1] == 0):
        quadrant = constants.SEVENTH_QUADRANT
    elif (score[0] == 2 and score[1] == 1):
        quadrant = constants.EIGHTH_QUADRANT
    else:
        quadrant = constants.NINTH_QUADRANT
    return quadrant

def check_winner(board_matrix_clone, symbol) -> int:
    winning_result = 1

    if (game_helper.check_winning_scenarios(board_matrix_clone, symbol)):
        pass
    elif (numpy.count_nonzero(board_matrix_clone == '-') == 0):
        winning_result = 0
    else:
        winning_result = -1
    return winning_result
