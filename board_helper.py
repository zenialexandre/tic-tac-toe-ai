import game_helper
import constants

drawed_symbols = []

def draw_board(pygame, display_surface, display_surface_width, display_surface_height, board_lines_color):
    # Board vertical lines
    pygame.draw.line(display_surface, board_lines_color, (display_surface_width / 3, 0), (display_surface_width / 3, display_surface_height), 7)
    pygame.draw.line(display_surface, board_lines_color, (display_surface_width / 3 * 2, 0), (display_surface_width / 3 * 2, display_surface_height), 7)

    # Board horizontal lines
    pygame.draw.line(display_surface, board_lines_color, (0, display_surface_height / 3), (display_surface_width, display_surface_height / 3), 7)
    pygame.draw.line(display_surface, board_lines_color, (0, display_surface_height / 3 * 2), (display_surface_width, display_surface_height / 3 * 2), 7)

def handle_player_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color):
    mouse_position = mouse_listener(pygame)

    if (mouse_position != 0):
        for quadrant in grid_quadrants.items():
            if ((mouse_position[0] >= quadrant[1][constants.POSITION][0] and mouse_position[0] <= quadrant[1][constants.POSITION][2]) \
                and (mouse_position[1] >= quadrant[1][constants.POSITION][1] and mouse_position[1] <= quadrant[1][constants.POSITION][3]) \
                and (quadrant[1][constants.IS_FILLED] == False)):
                    quadrant[1][constants.IS_FILLED] = True
                    draw_symbol(pygame, display_surface, generic_player_handler, quadrant, board_lines_color)
                    game_helper.fill_board_matrix(drawed_symbols, quadrant)
                    game_helper.search_for_winner(game_state_handler, grid_quadrants, drawed_symbols)

def mouse_listener(pygame):
    return pygame.mouse.get_pos() if (pygame.mouse.get_pressed()[0] == True) else 0

def draw_symbol(pygame, display_surface, generic_player_handler, quadrant, board_lines_color):
    if (len(drawed_symbols) == 0):
        if (generic_player_handler[constants.CURRENT_SYMBOL] == constants.X_SYMBOL):
            draw_x_symbol(pygame, display_surface, quadrant, board_lines_color)
        else:
            draw_circle_symbol(pygame, display_surface, quadrant, board_lines_color)
    else:
        if (drawed_symbols[-1] == constants.X_SYMBOL):
            draw_circle_symbol(pygame, display_surface, quadrant, board_lines_color)
        else:
            draw_x_symbol(pygame, display_surface, quadrant, board_lines_color)

def draw_x_symbol(pygame, display_surface, quadrant, board_lines_color):
    drawed_symbols.append(constants.X_SYMBOL)

    if (quadrant[0] == constants.FIRST_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (10, 10), (150, 150), 7)
        pygame.draw.line(display_surface, board_lines_color, (10, 150), (150, 10), 7)
    elif (quadrant[0] == constants.SECOND_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (180, 10), (330, 150), 7)
        pygame.draw.line(display_surface, board_lines_color, (180, 150), (330, 10), 7)
    elif (quadrant[0] == constants.THIRD_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (356, 10), (508, 150), 7)
        pygame.draw.line(display_surface, board_lines_color, (356, 150), (508, 10), 7)
    elif (quadrant[0] == constants.FOURTH_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (10, 180), (150, 330), 7)
        pygame.draw.line(display_surface, board_lines_color, (150, 180), (10, 330), 7)
    elif (quadrant[0] == constants.FIFTH_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (180, 180), (330, 330), 7)
        pygame.draw.line(display_surface, board_lines_color, (180, 330), (330, 180), 7)
    elif (quadrant[0] == constants.SIXTH_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (356, 180), (508, 330), 7)
        pygame.draw.line(display_surface, board_lines_color, (356, 330), (508, 180), 7)
    elif (quadrant[0] == constants.SEVENTH_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (10, 356), (150, 508), 7)
        pygame.draw.line(display_surface, board_lines_color, (150, 356), (10, 508), 7)
    elif (quadrant[0] == constants.EIGHTH_QUADRANT):
        pygame.draw.line(display_surface, board_lines_color, (180, 356), (330, 508), 7)
        pygame.draw.line(display_surface, board_lines_color, (180, 508), (330, 356), 7)
    else:
        pygame.draw.line(display_surface, board_lines_color, (352, 356), (504, 508), 7)
        pygame.draw.line(display_surface, board_lines_color, (352, 508), (504, 356), 7)

def draw_circle_symbol(pygame, display_surface, quadrant, board_lines_color):
    drawed_symbols.append(constants.O_SYMBOL)

    if (quadrant[0] == constants.FIRST_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (76, 80), 50, 5)
    elif (quadrant[0] == constants.SECOND_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (250, 80), 50, 5)
    elif (quadrant[0] == constants.THIRD_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (420, 80), 50, 5)
    elif (quadrant[0] == constants.FOURTH_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (76, 260), 50, 5)
    elif (quadrant[0] == constants.FIFTH_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (250, 260), 50, 5)
    elif (quadrant[0] == constants.SIXTH_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (420, 260), 50, 5)
    elif (quadrant[0] == constants.SEVENTH_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (76, 430), 50, 5)
    elif (quadrant[0] == constants.EIGHTH_QUADRANT):
        pygame.draw.circle(display_surface, board_lines_color, (250, 430), 50, 5)
    else:
        pygame.draw.circle(display_surface, board_lines_color, (420, 430), 50, 5)
