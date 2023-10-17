import pygame

pygame.init()
white = (255, 255, 255)

background_game = pygame.image.load(r'tic_tac_toe_background.png')
x_game = pygame.image.load(r'tic_tac_toe_x.png')
y_game = pygame.image.load(r'tic_tac_toe_circle.png')

pygame.display.set_caption('tic-tac-toe')

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

screen_size = background_game.get_size()
display_surface = pygame.display.set_mode(screen_size)

def mouse_listener():
    mouse_pressed = pygame.mouse.get_pressed()

    if(mouse_pressed[0] == True):
        return pygame.mouse.get_pos()

    return 0

def action_x_o(dict_quadrantes):
    mouse_position = mouse_listener()

    if (mouse_position != 0):
        for quadrante in dict_quadrantes.items():
            if ((mouse_position[0] >= quadrante[1]['position'][0] and mouse_position[0] <= quadrante[1]['position'][2]) \
                and (mouse_position[1] >= quadrante[1]['position'][1] and mouse_position[1] <= quadrante[1]['position'][3])):
                    if(quadrante[1]['is_filled'] == False):
                        quadrante[1]['is_filled'] = True
                        print(quadrante[1]['is_filled'])
                        print(quadrante[0])
                        print(mouse_position)

while True:
    display_surface.fill(white)
    display_surface.blit(background_game, (0, 0))
    action_x_o(grid_quadrants)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
