import pygame
import gamestate


#Initial Game Setup
pygame.init()
clock = pygame.time.Clock()
game_state = gamestate.Gamestate()


# Run until the user asks to quit
while game_state.running:
    game_state.main_game()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
