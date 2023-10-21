import board_helper

def handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color):
    if (game_state_handler['start_menu']['state'] == True):
        draw_start_menu(pygame, display_surface, board_lines_color)
    elif (game_state_handler['running']['state'] == True):
        display_surface.fill(pygame.Color('white'))
        board_helper.draw_board(pygame, display_surface, display_surface_width, display_surface_height, board_lines_color)
    elif (game_state_handler['ended']['state'] == True):
        display_surface.fill(pygame.Color('white'))
        draw_end_game_menu(pygame, display_surface, board_lines_color)

def draw_start_menu(pygame, display_surface, board_lines_color):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Tic-Tac-Toe', 1, board_lines_color), (150, 220))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press space to initialize.', 1, board_lines_color), (150, 280))

def draw_end_game_menu(pygame, display_surface, board_lines_color):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Game ended!', 1, board_lines_color), (150, 220))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press space to replay.', 1, board_lines_color), (150, 280))
