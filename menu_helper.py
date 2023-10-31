import board_helper
import constants

def handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color, generic_player_handler):
    display_surface.fill(pygame.Color('white'))
    if (game_state_handler[constants.START_MENU][constants.STATE] == True):
        draw_start_menu(pygame, display_surface, board_lines_color)
    elif (game_state_handler[constants.RUNNING][constants.STATE] == True):
        board_helper.draw_board(pygame, display_surface, display_surface_width, display_surface_height, board_lines_color)
    elif (game_state_handler[constants.ENDED][constants.STATE] == True):
        draw_end_game_menu(pygame, display_surface, board_lines_color, game_state_handler, generic_player_handler)

def draw_start_menu(pygame, display_surface, board_lines_color):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Tic-Tac-Toe', 1, board_lines_color), (150, 180))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press space to initialize.', 1, board_lines_color), (60, 250))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow up to let the AI start playing!', 1, board_lines_color), (60, 280))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow down to start playing!', 1, board_lines_color), (60, 310))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow left to draw "o"/', 1, board_lines_color), (60, 340))
    display_surface.blit(pygame.font.SysFont('comicsans', 15).render('Press arrow right to draw "x"', 1, board_lines_color), (265, 340))

def draw_end_game_menu(pygame, display_surface, board_lines_color, game_state_handler, generic_player_handler):
    display_surface.blit(pygame.font.SysFont('comicsans', 35).render('Game ended!', 1, board_lines_color), (150, 180))
    display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Press space to replay.', 1, board_lines_color), (150, 240))

    if (game_state_handler[constants.ENDED][constants.END_RESULT] == constants.WIN):
        if (generic_player_handler[constants.MOMENT_PLAYER] == constants.AI):
            display_surface.blit(pygame.font.SysFont('comicsans', 20).render('AI is the winner!', 1, board_lines_color), (150, 280))
        else:
            display_surface.blit(pygame.font.SysFont('comicsans', 20).render('Player is the winner!', 1, board_lines_color), (150, 280))
    else:
        display_surface.blit(pygame.font.SysFont('comicsans', 20).render("It's a tie!", 1, board_lines_color), (150, 280))
