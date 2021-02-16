import pygame
import random
from pygame.math import Vector2


class Enemy(pygame.sprite.Sprite):
    def __init__(self, hero, game_area, enemy_type):
        super().__init__()
        self.hero = hero
        self.enemy_type = enemy_type
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        if self.enemy_type == "Mushroom":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/Enemy1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Enemy2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Enemy3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Enemy4.png")]
            self.velocity = Vector2(self.hero.position) - Vector2(self.position)
            Vector2.scale_to_length(self.velocity, 3)
        if self.enemy_type == "Skeletor":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor4.png")]
            self.velocity = Vector2(self.hero.position) - Vector2(self.position)
            Vector2.scale_to_length(self.velocity, 8)

        if self.enemy_type == "Hydra":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/hydra/hydra1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra4.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra5.png")]
            self.velocity = Vector2(self.hero.position) - Vector2(self.position)
            Vector2.scale_to_length(self.velocity, 8)

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
        if self.enemy_type == "Mushroom":
            Vector2.scale_to_length(self.velocity, 1)
        if self.enemy_type == "Skeletor":
            Vector2.scale_to_length(self.velocity, 2)
        if self.enemy_type == "Hydra":
            Vector2.scale_to_length(self.velocity, 2)
