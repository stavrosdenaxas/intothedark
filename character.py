import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.charAnimation = [pygame.image.load("Sprites/MainCharacter/CharTest1.png"),
                              pygame.image.load("Sprites/MainCharacter/CharTest2.png"),
                              pygame.image.load("Sprites/MainCharacter/CharTest3.png"),
                              pygame.image.load("Sprites/MainCharacter/CharTest4.png"),
                              pygame.image.load("Sprites/MainCharacter/CharTest5.png"),
                              pygame.image.load("Sprites/MainCharacter/CharTest6.png")]
        self.positionX = 200
        self.positionY = 200
        self.velocityX = 0
        self.velocityY = 0
        self.all_sprites = pygame.sprite.Group()
        self.image = self.charAnimation[0]
        self.all_sprites.add(self)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

    def draw_character(self, screen):
        self.all_sprites.draw(screen)
        return "done"

    def move(self):
        self.velocityX += 1
        self.velocityY += 1
        return "done"
