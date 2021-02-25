import pygame
from pygame.math import Vector2


class Portal(pygame.sprite.Sprite):
    def __init__(self, game_area, x, y):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.assetAnimation = [pygame.image.load("Assets/Sprites/Portal/levelportal1.png"),
                               pygame.image.load("Assets/Sprites/Portal/levelportal2.png"),
                               pygame.image.load("Assets/Sprites/Portal/levelportal3.png"),
                               pygame.image.load("Assets/Sprites/Portal/levelportal4.png"),
                               pygame.image.load("Assets/Sprites/Portal/levelportal5.png"),
                               pygame.image.load("Assets/Sprites/Portal/levelportal6.png")]

        self.game_area = game_area
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = self.rect.center
        self.is_moving = False


def update(self):
    self.current_sprite += self.scale_factor
    if self.current_sprite >= len(self.treeAnimation):
        self.current_sprite = 0
    self.image = self.treeAnimation[int(self.current_sprite)]
