import pygame
import hero
from pygame.math import Vector2


class LevelIcon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/Bonzai1.png")]
        self.position = Vector2()
        self.velocity = Vector2(0, 0)
        self.acceleration = Vector2()
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = self.rect.center
        self.is_moving = False
        self.is_dead = False

    def update(self):
        self.rect.center = self.position

    def hit(self, all_sprites, game_state):
        if not self.is_dead:
            for obj in all_sprites:
                if isinstance(obj, hero.Hero):
                    if self.rect.colliderect(obj.rect):
                        # enter level if collide
                        game_state.state = "main_game"
                        game_state.level = "Forest"
