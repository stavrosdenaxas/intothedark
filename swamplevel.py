import pygame
import enemy
import flora


class SwampLevel:
    def __init__(self, all_sprites, hero, game_area):
        # forest floor
        self.tileset = pygame.image.load("Assets/Sprites/Ground/SwampFloor.png").convert()
        for x in range(5):
            all_sprites.add(flora.Flora("Tree2"))
        # forest enemies
        for x in range(20):
            all_sprites.add(enemy.Enemy(hero, game_area, "Skeletor"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Cacodemon"))

        # forest flora
        self.bonzai_tree1 = flora.Flora("Bonzai")

        all_sprites.add(self.bonzai_tree1)
        all_sprites.add(hero)

    def draw(self, screen, camera):
        for x in range(30):
            for y in range(17):
                screen.blit(self.tileset, camera + (x * 256, y * 256))