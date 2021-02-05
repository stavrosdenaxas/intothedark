

# Import and initialize the pygame library
import pygame
import character

pygame.init()
clock = pygame.time.Clock()

# set resolution variables
screen_width = 1920
screen_height = 1080

# Set up the drawing window
screen = pygame.display.set_mode([screen_width, screen_height])

# Run until the user asks to quit
running = True
sceneScreen = 1
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    # screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # Flip the display
    pygame.display.flip()
    clock.tick(60)

# Done! Time to quit.
pygame.quit()
