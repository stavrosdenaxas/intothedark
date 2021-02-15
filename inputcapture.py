import pygame
from pygame.math import Vector2
import gamestate
import projectile
import levelicon


def hero_check_input(hero):
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
        hero.is_moving = True
    else:
        hero.is_moving = False

    hero.velocity = move
    # if pygame.mouse.get_pressed(3)[2]:
    #   character.mouse_position = pygame.mouse.get_pos()
    #   character.is_moving = True
    if pygame.mouse.get_pressed(3)[0]:
        if hero.projectile_count >= 55\
                or pygame.time.get_ticks() - hero.projectile_fired_time < hero.fire_rate or hero.is_dead == True:
            return
        else:
            gamestate.all_sprites.add(projectile.Projectile(pygame.mouse.get_pos(), gamestate.game_area, hero))
            hero.projectile_count += 1
            hero.projectile_fired_time = pygame.time.get_ticks()


# checks to see if any key is pressed to switch between title, menu and game screens. Should be changed to change on
# click of menu item
def next_screen_check_input(gamest):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if gamest.state == 'title_screen':
                gamest.state = 'main_menu'
            elif gamest.state == 'main_menu':
                forest_level_icon = levelicon.LevelIcon(2000, 1500)
                gamestate.all_sprites.add(forest_level_icon)
                gamest.state = 'game_lobby'
            # elif gamest.state == 'game_lobby':
            #    gamest.state = 'main_game'
        quit_check_input(gamest, event)


# checks to see if user clicks X on top right of window and stops game **NOT CURRENTLY WORKING**
def quit_check_input(gamest, event):
    if event.type == pygame.QUIT:
        gamest.running = False
