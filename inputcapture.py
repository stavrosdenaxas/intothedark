import pygame


def character_check_input(character):
    if pygame.mouse.get_pressed(3)[0]:
        character.mouse_position = pygame.mouse.get_pos()
        print(pygame.mouse.get_pos())
        print(character.mouse_position)
        character.is_moving = True


    return "placeholder"


def next_screen_check_input(gamestate):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if gamestate.state == 'title_screen':
                gamestate.state = 'main_menu'
            elif gamestate.state == 'main_menu':
                gamestate.state = 'main_game'


def quit_check_input(gamestate):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestate.running = False
