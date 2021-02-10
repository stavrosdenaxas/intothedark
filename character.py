import pygame
import random


class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.charAnimation = [pygame.image.load("Assets/Sprites/MainCharacter/CharTest1.png"),
                              pygame.image.load("Assets/Sprites/MainCharacter/CharTest2.png"),
                              pygame.image.load("Assets/Sprites/MainCharacter/CharTest3.png"),
                              pygame.image.load("Assets/Sprites/MainCharacter/CharTest4.png"),
                              pygame.image.load("Assets/Sprites/MainCharacter/CharTest5.png"),
                              pygame.image.load("Assets/Sprites/MainCharacter/CharTest6.png")]

        self.velocityX = 0
        self.velocityY = 0
        self.current_sprite = 0
        self.scale_factor = 0.5
        self.mouse_position = [300, 300]
        self.image = self.charAnimation[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 600

        self.is_moving = False

    def move(self):

        if abs(self.rect.y - self.mouse_position[1] + self.image.get_size()[0]) > 3 or abs(self.rect.x - self.mouse_position[0] + self.image.get_size()[1]) > 3:
            self.is_moving = True

        if self.is_moving:
            if self.rect.x - self.mouse_position[0] < - self.image.get_size()[0]:
                self.rect.x += random.randint(-1, 7)
            if self.rect.x - self.mouse_position[0] > - self.image.get_size()[0]:
                self.rect.x -= random.randint(-1, 7)
            if self.rect.y - self.mouse_position[1] < - self.image.get_size()[1]:
                self.rect.y += random.randint(-1, 7)
            if self.rect.y - self.mouse_position[1] > - self.image.get_size()[1]:
                self.rect.y -= random.randint(-1, 7)

        if self.is_moving:
            self.current_sprite += 0.3
            if self.current_sprite >= len(self.charAnimation):
                self.current_sprite = 0
            self.image = self.charAnimation[int(self.current_sprite)]

        if abs(self.rect.x - self.mouse_position[0] + self.image.get_size()[0]) < 3 and\
                abs(self.rect.y - self.mouse_position[1] + self.image.get_size()[1]) < 3:
            self.is_moving = False
            self.current_sprite = 0
