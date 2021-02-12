import pygame
from pygame.math import Vector2


class Projectile(pygame.sprite.Sprite):
    def __init__(self, mouse_position, game_area, character):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.position = character.position
        self.velocity = pygame.Vector2.normalize(character.position - mouse_position)
        print(self.velocity)
        # self.acceleration =

        self.assetAnimation = [pygame.image.load("Assets/Sprites/Projectiles/Projectile1.png"),
                               pygame.image.load("Assets/Sprites/Projectiles/Projectile2.png"),
                               pygame.image.load("Assets/Sprites/Projectiles/Projectile3.png")]

        self.current_sprite = 0
        self.growth_factor = 0.4
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.game_area = game_area

    def move(self):
        print(self.position)
        self.position += self.velocity
        print(self.position)
        self.rect.center = self.position

        self.current_sprite += self.growth_factor
        if self.current_sprite >= len(self.assetAnimation):
            self.current_sprite = 0
        self.image = self.assetAnimation[int(self.current_sprite)]

        if not self.game_area.contains(self.rect):
            self.kill()
