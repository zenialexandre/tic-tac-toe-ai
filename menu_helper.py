import board_helper
import constants

def handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color):
    display_surface.fill(pygame.Color('white'))
    if (game_state_handler[constants.START_MENU][constants.STATE] == True):
        draw_start_menu(pygame, display_surface, board_lines_color)
    elif (game_state_handler[constants.RUNNING][constants.STATE] == True):
        board_helper.draw_board(pygame, display_surface, display_surface_width, display_surface_height, board_lines_color)
    elif (game_state_handler[constants.ENDED][constants.STATE] == True):
        draw_end_game_menu(pygame, display_surface, board_lines_color)

def draw_start_menu(pygame, display_surface, board_lines_color):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Tic-Tac-Toe', 1, board_lines_color), (150, 220))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press space to initialize.', 1, board_lines_color), (145, 280))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press arrow up to start playing!', 1, board_lines_color), (120, 320))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow left to draw "o"/', 1, board_lines_color), (60, 360))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow right to draw "x"', 1, board_lines_color), (265, 360))

def draw_end_game_menu(pygame, display_surface, board_lines_color):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Game ended!', 1, board_lines_color), (150, 220))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press space to replay.', 1, board_lines_color), (150, 280))
