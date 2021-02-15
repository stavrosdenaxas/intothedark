import pygame
import random
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hero, game_area):
        super().__init__()
        self.hero = hero
        self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/Enemy1.png"),
                               pygame.image.load("Assets/Sprites/Enemies/Enemy2.png"),
                               pygame.image.load("Assets/Sprites/Enemies/Enemy3.png"),
                               pygame.image.load("Assets/Sprites/Enemies/Enemy4.png")]
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.velocity = Vector2(self.hero.position) - Vector2(self.position)
        Vector2.scale_to_length(self.velocity, 3)
        self.game_area = game_area
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.mouse_position = [random.randint(100, 500), random.randint(100, 500)]
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, game_area.width)
        self.rect.y = random.randint(100, game_area.height)
        self.position = self.rect.center
        self.is_moving = True

    def update(self):
        if self.is_moving:
            self.position += self.velocity
            self.rect.center = self.position
            self.current_sprite += 0.3
            if self.current_sprite >= len(self.assetAnimation):
                self.current_sprite = 0
            self.image = self.assetAnimation[int(self.current_sprite)]

        if not self.game_area.contains(self.rect):
            self.kill()
        self.velocity = Vector2(self.hero.position) - Vector2(self.position)
        self.velocity.normalize_ip()
