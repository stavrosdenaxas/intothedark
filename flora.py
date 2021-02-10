import pygame
import random


class Flora(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.treeAnimation = [pygame.image.load("Assets/Sprites/Flora/Bonzai1.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai2.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai3.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai4.png"),
                              pygame.image.load("Assets/Sprites/Flora/Bonzai5.png")]
        self.velocityX = 0
        self.velocityY = 0
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.image = self.treeAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100,500)
        self.rect.y = random.randint(100,500)
        self.growth_factor = random.randint(100,1000)/10000
        self.is_moving = False

    def animate(self):
        self.current_sprite += self.growth_factor
        if self.current_sprite >= len(self.treeAnimation):
            self.current_sprite = 0
        self.image = self.treeAnimation[int(self.current_sprite)]
