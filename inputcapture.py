import pygame
from pygame.math import Vector2
import gamestate
import projectile


# checks if right mouse click is pressed and updates the character mouse position
def character_check_input(character):
    move = Vector2()
    event = pygame.key.get_pressed()
    if event[pygame.K_w]:
        move += (0, -3)
    if event[pygame.K_a]:
        move += (-3, 0)
    if event[pygame.K_s]:
        move += (0, 3)
    if event[pygame.K_d]:
        move += (3, 0)
    if move.length() > 0:
        move.normalize_ip()

    character.velocity = move * 3
    character.move()
    # if pygame.mouse.get_pressed(3)[2]:
    #   character.mouse_position = pygame.mouse.get_pos()
    #   character.is_moving = True
    if pygame.mouse.get_pressed(3)[0]:
        print(pygame.time.get_ticks())
        if character.projectile_count >= 10 \
                or pygame.time.get_ticks() - character.projectile_fired_time < character.fire_rate:
            return
        else:
            gamestate.all_sprites.add(projectile.Projectile(pygame.mouse.get_pos(), gamestate.game_area, character))
            character.projectile_count += 1
            character.projectile_fired_time = pygame.time.get_ticks()


# checks to see if any key is pressed to switch between title, menu and game screens. Should be changed to change on
# click of menu item
def next_screen_check_input(gamest):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if gamest.state == 'title_screen':
                gamest.state = 'main_menu'
            elif gamest.state == 'main_menu':
                gamest.state = 'main_game'


# checks to see if user clicks X on top right of window and stops game **NOT CURRENTLY WORKING**
def quit_check_input(gamest):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamest.running = False
