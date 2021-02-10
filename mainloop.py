import pygame
import gamestate

# Initial Game Setup
pygame.init()
clock = pygame.time.Clock()
# Create gamestate object, where the current game state is kept. This object coordinates:
# the main game loop, transitions between screen and levels of the game
game_state = gamestate.Gamestate()


# determine the state of the game: if we are in a title, menu or gameplay screen and then run loop code
def determine_state():
    if game_state.state == 'title_screen':
        game_state.title_screen()
    if game_state.state == 'main_menu':
        game_state.main_menu()
    if game_state.state == 'main_game':
        game_state.main_game(clock)


# main game loop, clock set to 60fps max
while game_state.running:

    determine_state()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
