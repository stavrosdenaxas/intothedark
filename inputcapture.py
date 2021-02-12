import pygame
import gamestate
import projectile


# checks if right mouse click is pressed and updates the character mouse position
def character_check_input(character):
    if pygame.mouse.get_pressed(3)[2]:
        character.mouse_position = pygame.mouse.get_pos()
        character.is_moving = True

    if pygame.mouse.get_pressed(3)[0]:
        gamestate.all_sprites.add(projectile.Projectile(pygame.mouse.get_pos(), gamestate.game_area, character))


# checks to see if any key is pressed to switch between title, menu and game screens. Should be changed to change on
# click of menu item
def next_screen_check_input(gamestate):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if gamestate.state == 'title_screen':
                gamestate.state = 'main_menu'
            elif gamestate.state == 'main_menu':
                gamestate.state = 'main_game'


# checks to see if user clicks X on top right of window and stops game **NOT CURRENTLY WORKING**
def quit_check_input(gamestate):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamestate.running = False
