import math
import copy
import game_helper
import constants

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.deepcopy(game_helper.board_matrix)
    depth = 0
    best_score = -math.inf
    best_possible_move = { 'row_position': 0, 'column_position': 0 }

    for i in range(3):
        for j in range(3):
            if (board_matrix_clone[i][j] == '-'):
                board_matrix_clone[i][j] = generic_player_handler[constants.CURRENT_SYMBOL]
                score = minimax_decision(generic_player_handler, board_matrix_clone, depth)
                board_matrix_clone[i][j] = '-'

                if (score > best_score):
                    best_score = score
                    best_possible_move['row_position'] = i
                    best_possible_move['column_position'] = j

    game_helper.board_matrix[best_possible_move['row_position']][best_possible_move['column_position']] = generic_player_handler[constants.CURRENT_SYMBOL]
    # here the AI should call 'draw_symbol' to populate the drawed_symbols vector and then search for a winner. 

def minimax_decision(generic_player_handler, board_matrix_clone, depth):
    '''
    if (game_helper.check_winning_scenarios(board_matrix_clone, generic_player_handler[constants.CURRENT_SYMBOL]) == True):
        return 1
    else:
        if (numpy.count_nonzero(board_matrix_clone == '-') == 0):
            return 0
        else:
            return -1
    '''

    if (generic_player_handler[constants.MAX_PLAYER] == constants.AI):
        best_score_max = -math.inf

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = generic_player_handler[constants.CURRENT_SYMBOL]
                    best_score_max = max(best_score_max, minimax_decision(generic_player_handler, board_matrix_clone, depth + 1))
        
        return best_score_max
    else:
        best_score_min = math.inf

        for i in range(3):
            for j in range(3):
                if (board_matrix_clone[i][j] == '-'):
                    board_matrix_clone[i][j] = generic_player_handler[constants.CURRENT_SYMBOL]
                    best_score_min = min(best_score_min, minimax_decision(generic_player_handler, board_matrix_clone, depth + 1))
        
        return best_score_min

def get_possible_moves_on_context(board_matrix_clone):
    possible_moves_on_context = []

    for i in range(3):
        for j in range(3):
            if (board_matrix_clone[i][j] == '-'):
                possible_moves_on_context.append([i, j])

    return possible_moves_on_context
