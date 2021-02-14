import pygame


class ForestLevel:
    def __init__(self, screen):
        self.tileset = pygame.image.load("Assets/Sprites/Tilemap/ForestFloor.png")
        for x in range(8):
            for y in range(5):
                screen.blit(self.tileset, (x * 256, y * 256))
