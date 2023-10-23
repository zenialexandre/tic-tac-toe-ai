import pygame
import board_helper
import menu_helper
import game_helper
import constants

pygame.init()

game_icon = pygame.image.load(r'tic_tac_toe_icon.png')
board_lines_color = pygame.Color('black')
game_state_handler = {
    'start_menu': {
        'state': True
    },
    'running': {
        'state': False
    },
    'ended': {
        'state': False
    }
}

pygame.display.set_caption('tic-tac-toe-ai')
pygame.display.set_icon(game_icon)
display_surface = pygame.display.set_mode((512, 512))
display_surface.fill(pygame.Color('white'))
display_surface_width, display_surface_height = display_surface.get_size()

grid_quadrants = {
    'first_quadrant': {
        'position': [0, 0, 150, 150],
        'is_filled': False
    },
    'second_quadrant': {
        'position': [180, 0, 330, 150],
        'is_filled': False
    },
    'third_quadrant': {
        'position': [360, 0, 512, 150],
        'is_filled': False
    },
    'fourth_quadrant': {
        'position': [0, 180, 150, 330],
        'is_filled': False
    },
    'fifth_quadrant': {
        'position': [180, 180, 330, 330],
        'is_filled': False
    },
    'sixth_quadrant': {
        'position': [360, 180, 512, 330],
        'is_filled': False
    },
    'seventh_quadrant': {
        'position': [0, 360, 150, 512],
        'is_filled': False
    },
    'eighth_quadrant': {
        'position': [180, 360, 330, 512],
        'is_filled': False
    },
    'ninth_quadrant': {
        'position': [360, 360, 512, 512],
        'is_filled': False
    },
}

def handle_game_events(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, grid_quadrants, board_lines_color):
    if (event.type == pygame.QUIT):
        pygame.quit()
        quit()
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and game_state_handler[constants.START_MENU][constants.STATE] == True):
        # TODO
        print('user starts playing')
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and game_state_handler[constants.START_MENU][constants.STATE] == True):
        # TODO
        print('user draws o')
    elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and game_state_handler[constants.START_MENU][constants.STATE] == True):
        # TODO
        print('users draws x')
    elif (game_state_handler[constants.START_MENU][constants.STATE] == True or game_state_handler[constants.ENDED][constants.STATE] == True):
        default_play_process(pygame, event, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color)
    elif (event.type == pygame.MOUSEBUTTONDOWN and game_state_handler[constants.RUNNING][constants.STATE] == True):
        board_helper.handle_player_action(pygame, game_state_handler, display_surface, grid_quadrants, board_lines_color)

def default_play_process(pygame, event, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color):
    menu_helper.handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color)
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
        if (game_state_handler[constants.START_MENU][constants.STATE] == True):
            game_helper.modify_game_state(game_state_handler, False, True, False)
        else:
            game_helper.modify_game_state(game_state_handler, True, False, False)

        menu_helper.handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color)

while True:
    for event in pygame.event.get():
        handle_game_events(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, grid_quadrants, board_lines_color)
        pygame.display.update()