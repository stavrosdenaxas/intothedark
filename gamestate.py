import pygame
import pygame.freetype


class Gamestate:
    def __init__(self):
        self.state = 'title_screen'
        # set resolution variables
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.running = True
        self.GAME_FONT = pygame.freetype.Font("Fonts/Oswald-Bold.ttf", 128)

    def title_screen(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = "main_menu"

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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = "main_game"

        # Fill the background with white
        self.screen.fill((0, 0, 0))

        # Draw a solid blue circle in the center
        pygame.draw.circle(self.screen, (0, 0, 255), (500, 500), 75)

        # Flip the display
        pygame.display.flip()

    def main_game(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        # Fill the background with white
        # screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()
