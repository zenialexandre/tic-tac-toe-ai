import math
import copy
import numpy
import game_helper
import board_helper
import constants
from random import randint

def handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    board_matrix_clone = copy.deepcopy(game_helper.board_matrix)

    if(len(board_helper.drawed_symbols) == 0):
        symbol = generic_player_handler[constants.CURRENT_SYMBOL]
    else:
        symbol = board_helper.drawed_symbols[-1]
        symbol = 'x' if symbol == 'o' else 'o'

    is_max = constants.AI if generic_player_handler[constants.MAX_PLAYER] == constants.AI else constants.PLAYER 
    
    blank_spaces = get_board_blank_spaces(board_matrix_clone)

    print(symbol)
    print(is_max)
    print(blank_spaces)

    heuristic, best_possible_move = minimax_decision(board_matrix_clone, blank_spaces, is_max, symbol, constants.AI)

    print(heuristic)
    print(best_possible_move)

    if(best_possible_move[constants.ROW_POSITION] == -1):
        min_col = math.inf
        max_col = -math.inf
        min_row = math.inf
        max_row = -math.inf

        for space in blank_spaces:
            if(space['col'] < min_col):
                min_col = space['col']
            
            if(space['row'] < min_row):
                min_row = space['row']

            if(space['col'] > max_col):
                max_col = space['col']
            
            if(space['row'] > max_row):
                max_row = space['row']

        print(best_possible_move)
        best_possible_move[constants.COLUMN_POSITION] = randint(min_col, max_col)
        best_possible_move[constants.ROW_POSITION] = randint(min_row, max_row)

    execute_ai_actions(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, best_possible_move, board_lines_color)

def minimax_decision(board_matrix, blank_spaces, is_max, symbol, player) -> dict:
    heuristic_value = None
    position = None
    blank_spaces_copy = copy.deepcopy(blank_spaces)
    board_matrix_copy = copy.deepcopy(board_matrix)

    for index, space in enumerate(blank_spaces_copy):
        if(space['symbol'] == '-'):
            space['symbol'] = symbol
            board_matrix_copy[space['row']][space['col']] = symbol

            if(game_helper.check_winning_scenarios(board_matrix_copy, symbol)):
                if(player == constants.PLAYER and is_max == constants.AI):
                    return -1, {constants.ROW_POSITION: -1, constants.COLUMN_POSITION: -1}
                elif(player == constants.PLAYER):
                    return 1, {constants.ROW_POSITION: -1, constants.COLUMN_POSITION: -1}
                elif(constants.AI == is_max):
                    return 1, {constants.ROW_POSITION : space['row'], constants.COLUMN_POSITION: space['col']}
                else:
                    return -1, {constants.ROW_POSITION: space['row'], constants.COLUMN_POSITION: space['col']}

            if(game_helper.check_terminal_state(board_matrix_copy)):
                return 0, {constants.ROW_POSITION: -1, constants.COLUMN_POSITION: -1} 

            heuristic_next_node, position_next_node = minimax_decision(board_matrix_copy, 
                                                                       blank_spaces_copy, 
                                                                       is_max, 
                                                                       'x' if symbol == 'o' else 'o', 
                                                                       constants.PLAYER if player == constants.AI else constants.AI)

            if(heuristic_value == None):
                heuristic_value = heuristic_next_node
                position = position_next_node
            else:
                if(is_max == constants.AI):
                    if(heuristic_next_node > heuristic_value):
                        heuristic_value = heuristic_next_node
                        position = position_next_node
                else:
                    if(heuristic_next_node < heuristic_value):
                        heuristic_value = heuristic_next_node
                        position = position_next_node

            if(index != len(blank_spaces_copy)):
                space['symbol'] = '-'
                board_matrix_copy[space['row']][space['col']] = '-'

    return heuristic_value, position

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
