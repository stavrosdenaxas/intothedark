import pygame
import hero
from pygame.math import Vector2


class LevelIcon(pygame.sprite.Sprite):
    def __init__(self, x, y, level_type):
        super().__init__()
        if level_type == "Forest":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/Forest.png")]
        if level_type == "Mountain":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/Rock.png")]
        if level_type == "Swamp":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/Swamp.png")]
        if level_type == "Mergamoth":
            self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/Swamp.png")]
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
        self.level_type = level_type
        self.level_complete = False

    def update(self):
        self.rect.center = self.position
        if self.level_complete:
            if self.level_type == "Forest":
                print("triggered forest is complete change sprite")
                self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/ForestComplete.png")]
            if self.level_type == "Mountain":
                self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/RockComplete.png")]
            if self.level_type == "Swamp":
                self.assetAnimation = [pygame.image.load("Assets/Sprites/Flora/SwampComplete.png")]
            self.image = self.assetAnimation[self.current_sprite]

    def hit(self, all_sprites, game_state):
        if not self.is_dead:
            for obj in all_sprites:
                if isinstance(obj, hero.Hero):
                    if self.rect.colliderect(obj.rect):
                        if not self.level_complete:
                            if self.level_type == "Forest":
                                game_state.state = "main_game"
                                game_state.level = "Forest"
                            if self.level_type == "Mountain":
                                game_state.state = "main_game"
                                game_state.level = "Mountain"
                            if self.level_type == "Swamp":
                                game_state.state = "main_game"
                                game_state.level = "Swamp"