def draw_board(pygame, display_surface, display_surface_width, display_surface_height):
    board_lines_color = pygame.Color('black')

    # Board vertical lines
    pygame.draw.line(display_surface, board_lines_color, (display_surface_width / 3, 0), (display_surface_width / 3, display_surface_height), 7)
    pygame.draw.line(display_surface, board_lines_color, (display_surface_width / 3 * 2, 0), (display_surface_width / 3 * 2, display_surface_height), 7)

    # Board horizontal lines
    pygame.draw.line(display_surface, board_lines_color, (0, display_surface_height / 3), (display_surface_width, display_surface_height / 3), 7)
    pygame.draw.line(display_surface, board_lines_color, (0, display_surface_height / 3 * 2), (display_surface_width, display_surface_height / 3 * 2), 7)

def handle_player_action(pygame, display_surface, grid_quadrants):
    mouse_position = mouse_listener(pygame)

    if (mouse_position != 0):
        for quadrant in grid_quadrants.items():
            if ((mouse_position[0] >= quadrant[1]['position'][0] and mouse_position[0] <= quadrant[1]['position'][2]) \
                and (mouse_position[1] >= quadrant[1]['position'][1] and mouse_position[1] <= quadrant[1]['position'][3])):
                    if (quadrant[1]['is_filled'] == False):
                        quadrant[1]['is_filled'] = True
                        draw_x_symbol(pygame, display_surface, quadrant)
                        print(quadrant[1]['is_filled'])
                        print(quadrant[0])
                        print(mouse_position)

def mouse_listener(pygame):
    mouse_pressed = pygame.mouse.get_pressed()

    if(mouse_pressed[0] == True):
        return pygame.mouse.get_pos()

    return 0

def draw_x_symbol(pygame, display_surface, quadrant):
    pygame.draw.line(display_surface, 'black', (quadrant[1]['position'][0], quadrant[1]['position'][2]), (quadrant[1]['position'][1], quadrant[1]['position'][3]), 10)
