import pygame
from pygame.math import Vector2


# placeholder class
class Item(pygame.sprite.Sprite):
    def __init__(self, game_area, x, y):
        super().__init__()
        self.position = Vector2()
        self.velocity = Vector2()
        self.acceleration = Vector2()
        self.assetAnimation = [pygame.image.load("Assets/Sprites/Items/levelkey.png")]
        self.game_area = game_area
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.image = self.assetAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.position = self.rect.center
        self.is_moving = False


def update():
    print("do nothing update")
