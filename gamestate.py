import pygame
import pygame.freetype
from pygame.math import Vector2

import hero
import enemy
import flora
import projectile
import inputcapture
import forestlevel

# set screen resolution variables, this should be customisable in future
screen_width = 1920
screen_height = 1080
all_sprites = pygame.sprite.Group()
game_area = pygame.Rect(0, 0, screen_width, screen_height)


class Gamestate:
    def __init__(self):

        self.state = 'title_screen'
        self.camera = Vector2(0, 0)
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.background_surface = pygame.Surface([screen_width, screen_height])

        self.running = True
        self.level = "Forest"
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)
        self.DIAGNOSTICS_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 12)
        # create a sprite group to hold all sprites

        # create our first game objects/sprites as a test
        self.hero = hero.Hero()

        # add all sprites to the group
        all_sprites.add(self.hero)
        self.forest_level = forestlevel.ForestLevel(all_sprites, self.hero, game_area)

    # method called when in title screen to render
    def title_screen(self):

        inputcapture.next_screen_check_input(self)
        # Did the user click the window close button?

        # Fill the background with black
        self.screen.fill((0, 0, 0))
        # put title on screen
        self.GAME_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height / 2 - 0.1 * screen_width)),
                                 "Into the Dark",
                                 (100, 100, 100))
        pygame.display.flip()

    def main_menu(self):
        inputcapture.next_screen_check_input(self)
        # Did the user click the window close button?
        # Fill the background with black
        self.screen.fill((0, 0, 0))

        # Draw a solid blue circle in the center
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.4 - 0.1 * screen_width)),
                                 "Enter the Darkness",
                                 (100, 100, 100))
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.55 - 0.1 * screen_width)),
                                 "Options",
                                 (100, 100, 100))
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.7 - 0.1 * screen_width)),
                                 "Credits",
                                 (100, 100, 100))
        pygame.display.flip()

    def menu_options(self):
        # placeholder for options menu
        return

    def menu_credits(self):
        # placeholder for credits showcase
        return

    def main_game(self, clock):
        # Fill the background with black
        # self.screen.fill((0, 0, 0))
        inputcapture.next_screen_check_input(self)
        # check character input
        inputcapture.hero_check_input(self.hero)

        if self.level == "Forest":
            self.forest_level.draw(self.screen, self.hero.camera)

        # move or animate our test sprites
        for obj in all_sprites:
            if isinstance(obj, hero.Hero):
                obj.hit(all_sprites)
                obj.update()
            if isinstance(obj, flora.Flora):
                obj.update()
            if isinstance(obj, projectile.Projectile):
                obj.update()
                obj.hit(all_sprites)
            if isinstance(obj, enemy.Enemy):
                obj.update()

        # draw all sprites
        # all_level_sprites.draw(self.screen)
        for sprite in all_sprites:
            self.screen.blit(sprite.image, Vector2(sprite.rect.x, sprite.rect.y) + self.hero.camera)

        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10,30), "FPS:" + str(round(clock.get_fps())),(150, 150, 150))
        # Flip the display ( update the display)
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 30), "Len:" + str(len(all_sprites)), (150, 150, 150))
        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "Len:" + str(len(all_level_sprites)), (150, 150, 150))
        pygame.display.flip()
