import pygame
import random
from pygame.math import Vector2


class Flora(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.treeAnimation = [pygame.image.load("Assets/Sprites/Flora/Bonzai1.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai2.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai3.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai4.png")]
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.image = self.treeAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 500)
        self.rect.y = random.randint(100, 500)
        self.position = self.rect.center
        self.growth_factor = random.randint(100, 1000)/10000
        self.is_moving = False

    def update(self):
        self.current_sprite += self.growth_factor
        if self.current_sprite >= len(self.treeAnimation):
            self.current_sprite = 0
        self.image = self.treeAnimation[int(self.current_sprite)]
