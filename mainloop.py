import pygame
import gamestate

# Initial Game Setup
pygame.init()
clock = pygame.time.Clock()
# Create gamestate object, where the current game state is kept. This object coordinates:
# the main game loop, transitions between screen and levels of the game
game_state = gamestate.Gamestate('title_screen')


# determine the state of the game: if we are in a title, menu or gameplay screen and then run loop code
def determine_state():
    if game_state.state == 'title_screen':
        game_state.title_screen()
    if game_state.state == 'main_menu':
        game_state.main_menu()
    if game_state.state == 'game_lobby':
        game_state.game_lobby(clock)
    if game_state.state == 'main_game':
        game_state.main_game(clock)
    if game_state.state == 'credit_screen':
        game_state.credits_screen(clock)


def game_restart_check():
    if pygame.time.get_ticks() - game_state.time_of_death >= 4000:
        game_state.__init__('main_menu')
        print("restart")


# main game loop, clock set to 60fps max
def main():
    while game_state.running:
        clock.tick(60)
        determine_state()
        game_restart_check()
    # Done! Time to quit.

    pygame.quit()


if __name__ == '__main__':
    main()
