import pygame
import board_helper
import menu_helper
import game_helper
import ai
import constants

pygame.init()

game_icon = pygame.image.load(r'tic_tac_toe_icon.png')
board_lines_color = pygame.Color('black')
pygame.display.set_caption('tic-tac-toe-ai')
pygame.display.set_icon(game_icon)
display_surface = pygame.display.set_mode((512, 512))
display_surface.fill(pygame.Color('white'))
display_surface_width, display_surface_height = display_surface.get_size()

game_state_handler = {
    constants.START_MENU: {
        constants.STATE: True
    },
    constants.RUNNING: {
        constants.STATE: False
    },
    constants.ENDED: {
        constants.STATE: False,
        constants.END_RESULT: constants.TIE
    },
}

generic_player_handler = {
    constants.MOMENT_PLAYER: constants.PLAYER,
    constants.MAX_PLAYER: constants.PLAYER,
    constants.CURRENT_SYMBOL: constants.X_SYMBOL
}

grid_quadrants = {
    constants.FIRST_QUADRANT: {
        constants.POSITION: [0, 0, 150, 150],
        constants.IS_FILLED: False
    },
    constants.SECOND_QUADRANT: {
        constants.POSITION: [180, 0, 330, 150],
        constants.IS_FILLED: False
    },
    constants.THIRD_QUADRANT: {
        constants.POSITION: [360, 0, 512, 150],
        constants.IS_FILLED: False
    },
    constants.FOURTH_QUADRANT: {
        constants.POSITION: [0, 180, 150, 330],
        constants.IS_FILLED: False
    },
    constants.FIFTH_QUADRANT: {
        constants.POSITION: [180, 180, 330, 330],
        constants.IS_FILLED: False
    },
    constants.SIXTH_QUADRANT: {
        constants.POSITION: [360, 180, 512, 330],
        constants.IS_FILLED: False
    },
    constants.SEVENTH_QUADRANT: {
        constants.POSITION: [0, 360, 150, 512],
        constants.IS_FILLED: False
    },
    constants.EIGHTH_QUADRANT: {
        constants.POSITION: [180, 360, 330, 512],
        constants.IS_FILLED: False
    },
    constants.NINTH_QUADRANT: {
        constants.POSITION: [360, 360, 512, 512],
        constants.IS_FILLED: False
    },
}

def handle_game_events(pygame, game_state_handler, generic_player_handler, display_surface, display_surface_width, display_surface_height, grid_quadrants, board_lines_color):
    if (event.type == pygame.QUIT):
        pygame.quit()
        quit()
    elif (game_state_handler[constants.START_MENU][constants.STATE] == True or game_state_handler[constants.ENDED][constants.STATE] == True):
        handle_game_configuration_event(pygame, event, generic_player_handler)
        default_play_process(pygame, event, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color, generic_player_handler)
    elif (game_state_handler[constants.RUNNING][constants.STATE] == True):
        if (event.type == pygame.MOUSEBUTTONDOWN and generic_player_handler[constants.MOMENT_PLAYER] == constants.PLAYER):
            board_helper.handle_player_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color)
            generic_player_handler[constants.MOMENT_PLAYER] = constants.AI

            if (game_state_handler[constants.ENDED][constants.STATE] == True):
                generic_player_handler[constants.MOMENT_PLAYER] = constants.PLAYER
                generic_player_handler[constants.MAX_PLAYER] = constants.PLAYER
        elif (generic_player_handler[constants.MOMENT_PLAYER] == constants.AI):
            ai.handle_ai_action(pygame, display_surface, game_state_handler, generic_player_handler, grid_quadrants, board_lines_color)
            generic_player_handler[constants.MOMENT_PLAYER] = constants.PLAYER

            if (game_state_handler[constants.ENDED][constants.STATE] == True):
                generic_player_handler[constants.MOMENT_PLAYER] = constants.AI
                generic_player_handler[constants.MAX_PLAYER] = constants.AI

def handle_game_configuration_event(pygame, event, generic_player_handler):
    if (game_state_handler[constants.START_MENU][constants.STATE] == True):
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            generic_player_handler[constants.MOMENT_PLAYER] = constants.AI
            generic_player_handler[constants.MAX_PLAYER] = constants.AI
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            generic_player_handler[constants.MOMENT_PLAYER] = constants.PLAYER
            generic_player_handler[constants.MAX_PLAYER] = constants.PLAYER
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            generic_player_handler[constants.CURRENT_SYMBOL] = constants.O_SYMBOL
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            generic_player_handler[constants.CURRENT_SYMBOL] = constants.X_SYMBOL

def default_play_process(pygame, event, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color, generic_player_handler):
    menu_helper.handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color, generic_player_handler)
    if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
        if (game_state_handler[constants.START_MENU][constants.STATE] == True):
            game_helper.modify_game_state(game_state_handler, False, True, False)
        else:
            game_helper.modify_game_state(game_state_handler, True, False, False)

        menu_helper.handle_drawing(pygame, game_state_handler, display_surface, display_surface_width, display_surface_height, board_lines_color, generic_player_handler)

while True:
    for event in pygame.event.get():
        handle_game_events(pygame, game_state_handler, generic_player_handler,
            display_surface, display_surface_width, display_surface_height, grid_quadrants, board_lines_color)
        pygame.display.update()
