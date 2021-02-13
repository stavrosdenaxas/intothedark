import pygame
import random
import enemy
from pygame.math import Vector2


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.assetAnimation = [pygame.image.load("Assets/Sprites/Hero/CharTestWizard1.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestWizard2.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestWizard3.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestWizard4.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestWizard5.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestWizard6.png")]
        self.deathAnimation = [pygame.image.load("Assets/Sprites/Hero/CharTestDeath1.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestDeath2.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestDeath3.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestDeath4.png"),
                               pygame.image.load("Assets/Sprites/Hero/CharTestDeath5.png")]
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.mouse_position = [random.randint(100, 500), random.randint(100, 500)]
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, 500)
        self.rect.y = random.randint(100, 500)
        self.position = self.rect.center
        self.projectile_count = 0
        self.fire_rate = 400
        self.projectile_fired_time = pygame.time.get_ticks()
        self.inventory = [1]
        self.is_moving = False
        self.is_dead = False

    def move(self):

        if not self.is_dead:
            self.position += self.velocity
            self.rect.center = self.position

            if self.is_moving:
                self.current_sprite += 0.3
                if self.current_sprite >= len(self.assetAnimation):
                    self.current_sprite = 0
            else:
                self.current_sprite = 0

            self.image = self.assetAnimation[int(self.current_sprite)]
            self.position = self.rect.center

        elif self.is_dead:
            self.current_sprite += 0.15
            if self.current_sprite >= len(self.deathAnimation):
                self.current_sprite = 4
            self.image = self.deathAnimation[int(self.current_sprite)]

        self.position = self.rect.center

    # placeholder method for inventory
    def add_item(self, item):
        self.inventory[0] = item
        return "placeholder"

    def hit(self, all_sprites):

        if not self.is_dead:
            for obj in all_sprites:
                if isinstance(obj, enemy.Enemy):
                    if self.rect.colliderect(obj.rect):
                        self.is_dead = True
                        self.current_sprite = 1

    # placeholder for death
    def death(self):
        self.kill()
