import numpy
import constants

board_matrix = numpy.array(
    [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
)

def fill_board_matrix(drawed_symbols, quadrant):
    if (quadrant[0] == constants.FIRST_QUADRANT):
        board_matrix[0][0] = drawed_symbols[-1]
    elif (quadrant[0] == constants.SECOND_QUADRANT):
        board_matrix[0][1] = drawed_symbols[-1]
    elif (quadrant[0] == constants.THIRD_QUADRANT):
        board_matrix[0][2] = drawed_symbols[-1]
    elif (quadrant[0] == constants.FOURTH_QUADRANT):
        board_matrix[1][0] = drawed_symbols[-1]
    elif (quadrant[0] == constants.FIFTH_QUADRANT):
        board_matrix[1][1] = drawed_symbols[-1]
    elif (quadrant[0] == constants.SIXTH_QUADRANT):
        board_matrix[1][2] = drawed_symbols[-1]
    elif (quadrant[0] == constants.SEVENTH_QUADRANT):
        board_matrix[2][0] = drawed_symbols[-1]
    elif (quadrant[0] == constants.EIGHTH_QUADRANT):
        board_matrix[2][1] = drawed_symbols[-1]
    else:
        board_matrix[2][2] = drawed_symbols[-1]

def search_for_winner(game_state_handler, grid_quadrants, drawed_symbols):
    if (check_winning_scenarios(None, constants.X_SYMBOL) == True or check_winning_scenarios(None, constants.O_SYMBOL) == True):
        end_game_state_transition(game_state_handler, grid_quadrants, drawed_symbols)
    elif (numpy.count_nonzero(board_matrix == '-') == 0):
        end_game_state_transition(game_state_handler, grid_quadrants, drawed_symbols)

def check_winning_scenarios(board_matrix_clone, symbol) -> bool:
    board_matrix_internal = board_matrix if (board_matrix_clone is None) else board_matrix_clone

    return check_row_winning_scenarios(board_matrix_internal, symbol) == True \
        or check_column_winning_scenarios(board_matrix_internal, symbol) == True \
        or check_crossed_winning_scenarios(board_matrix_internal, symbol) == True

def check_row_winning_scenarios(board_matrix_internal, symbol) -> bool:
    return (board_matrix_internal[0][0] == symbol and board_matrix_internal[0][1] == symbol and board_matrix_internal[0][2] == symbol) \
        or (board_matrix_internal[1][0] == symbol and board_matrix_internal[1][1] == symbol and board_matrix_internal[1][2] == symbol) \
        or (board_matrix_internal[2][0] == symbol and board_matrix_internal[2][1] == symbol and board_matrix_internal[2][2] == symbol)

def check_column_winning_scenarios(board_matrix_internal, symbol) -> bool:
    return (board_matrix_internal[0][0] == symbol and board_matrix_internal[1][0] == symbol and board_matrix_internal[2][0] == symbol) \
        or (board_matrix_internal[0][1] == symbol and board_matrix_internal[1][1] == symbol and board_matrix_internal[2][1] == symbol) \
        or (board_matrix_internal[0][2] == symbol and board_matrix_internal[1][2] == symbol and board_matrix_internal[2][2] == symbol)

def check_crossed_winning_scenarios(board_matrix_internal, symbol) -> bool:
    return (board_matrix_internal[0][0] == symbol and board_matrix_internal[1][1] == symbol and board_matrix_internal[2][2] == symbol) \
        or (board_matrix_internal[0][2] == symbol and board_matrix_internal[1][1] == symbol and board_matrix_internal[2][0] == symbol)

def modify_game_state(game_state_handler, start_menu_state, running_state, ended_state):
    game_state_handler[constants.START_MENU][constants.STATE] = start_menu_state
    game_state_handler[constants.RUNNING][constants.STATE] = running_state
    game_state_handler[constants.ENDED][constants.STATE] = ended_state

def end_game_state_transition(game_state_handler, grid_quadrants, drawed_symbols):
    global board_matrix

    modify_game_state(game_state_handler, False, False, True)
    clean_filled_quadrants(grid_quadrants)
    board_matrix = numpy.full((3, 3), '-')
    drawed_symbols.clear()

def clean_filled_quadrants(grid_quadrants):
    for quadrant in grid_quadrants.items():
        if (quadrant[1][constants.IS_FILLED] == True):
            quadrant[1][constants.IS_FILLED] = False
