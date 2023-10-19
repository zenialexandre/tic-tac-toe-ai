import constants
import numpy

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
