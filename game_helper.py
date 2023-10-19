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

def search_for_winner():
    if (check_winning_scenarios('x') == True or check_winning_scenarios('o') == True):
        print('winner')

def check_winning_scenarios(symbol):
    return check_row_winning_scenarios(symbol) == True or check_column_winning_scenarios(symbol) == True \
        or check_crossed_winning_scenarios(symbol) == True

def check_row_winning_scenarios(symbol):
    return (board_matrix[0][0] == symbol and board_matrix[0][1] == symbol and board_matrix[0][2] == symbol) \
        or (board_matrix[1][0] == symbol and board_matrix[1][1] == symbol and board_matrix[1][2] == symbol) \
        or (board_matrix[2][0] == symbol and board_matrix[2][1] == symbol and board_matrix[2][2] == symbol)

def check_column_winning_scenarios(symbol):
    return (board_matrix[0][0] == symbol and board_matrix[1][0] == symbol and board_matrix[2][0] == symbol) \
        or (board_matrix[0][1] == symbol and board_matrix[1][1] == symbol and board_matrix[2][1] == symbol) \
        or (board_matrix[0][2] == symbol and board_matrix[1][2] == symbol and board_matrix[2][2] == symbol)

def check_crossed_winning_scenarios(symbol):
    return (board_matrix[0][0] == symbol and board_matrix[1][1] == symbol and board_matrix[2][2] == symbol) \
        or (board_matrix[0][2] == symbol and board_matrix[1][1] == symbol and board_matrix[2][0] == symbol)
