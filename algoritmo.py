#!/usr/bin/env python3
from math import inf as infinity
from random import choice
import platform
import time
from os import system

human = -1
ai = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def evaluate(condition):
    if wins(condition, ai):
        score = +1
    elif wins(condition, human):
        score = -1
    else:
        score = 0

    return score


def wins(condition, player):
    """
    This function tests if a specific player wins. Possibilities:
    * Three rows    [X X X] or [O O O]
    * Three cols    [X X X] or [O O O]
    * Two diagonals [X X X] or [O O O]
    :param condition: the condition of the current board
    :param player: a human or a aiuter
    :return: True if the player wins
    """
    win_condition = [
        [condition[0][0], condition[0][1], condition[0][2]],
        [condition[1][0], condition[1][1], condition[1][2]],
        [condition[2][0], condition[2][1], condition[2][2]],
        [condition[0][0], condition[1][0], condition[2][0]],
        [condition[0][1], condition[1][1], condition[2][1]],
        [condition[0][2], condition[1][2], condition[2][2]],
        [condition[0][0], condition[1][1], condition[2][2]],
        [condition[2][0], condition[1][1], condition[0][2]],
    ]
    if [player, player, player] in win_condition:
        return True
    else:
        return False


def game_over(condition):
    """
    This function test if the human or aiuter wins
    :param condition: the condition of the current board
    :return: True if the human or aiuter wins
    """
    return wins(condition, human) or wins(condition, ai)


def empty_cells(condition):
    """
    Each empty cell will be added into cells' list
    :param condition: the condition of the current board
    :return: a list of empty cells
    """
    cells = []

    for x, row in enumerate(condition):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells


def valid_move(x, y):
    """
    A move is valid if the chosen cell is empty
    :param x: X coordinate
    :param y: Y coordinate
    :return: True if the board[x][y] is empty
    """
    if [x, y] in empty_cells(board):
        return True
    else:
        return False


def set_move(x, y, player):
    """
    Set the move on board, if the coordinates are valid
    :param x: X coordinate
    :param y: Y coordinate
    :param player: the current player
    """
    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False


def minimax(condition, depth, player):
    """
    AI function that choice the best move
    :param condition: current condition of the board
    :param depth: node index in the tree (0 <= depth <= 9),
    but never nine in this case (see iaturn() function)
    :param player: an human or a aiuter
    :return: a list with [the best row, best col, best score]
    """
    if player == ai:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(condition):
        score = evaluate(condition)
        return [-1, -1, score]

    for cell in empty_cells(condition):
        x, y = cell[0], cell[1]
        condition[x][y] = player
        score = minimax(condition, depth - 1, -player)
        condition[x][y] = 0
        score[0], score[1] = x, y

        if player == ai:
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value

    return best


def clean():
    """
    Clears the console
    """
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')


def render(condition, c_choice, h_choice):
    """
    Print the board on console
    :param condition: current condition of the board
    """

    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '---------------'

    print('\n' + str_line)
    for row in condition:
        for cell in row:
            symbol = chars[cell]
            print(f'| {symbol} |', end='')
        print('\n' + str_line)


def ai_turn(c_choice, h_choice):
    """
    It calls the minimax function if the depth < 9,
    else it choices a random coordinate.
    :param c_choice: aiuter's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    clean()
    print(f'aiuter turn [{c_choice}]')
    render(board, c_choice, h_choice)

    if depth == 9:
        x = choice([0, 1, 2])
        y = choice([0, 1, 2])
    else:
        move = minimax(board, depth, ai)
        x, y = move[0], move[1]

    set_move(x, y, ai)
    time.sleep(1)


def human_turn(c_choice, h_choice):
    """
    The human plays choosing a valid move.
    :param c_choice: aiuter's choice X or O
    :param h_choice: human's choice X or O
    :return:
    """
    depth = len(empty_cells(board))
    if depth == 0 or game_over(board):
        return

    # Dictionary of valid moves
    move = -1
    moves = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
    }

    clean()
    print(f'human turn [{h_choice}]')
    render(board, c_choice, h_choice)

    while move < 1 or move > 9:
        try:
            move = int(input('Use numpad (1..9): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], human)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')


def main():
    """
    Main function that calls all functions
    """
    clean()
    h_choice = ''  # X or O
    c_choice = ''  # X or O
    first = ''  # if human is the first

    # human chooses X or O to play
    while h_choice != 'O' and h_choice != 'X':
        try:
            print('')
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Setting aiuter's choice
    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    # human may starts first
    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    # Main loop of this game
    while len(empty_cells(board)) > 0 and not game_over(board):
        if first == 'N':
            ai_turn(c_choice, h_choice)
            first = ''

        human_turn(c_choice, h_choice)
        ai_turn(c_choice, h_choice)

    # Game over message
    if wins(board, human):
        clean()
        print(f'human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, ai):
        clean()
        print(f'aiuter turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

    exit()


if __name__ == '__main__':
    main()