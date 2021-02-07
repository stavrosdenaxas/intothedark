import pygame
import gamestate


#Initial Game Setup
pygame.init()
clock = pygame.time.Clock()
game_state = gamestate.Gamestate()


# Run until the user asks to quit
while game_state.running:

    if game_state.state == 'title_screen':
        game_state.title_screen()
    if game_state.state == 'main_menu':
        game_state.main_menu()
    if game_state.state == 'main_game':
        game_state.main_game()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
