import pygame
import enemy
import flora
import portal
import item


class ForestLevel:
    def __init__(self, all_sprites, hero, game_area):
        # forest floor
        self.tileset = pygame.image.load("Assets/Sprites/Ground/ForestFloor.png").convert()
        for x in range(5):
            all_sprites.add(flora.Flora("Tree1"))
            all_sprites.add(flora.Flora("Tree2"))
        all_sprites.add(hero)
        all_sprites.add(item.Item(game_area, 150, 150))
        all_sprites.add(portal.Portal(game_area, 350, 350))
        # forest enemies
        for x in range(10):
            all_sprites.add(enemy.Enemy(hero, game_area, "Mushroom"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Invulnro"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Cacodemon"))
            all_sprites.add(enemy.Enemy(hero, game_area, "Tetro"))


        # forest flora
        self.bonzai_tree1 = flora.Flora("Bonzai")

        all_sprites.add(self.bonzai_tree1)
        all_sprites.add(hero)

    def draw(self, screen, camera):
        for x in range(30):
            for y in range(17):
                screen.blit(self.tileset, camera + (x * 256, y * 256))



