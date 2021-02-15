import pygame
import enemy
import flora


class ForestLevel:
    def __init__(self, all_sprites, hero, game_area):
        # forest floor
        self.tileset = pygame.image.load("Assets/Sprites/Tilemap/ForestFloor.png").convert()
        for x in range(100):
            all_sprites.add(flora.Flora("Tree1"))
            all_sprites.add(flora.Flora("Tree2"))
        # forest enemies
        for x in range(50):
            all_sprites.add(enemy.Enemy(hero, game_area, "Mushroom"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Skeletor"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Hydra"))

        # forest flora
        self.bonzai_tree1 = flora.Flora("Bonzai")

        all_sprites.add(self.bonzai_tree1)
        all_sprites.add(hero)

    def draw(self, screen, camera):
        for x in range(30):
            for y in range(17):
                screen.blit(self.tileset, camera + (x * 256, y * 256))
