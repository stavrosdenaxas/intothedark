import pygame
import pygame.freetype
import character
import inputcapture


class Gamestate:
    def __init__(self):
        self.state = 'title_screen'
        # set resolution variables
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.running = True
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)

        self.all_sprites = pygame.sprite.Group()

        self.mainCharacter = character.Character()


        self.all_sprites.add(self.mainCharacter)

    def title_screen(self):
        # Did the user click the window close button?
        inputcapture.next_screen_check_input(self)
        inputcapture.quit_check_input(self)

        # Fill the background with white
        self.screen.fill((0, 0, 0))
        self.GAME_FONT.render_to(self.screen,
                                 (round(self.screen_width / 2 - 0.2 * self.screen_width),
                                  round(self.screen_height / 2 - 0.1 * self.screen_width)),
                                 "Into the Dark",
                                 (50, 50, 50))
        # Draw a solid blue circle in the center
        pygame.display.flip()

    def main_menu(self):
        # Did the user click the window close button?
        inputcapture.next_screen_check_input(self)
        inputcapture.quit_check_input(self)

        # Fill the background with white
        self.screen.fill((0, 0, 0))

        # Draw a solid blue circle in the center
        self.MENU_FONT.render_to(self.screen,
                                 (round(self.screen_width / 2 - 0.2 * self.screen_width),
                                  round(self.screen_height * 0.4 - 0.1 * self.screen_width)),
                                 "Enter the Darkness",
                                 (50, 50, 50))
        self.MENU_FONT.render_to(self.screen,
                                 (round(self.screen_width / 2 - 0.2 * self.screen_width),
                                  round(self.screen_height * 0.55 - 0.1 * self.screen_width)),
                                 "Options",
                                 (50, 50, 50))
        self.MENU_FONT.render_to(self.screen,
                                 (round(self.screen_width / 2 - 0.2 * self.screen_width),
                                  round(self.screen_height * 0.7 - 0.1 * self.screen_width)),
                                 "Credits",
                                 (50, 50, 50))
        # Flip the display
        pygame.display.flip()

    def menu_options(self):
        # placeholder
        inputcapture.quit_check_input(self)

    def menu_credits(self):
        # placeholder
        inputcapture.quit_check_input(self)

    def main_game(self):
        # Did the user click the window close button?
        inputcapture.quit_check_input(self)

        # Fill the background with white
        # screen.fill((255, 255, 255))
        self.screen.fill((0, 0, 0))
        inputcapture.character_check_input(self.mainCharacter)
        # Draw a solid blue circle in the center

        self.all_sprites.draw(self.screen)


        # Flip the display
        pygame.display.flip()
