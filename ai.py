import math
import copy
import numpy
import game_helper
import board_helper
import constants

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.deepcopy(game_helper.board_matrix)
    symbol = constants.CURRENT_SYMBOL if (len(board_helper.drawed_symbols) == 0) else board_helper.drawed_symbols[-1]
    oponent_symbol = 'x' if symbol == 'o' else 'o'
    best_score = -math.inf
    best_possible_move = { 'row_position': 0, 'column_position': 0 }

    blank_spaces = get_board_blank_spaces(board_matrix_clone)

    execute_ai_actions(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, best_possible_move, board_lines_color)

def minimax_decision(board_matrix, blank_spaces, is_max, symbol, player) -> dict:
    heuristic_value = None
    position = None
    blank_spaces_copy = blank_spaces
    board_matrix_copy = board_matrix

    for space in blank_spaces_copy:
        if(space['symbol'] == '-'):
            space['symbol'] = symbol
            board_matrix_copy[space['row']][space['col']] = symbol

            if(game_helper.check_column_winning_scenarios((board_matrix_copy, symbol))):
                if(player == constants.PLAYER and is_max == constants.AI):
                    return -1, {'row_position': -1, 'column_position': -1}
                elif(player == constants.PLAYER and is_max != constants.AI):
                    return 1, {'row_position': -1, 'column_position': -1}
                elif(constants.AI != is_max):
                    return -1, {'row_position' : space['row'], 'column_position': space['col']}
                else:
                    return 1, {'row_position' : space['row'], 'column_position': space['col']}

            if(game_helper.check_terminal_state(board_matrix)):
                return 0, {'row_position': -1, 'column_position': -1} 
            
            player = constants.AI if player == constants.PLAYER else constants.AI
            symbol = 'x' if symbol == 'o' else 'o'

            heuristic_next_node = minimax_decision(board_matrix_copy, blank_spaces_copy, is_max, symbol, player)

            if(heuristic_value == None):
                heuristic_value = heuristic_next_node
            else:
                if(is_max != constants.AI):
                    heuristic_value = heuristic_next_node if heuristic_next_node < heuristic_value else heuristic_value
                else:
                    heuristic_value = heuristic_next_node if heuristic_next_node > heuristic_value else heuristic_value

            

    #Ver como implementar a questão da position e o retorno final, testar em casa.
    pass


def get_board_blank_spaces(board_matrix):
    blank_spaces = []
    for i in range(3):
        for j in range(3):
            if(board_matrix[i][j] == '-'):
                blank_spaces.append(
                    {
                        'row': i,
                        'col': j,
                        'symbol': '-'
                    }
                )
    
    return blank_spaces

def execute_ai_actions(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, best_possible_move, board_lines_color):
    ai_quadrant = get_ai_quadrant(best_possible_move)
    board_helper.draw_symbol(pygame, display_surface, generic_player_handler, True, ai_quadrant, None, board_lines_color)
    game_helper.fill_board_matrix(board_helper.drawed_symbols, True, ai_quadrant, None)
    grid_quadrants[ai_quadrant][constants.IS_FILLED] = True
    game_helper.search_for_winner(game_state_handler, grid_quadrants, board_helper.drawed_symbols)

def minimax_decision(generic_player_handler, board_matrix_clone, is_max, symbol) -> int:
    winner = check_winner(board_matrix_clone, symbol)
    best_score_minimax = 0

    return best_score_minimax

def get_ai_quadrant(best_possible_move) -> str:
    quadrant = constants.FIRST_QUADRANT

    if (best_possible_move[constants.ROW_POSITION] == 0 and best_possible_move[constants.COLUMN_POSITION] == 0):
        pass
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
    winning_result = 1

    if (game_helper.check_winning_scenarios(board_matrix_clone, symbol)):
        pass
    elif (numpy.count_nonzero(board_matrix_clone == '-') == 0):
        winning_result = 0
    else:
        winning_result = -1
    return winning_result
