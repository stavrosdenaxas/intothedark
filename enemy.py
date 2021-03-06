import pygame
import random
import gamestate
import projectile
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
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/Shroom/Enemy1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Shroom/Enemy2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Shroom/Enemy3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Shroom/Enemy4.png")]
        if self.enemy_type == "Skeletor":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/skeletor/skeletor4.png")]
        if self.enemy_type == "Hydra":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/hydra/hydra1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra4.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/hydra/hydra5.png")]
        if self.enemy_type == "Cacodemon":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/Cacodemon/cacodemon1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Cacodemon/cacodemon2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Cacodemon/cacodemon3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Cacodemon/cacodemon4.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Cacodemon/cacodemon5.png")]
        if self.enemy_type == "Invulnro":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/invulnro/invulnro1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/invulnro/invulnro2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/invulnro/invulnro3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/invulnro/invulnro4.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/invulnro/invulnro5.png")]
        if self.enemy_type == "Tetro":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro1.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro2.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro3.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro4.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro5.png"),
                                   pygame.image.load("Assets/Sprites/Enemies/Tetro/Tetro6.png")]
        if self.enemy_type == "Mergamoth":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Mergamoth/mergamoth1.png"),
                                   pygame.image.load("Assets/Sprites/Mergamoth/mergamoth2.png"),
                                   pygame.image.load("Assets/Sprites/Mergamoth/mergamoth3.png"),
                                   pygame.image.load("Assets/Sprites/Mergamoth/mergamoth4.png"),
                                   pygame.image.load("Assets/Sprites/Mergamoth/mergamoth5.png")]

        self.game_area = game_area
        self.current_sprite = 0
        self.scale_factor = 1
        self.mouse_position = [random.randint(100, 500), random.randint(100, 500)]
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, game_area.width)
        self.rect.y = random.randint(100, game_area.height)
        self.position = self.rect.center
        self.is_moving = True

    def update(self, hero):
        if self.is_moving:
            self.position += self.velocity
            self.rect.center = self.position
            self.current_sprite += 0.3
            if self.current_sprite >= len(self.assetAnimation):
                self.current_sprite = 0
            self.image = self.assetAnimation[int(self.current_sprite)]

        # if not self.game_area.contains(self.rect):
        #    self.kill()

        self.velocity = Vector2(self.hero.position) - Vector2(self.position)
        if self.enemy_type == "Mushroom":
            Vector2.scale_to_length(self.velocity, 1)
        if self.enemy_type == "Skeletor":
            Vector2.scale_to_length(self.velocity, 2)
        if self.enemy_type == "Hydra":
            Vector2.scale_to_length(self.velocity, 2)
        if self.enemy_type == "Cacodemon":
            Vector2.scale_to_length(self.velocity, 2)
        if self.enemy_type == "Invulnro":
            Vector2.scale_to_length(self.velocity, 1)
        if self.enemy_type == "Tetro":
            Vector2.scale_to_length(self.velocity, 4)
        if self.enemy_type == "Mergamoth":
            Vector2.scale_to_length(self.velocity, self.scale_factor)

        if self.enemy_type == "Cacodemon" or self.enemy_type == "Mergamoth":
            if random.randint(1, 100) > 99:
                self.velocity.scale_to_length(0)
                # self.fired_time = pygame.time.get_ticks()
                gamestate.all_sprites.add(projectile.Projectile(self.rect.center, gamestate.game_area, hero, "enemy"))

    def scale_enemy(self):
        self.image = pygame.transform.scale(self.image, (round(256 / self.scale_factor), round(256 / self.scale_factor)))
        self.rect = self.image.get_rect()
