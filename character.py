import pygame
import random
from pygame.math import Vector2


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.assetAnimation = [pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard1.png"),
                               pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard2.png"),
                               pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard3.png"),
                               pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard4.png"),
                               pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard5.png"),
                               pygame.image.load("Assets/Sprites/MainCharacter/CharTestWizard6.png")]
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
        self.inventory = [1]
        self.is_moving = False

    def move(self):

        if abs(self.rect.y - self.mouse_position[1] + self.image.get_size()[0]) > 3 or\
                abs(self.rect.x - self.mouse_position[0] + self.image.get_size()[1]) > 3:
            self.is_moving = True

        if self.is_moving:
            if self.rect.x - self.mouse_position[0] < - self.image.get_size()[0]:
                self.rect.x += random.randint(-1, 5)
                self.rect.y += random.randint(-1, 1)
            if self.rect.x - self.mouse_position[0] > - self.image.get_size()[0]:
                self.rect.x -= random.randint(-1, 5)
                self.rect.y += random.randint(-1, 1)
            if self.rect.y - self.mouse_position[1] < - self.image.get_size()[1]:
                self.rect.y += random.randint(-1, 5)
                self.rect.x -= random.randint(-1, 1)
            if self.rect.y - self.mouse_position[1] > - self.image.get_size()[1]:
                self.rect.y -= random.randint(-1, 5)
                self.rect.x -= random.randint(-1, 1)

        if self.is_moving:
            self.current_sprite += 0.3
            if self.current_sprite >= len(self.assetAnimation):
                self.current_sprite = 0
            self.image = self.assetAnimation[int(self.current_sprite)]

        if abs(self.rect.x - self.mouse_position[0] + self.image.get_size()[0]) < 3 and\
                abs(self.rect.y - self.mouse_position[1] + self.image.get_size()[1]) < 3:
            self.is_moving = False
            self.current_sprite = 0
        self.position = self.rect.center

    # placeholder method for inventory
    def add_item(self, item):
        self.inventory[0] = item
        return "placeholder"

    # placeholder for death
    def death(self):
        self.kill()
