import pygame

pygame.init() 
white = (255, 255, 255)

background_game = pygame.image.load(r'background_jogo_da_velha.png') 
x_game = pygame.image.load(r'xis_jogo_da_velha.png') 
y_game = pygame.image.load(r'bolinhadegolf_jogo_da_velha.png')

pygame.display.set_caption('Jogo da Velha')

quadrantes = {
    'primerio': {
        'position': [0,0,150,150],
        'is_filled': False
    },
    'segundo': {
        'position': [180,0,330,150],
        'is_filled': False
    },
    'terceiro': {
        'position': [360,0,512,150],
        'is_filled': False
    },
    'quarto': {
        'position': [0,180,150,330],
        'is_filled': False
    },
    'quinto': {
        'position': [180,180,330,330],
        'is_filled': False
    },
    'sexto': {
        'position': [360,180,512,330],
        'is_filled': False
    },
    'setimo': {
        'position': [0,360,150,512],
        'is_filled': False
    },
    'oitavo': {
        'position': [180,360,330,512],
        'is_filled': False
    },
    'nono': {
        'position': [360,360,512,512],
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

    if(mouse_position != 0):
        for quadrante in dict_quadrantes.items():
            if((mouse_position[0] >= quadrante[1]['position'][0] and mouse_position[0] <= quadrante[1]['position'][2]) \
            and (mouse_position[1] >= quadrante[1]['position'][1] and mouse_position[1] <= quadrante[1]['position'][3])):
                    if(quadrante[1]['is_filled'] == False):
                        quadrante[1]['is_filled'] = True
                        print(quadrante[1]['is_filled'])
                        print(quadrante[0])
                        print(mouse_position)
                                        

while True:
    display_surface.fill(white)
    display_surface.blit(background_game, (0, 0)) 

    action_x_o(quadrantes)

    for event in pygame.event.get() : 
      
        if event.type == pygame.QUIT : 
            pygame.quit() 
            quit() 
        
        pygame.display.update() 


    '''


    ''' 