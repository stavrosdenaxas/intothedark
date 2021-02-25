import pygame
from pygame.math import Vector2
import gamestate
import projectile


def hero_check_input(game_state):
    move = Vector2(0, 0)
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
        move.scale_to_length(3.0)
        game_state.hero.is_moving = True
    else:
        game_state.hero.is_moving = False

    game_state.hero.velocity = move
    # if pygame.mouse.get_pressed(3)[2]:
    #   character.mouse_position = pygame.mouse.get_pos()
    #   character.is_moving = True
    if pygame.mouse.get_pressed(3)[0]:
        if game_state.hero.projectile_count >= 55\
                or pygame.time.get_ticks() - game_state.hero.projectile_fired_time < game_state.hero.fire_rate or game_state.hero.is_dead:
            return
        else:
            if game_state.state == 'game_lobby':
                gamestate.lobby_sprites.add(projectile.Projectile(pygame.mouse.get_pos(), gamestate.game_area, game_state.hero, "hero"))
                game_state.hero.projectile_fired_time = pygame.time.get_ticks()
            if game_state.state == 'main_game':
                gamestate.all_sprites.add(projectile.Projectile(pygame.mouse.get_pos(), gamestate.game_area, game_state.hero, "hero"))
                game_state.hero.projectile_count += 1
                game_state.hero.projectile_fired_time = pygame.time.get_ticks()


# checks to see if any key is pressed to switch between title, menu and game screens. Should be changed to change on
# click of menu item
def next_screen_check_input(gamest):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if gamest.state == 'title_screen':
                gamest.state = 'main_menu'
            elif gamest.state == 'main_menu':
                gamest.state = 'game_lobby'
            # elif gamest.state == 'game_lobby':
            #    gamest.state = 'main_game'
        quit_check_input(gamest, event)


# checks to see if user clicks X on top right of window and stops game **NOT CURRENTLY WORKING**
def quit_check_input(gamest, event):
    if event.type == pygame.QUIT:
        gamest.running = False
