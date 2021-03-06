import pygame
import enemy
import random
import hero
import gamestate
from pygame.math import Vector2


class Projectile(pygame.sprite.Sprite):
    def __init__(self, mouse_or_enemy_position, game_area, hero, type):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()

        self.type = type
        if self.type == "hero":
            self.position = hero.position
            self.velocity = Vector2(mouse_or_enemy_position) - (Vector2(hero.position) + Vector2(hero.camera))
            Vector2.scale_to_length(self.velocity, 4)
        elif self.type == "enemy":
            self.position = mouse_or_enemy_position
            self.velocity = (Vector2(hero.position) +
                             Vector2(random.randint(5, 100), random.randint(5, 100)) - Vector2(mouse_or_enemy_position))
            Vector2.scale_to_length(self.velocity, 5)
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
        self.hero = hero
        self.game_area = game_area

    def update(self):
        self.position += self.velocity
        self.rect.center = self.position
        self.current_sprite += self.growth_factor
        if self.current_sprite >= len(self.assetAnimation):
            self.current_sprite = 0
        self.image = self.assetAnimation[int(self.current_sprite)]

        if self.type == "hero":
            if not self.game_area.contains(self.rect):
                self.kill()
                self.hero.projectile_count -= 1

            if pygame.time.get_ticks() - self.projectile_fired_time > self.projectile_live_time:
                self.kill()
                self.hero.projectile_count -= 1

        if self.type == "enemy":
            if pygame.time.get_ticks() - self.projectile_fired_time > self.projectile_live_time:
                self.kill()

    def hit(self, all_sprites, game_state):

        for obj in all_sprites:
            if isinstance(obj, enemy.Enemy):
                if self.type == "hero":
                    if self.rect.colliderect(obj.rect):
                        if obj.enemy_type == "Invulnro":
                            print("nice try")
                            self.kill()
                            self.hero.projectile_count -= 1
                        elif obj.enemy_type == "Mergamoth":
                            obj.scale_factor += 1
                            self.kill()
                            self.hero.projectile_count -= 1
                            if obj.scale_factor < 6:
                                for x in range(obj.scale_factor):
                                    placeholder = enemy.Enemy(self.hero, gamestate.game_area, "Mergamoth")
                                    placeholder.scale_factor = obj.scale_factor
                                    placeholder.scale_enemy()
                                    placeholder.rect.x = obj.rect.x + random.randint(1, 10)
                                    placeholder.rect.y = obj.rect.y + random.randint(1, 10)
                                    all_sprites.add(placeholder)
                            all_sprites.remove(obj)
                            obj.kill()

                        else:
                            all_sprites.remove(obj)
                            obj.kill()
                            self.kill()
                            self.hero.projectile_count -= 1

            if isinstance(obj, hero.Hero):
                if self.type == "enemy":
                    if self.rect.colliderect(obj.rect):
                        if not obj.is_dead:
                            obj.death(game_state)
