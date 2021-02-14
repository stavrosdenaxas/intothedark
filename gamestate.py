import pygame
import pygame.freetype
import hero
import flora
import projectile
import inputcapture
import enemy
import forestlevel

# set screen resolution variables, this should be customisable in future
screen_width = 1920
screen_height = 1080
all_sprites = pygame.sprite.Group()
all_level_sprites = pygame.sprite.Group()
game_area = pygame.Rect(60, 60, screen_width, screen_height)


class Gamestate:
    def __init__(self):

        self.state = 'title_screen'
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.background_surface = pygame.Surface([screen_width, screen_height])
        self.running = True
        self.level = "none"
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)
        self.DIAGNOSTICS_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 12)
        # create a sprite group to hold all sprites

        # create our first game objects/sprites as a test
        self.hero = hero.Hero()
        self.bonzai_tree1 = flora.Flora()
        for x in range(20):
            all_sprites.add(enemy.Enemy(self.hero, game_area))

        # add all sprites to the group
        all_sprites.add(self.hero)
        all_sprites.add(self.bonzai_tree1)

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
        self.screen.fill((0, 0, 0))
        inputcapture.next_screen_check_input(self)
        # check character input
        inputcapture.character_check_input(self.hero)

        if self.level == "none":
            # self.level == "forest"
            forest_level = forestlevel.ForestLevel(self.screen)

        # move or animate our test sprites
        for obj in all_sprites:
            if isinstance(obj, hero.Hero):
                obj.hit(all_sprites)
            if isinstance(obj, flora.Flora):
                obj.animate()
            if isinstance(obj, projectile.Projectile):
                obj.move()
                obj.hit(all_sprites)
            if isinstance(obj, enemy.Enemy):
                obj.move()


        # draw all sprites
        # all_level_sprites.draw(self.screen)
        all_sprites.draw(self.screen)

        if self.hero.is_dead and self.hero.current_sprite == 4:
            pygame.quit()

        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10,30), "FPS:" + str(round(clock.get_fps())),(150, 150, 150))
        # Flip the display ( update the display)
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 30), "Len:" + str(len(all_level_sprites)), (150, 150, 150))
        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "Len:" + str(len(all_level_sprites)), (150, 150, 150))
        pygame.display.flip()
