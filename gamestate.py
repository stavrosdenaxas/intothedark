import pygame
import pygame.freetype
import character
import flora
import inputcapture


screen_width = 1920
screen_height = 1080


class Gamestate:
    def __init__(self):
        self.state = 'title_screen'
        # set resolution variables

        self.screen = pygame.display.set_mode([screen_width, screen_height])
        self.running = True
        self.GAME_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 128)
        self.MENU_FONT = pygame.freetype.Font("Assets/Fonts/Oswald-Bold.ttf", 96)

        self.all_sprites = pygame.sprite.Group()
        self.bonzai_tree1 = flora.Flora()
        self.bonzai_tree2 = flora.Flora()
        self.bonzai_tree3 = flora.Flora()
        self.mainCharacter = character.Character()

        # ADD BONZAI TREE AS TEST


        self.all_sprites.add(self.mainCharacter)
        self.all_sprites.add(self.bonzai_tree1)
        self.all_sprites.add(self.bonzai_tree2)
        self.all_sprites.add(self.bonzai_tree3)

    def title_screen(self):
        # Did the user click the window close button?
        inputcapture.next_screen_check_input(self)
        inputcapture.quit_check_input(self)

        # Fill the background with white
        self.screen.fill((0, 0, 0))
        self.GAME_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height / 2 - 0.1 * screen_width)),
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
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.4 - 0.1 * screen_width)),
                                 "Enter the Darkness",
                                 (50, 50, 50))
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.55 - 0.1 * screen_width)),
                                 "Options",
                                 (50, 50, 50))
        self.MENU_FONT.render_to(self.screen,
                                 (round(screen_width / 2 - 0.2 * screen_width),
                                  round(screen_height * 0.7 - 0.1 * screen_width)),
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
        self.mainCharacter.move()
        self.all_sprites.draw(self.screen)
        self.bonzai_tree1.animate()
        self.bonzai_tree2.animate()
        self.bonzai_tree3.animate()
        # Flip the display
        pygame.display.flip()
