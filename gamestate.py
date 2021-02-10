import pygame
import pygame.freetype
import character
import flora
import inputcapture

# set screen resolution variables, this should be customisable in future
screen_width = 1920
screen_height = 1080


class Gamestate:
    def __init__(self):

        self.state = 'title_screen'
        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.running = True
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)
        self.DIAGNOSTICS_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 12)

        # create a sprite group to hold all sprites
        self.all_sprites = pygame.sprite.Group()

        # create our first game objects/sprites as a test
        self.bonzai_tree1 = flora.Flora()
        self.bonzai_tree2 = flora.Flora()
        self.bonzai_tree3 = flora.Flora()
        self.mainCharacter = character.Character()

        # add all sprites to the group
        self.all_sprites.add(self.mainCharacter)
        self.all_sprites.add(self.bonzai_tree1)
        self.all_sprites.add(self.bonzai_tree2)
        self.all_sprites.add(self.bonzai_tree3)

    # method called when in title screen to render
    def title_screen(self):

        inputcapture.next_screen_check_input(self)
        # Did the user click the window close button?
        inputcapture.quit_check_input(self)

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
        inputcapture.quit_check_input(self)
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
        inputcapture.quit_check_input(self)

    def menu_credits(self):
        # placeholder for credits showcase
        inputcapture.quit_check_input(self)

    def main_game(self, clock):

        # Did the user click the window close button?
        inputcapture.quit_check_input(self)

        # Fill the background with black
        self.screen.fill((0, 0, 0))

        # check character input
        inputcapture.character_check_input(self.mainCharacter)

        # move or animate our test sprites
        self.mainCharacter.move()
        self.bonzai_tree1.animate()
        self.bonzai_tree2.animate()
        self.bonzai_tree3.animate()

        # draw all sprites
        self.all_sprites.draw(self.screen)

        # draw fps in screen
        self.DIAGNOSTICS_FONT.render_to(self.screen, (10, 10), "FPS:" + str(round(clock.get_fps())), (150, 150, 150))
        # self.DIAGNOSTICS_FONT.render_to(self.screen, (10,30), "FPS:" + str(round(clock.get_fps())),(150, 150, 150))
        # Flip the display ( update the display)
        pygame.display.flip()
