import pygame
import enemy
import flora
from pygame.math import Vector2


class Hero(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
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
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2()

        self.current_sprite = 0
        self.scale_factor = 0.5
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = screen_width
        self.rect.y = screen_height
        self.position = self.rect.center
        self.collide_rect = pygame.Rect(self.rect.x + 12,
                                        self.rect.y + 50,
                                        15,
                                        15)
        self.projectile_count = 0
        self.fire_rate = 100
        self.projectile_fired_time = pygame.time.get_ticks()
        self.inventory = [1]
        self.is_moving = False
        self.is_dead = False
        self.camera = Vector2(-screen_width/2, - screen_height/2)

    def update(self, all_sprites):

        if not self.is_dead:
            self.rect.x += self.velocity.x
            self.collide_rect.x += self.velocity.x
            for obj in all_sprites:
                if isinstance(obj, flora.Flora):
                    if self.collide_rect.colliderect(obj.collide_rect):
                        if self.velocity.x < 0:
                            self.collide_rect.left = obj.collide_rect.right
                            self.rect.left = obj.collide_rect.right
                            self.velocity.x = 0
                        elif self.velocity.x > 0:
                            self.rect.right = obj.collide_rect.left
                            self.collide_rect.right = obj.collide_rect.left
                            self.velocity.x = 0

            self.rect.y += self.velocity.y
            self.collide_rect.y += self.velocity.y
            for obj in all_sprites:
                if isinstance(obj, flora.Flora):
                    if self.collide_rect.colliderect(obj.collide_rect):
                        if self.velocity.y < 0:
                            self.collide_rect.top = obj.collide_rect.bottom
                            self.rect.bottom = self.collide_rect.bottom
                            self.velocity.y = 0
                        elif self.velocity.y > 0:
                            self.rect.bottom = obj.collide_rect.top
                            self.collide_rect.bottom = obj.collide_rect.top
                            self.velocity.y = 0

            self.camera -= self.velocity
            self.position = self.rect.center

            if self.is_moving:
                self.current_sprite += 0.3
                if self.current_sprite >= len(self.assetAnimation):
                    self.current_sprite = 0
            else:
                self.current_sprite = 0

            self.image = self.assetAnimation[int(self.current_sprite)]

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

    def hit(self, all_sprites, gamestate):

        if not self.is_dead:
            for obj in all_sprites:
                if isinstance(obj, enemy.Enemy):
                    if self.rect.colliderect(obj.rect):
                        self.death(gamestate)
                # add key collide here and call add_item if added

    def death(self, gamestate):
        self.is_dead = True
        self.current_sprite = 1
        gamestate.time_of_death = pygame.time.get_ticks()
