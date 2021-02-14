import pygame
import enemy
from pygame.math import Vector2


class Projectile(pygame.sprite.Sprite):
    def __init__(self, mouse_position, game_area, hero):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.position = hero.position
        self.velocity = Vector2(mouse_position) - (Vector2(hero.position) + Vector2(hero.camera))
        Vector2.scale_to_length(self.velocity, 4)
        # self.acceleration =

        self.assetAnimation = [pygame.image.load("Assets/Sprites/Projectiles/Projectile1.png"),
                               pygame.image.load("Assets/Sprites/Projectiles/Projectile2.png"),
                               pygame.image.load("Assets/Sprites/Projectiles/Projectile3.png")]

        self.current_sprite = 0
        self.growth_factor = 0.4
        self.projectile_fired_time = pygame.time.get_ticks()
        self.projectile_live_time = 5000
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.character = hero
        self.game_area = game_area

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position
        self.current_sprite += self.growth_factor
        if self.current_sprite >= len(self.assetAnimation):
            self.current_sprite = 0
        self.image = self.assetAnimation[int(self.current_sprite)]

        if not self.game_area.contains(self.rect):
            self.kill()
            self.character.projectile_count -= 1

        if pygame.time.get_ticks() - self.projectile_fired_time > self.projectile_live_time:
            self.kill()
            self.character.projectile_count -= 1

    def hit(self, all_sprites):

        for obj in all_sprites:
            if isinstance(obj, enemy.Enemy):
                if self.rect.colliderect(obj.rect):
                    all_sprites.remove(obj)
                    obj.kill()
                    self.kill()
                    self.character.projectile_count -= 1
