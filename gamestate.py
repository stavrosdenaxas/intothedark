import pygame


class Gamestate():
    def __init__(self):
        self.state = 'title_screen'
        # set resolution variables
        self.screen_width = 1920
        self.screen_height = 1080
        self.screen = pygame.display.set_mode([self.screen_width, self.screen_height])
        self.running = True

    def title_screen(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = "main_menu"

        # Fill the background with white
        self.screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(self.screen, (0, 0, 255), (750, 750), 75)

        # Flip the display
        pygame.display.flip()


    def main_menu(self):
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.state = "main_game"

        # Fill the background with white
        self.screen.fill((255, 0, 255))

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





