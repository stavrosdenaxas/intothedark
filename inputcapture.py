import pygame


def main_game_check_input(character):
    # placeholder
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