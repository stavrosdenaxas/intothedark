import pygame
import pygame.freetype
from pygame.math import Vector2

import hero
import enemy
import flora
import item
import projectile
import inputcapture
import forestlevel
import mountainlevel
import swamplevel
import mergamothlevel
import levelicon

# set screen resolution variables, this should be customisable in future
screen_width = 1920
screen_height = 1080
all_sprites = pygame.sprite.Group()
lobby_sprites = pygame.sprite.Group()
ui_sprites = pygame.sprite.Group()
game_area = pygame.Rect(0, 0, screen_width * 4, screen_height * 4)


class Gamestate:
    def __init__(self, state):
        all_sprites.empty()
        ui_sprites.empty()
        lobby_sprites.empty()
        self.state = state
        self.camera = Vector2(0, 0)
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.background_surface = pygame.Surface([screen_width, screen_height])

        self.running = True
        self.level = "none"
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)
        self.DIAGNOSTICS_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 12)
        # create a sprite group to hold all sprites

        self.forest_level_icon = levelicon.LevelIcon(1500, 1200, "Forest")
        self.swamp_level_icon = levelicon.LevelIcon(1300, 1200, "Swamp")
        self.mountain_level_icon = levelicon.LevelIcon(1100, 1200, "Mountain")
        self.mergamoth_level_icon = levelicon.LevelIcon(1300, 800, "Mergamoth")
        lobby_sprites.add(self.forest_level_icon)
        lobby_sprites.add(self.swamp_level_icon)
        lobby_sprites.add(self.mountain_level_icon)
        lobby_sprites.add(self.mergamoth_level_icon)
        # create our first game objects/sprites as a test
        self.hero = hero.Hero(screen_width, screen_height)
        self.hero.is_moving = False
        self.hero.is_dead = False
        self.time_of_death = 100000000000000000
        # add all sprites to the group
        lobby_sprites.add(self.hero)
        self.forest_level = None
        self.mountain_level = None
        self.swamp_level = None
        self.mergamoth_level = None

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

    def game_lobby(self, clock):
        self.screen.fill((0, 0, 0))

        inputcapture.next_screen_check_input(self)
        inputcapture.hero_check_input(self)
        # forest flora

        for obj in lobby_sprites:
            if isinstance(obj, levelicon.LevelIcon):
                obj.update()
                obj.hit(lobby_sprites, self)
            if isinstance(obj, hero.Hero):
                obj.hit(lobby_sprites, ui_sprites, lobby_sprites, self)
                obj.update(lobby_sprites)
            if isinstance(obj, projectile.Projectile):
                obj.update()
                obj.hit(lobby_sprites, self)

        for sprite in sorted(lobby_sprites, key=lambda spr: spr.rect.bottom):
            self.screen.blit(sprite.image, Vector2(sprite.rect.x, sprite.rect.y) + self.hero.camera)
        for sprite in sorted(ui_sprites, key=lambda spr: spr.rect.bottom):
            self.screen.blit(sprite.image, Vector2(sprite.rect.x, sprite.rect.y))

        if self.level == "Forest":
            all_sprites.empty()
            self.forest_level = forestlevel.ForestLevel(all_sprites, self.hero, game_area)
        if self.level == "Mountain":
            all_sprites.empty()
            self.mountain_level = mountainlevel.MountainLevel(all_sprites, self.hero, game_area)
        if self.level == "Swamp":
            all_sprites.empty()
            self.swamp_level = swamplevel.SwampLevel(all_sprites, self.hero, game_area)
        if self.level == "Mergamoth":
            all_sprites.empty()
            self.mergamoth_level = mergamothlevel.MergamothLevel(all_sprites, self.hero, game_area)

        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 30), "Len:" + str(len(all_sprites)), (150, 150, 150))
        pygame.display.flip()

    def main_game(self, clock):
        # Fill the background with black
        self.screen.fill((0, 0, 0))
        inputcapture.next_screen_check_input(self)
        # check character input
        inputcapture.hero_check_input(self)

        if self.level == "Forest":
            self.forest_level.draw(self.screen, self.hero.camera)
        if self.level == "Mountain":
            self.mountain_level.draw(self.screen, self.hero.camera)
        if self.level == "Swamp":
            self.swamp_level.draw(self.screen, self.hero.camera)
        if self.level == "Mergamoth":
            self.mergamoth_level.draw(self.screen, self.hero.camera)

        # move or animate our test sprites
        for obj in all_sprites:
            if isinstance(obj, flora.Flora):
                obj.update()
            if isinstance(obj, projectile.Projectile):
                obj.update()
                obj.hit(all_sprites, self)
            if isinstance(obj, enemy.Enemy):
                obj.update(self.hero)
            if isinstance(obj, hero.Hero):
                obj.hit(all_sprites, ui_sprites, lobby_sprites, self)
                obj.update(all_sprites)
            if isinstance(obj, item.Item):
                obj.update()

        # draw all sprites sorted by y
        for sprite in sorted(all_sprites, key=lambda spr: spr.rect.bottom):
            self.screen.blit(sprite.image, Vector2(sprite.rect.x, sprite.rect.y) + self.hero.camera)
        for sprite in sorted(ui_sprites, key=lambda spr: spr.rect.bottom):
            self.screen.blit(sprite.image, Vector2(sprite.rect.x, sprite.rect.y))

        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10,30), "FPS:" + str(round(clock.get_fps())),(150, 150, 150))
        # Flip the display ( update the display)
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 30), "Len:" + str(len(all_sprites)), (150, 150, 150))
        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "Len:" + str(len(all_level_sprites)), (150, 150, 150))
        pygame.display.flip()

    def credits_screen(self, clock):
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.4 - 0.1 * screen_width)),
                                 "Stavros made this flaming pile of garbage",
                                 (100, 100, 100))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 30), "Len:" + str(len(all_sprites)), (150, 150, 150))
