import pygame


def character_check_input(character):
    # probably need to pass character as input to update when needed
    character.move(pygame.mouse.get_pos())
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
