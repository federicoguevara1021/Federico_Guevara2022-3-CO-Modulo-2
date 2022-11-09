import pygame.time

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.obstacles2 = []


    def update(self,game):
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        if len(self.obstacles2) == 0:
            cactus2 = Cactus(LARGE_CACTUS)
            self.obstacles2.append(cactus2)



        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

        for obstacle in self.obstacles2:
            obstacle.update(game.game_speed,self.obstacles2)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(700)
                game.playing = False
                break




    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

        for x in self.obstacles2:
            x.draw(screen)

