import pygame
from pygame.math import Vector2


# placeholder for parent of Enemy, Hero and other physical game objects/chars
class GameObject(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.max_speed = Vector2(3, 3)
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.collide_rect = pygame.Rect(1, 1, 1, 1)
        self.rect = self.image.get_rect()
        self.position = self.rect.center
        self.is_moving = False
        self.is_dead = False
