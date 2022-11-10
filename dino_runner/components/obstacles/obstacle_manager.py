import pygame.time
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.birds import Bird
from dino_runner.utils.constants import SMALL_CACTUS
from dino_runner.utils.constants import LARGE_CACTUS
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []




    def update(self,game):
        self.aleatorio = random.randint(0, 2)
        if len(self.obstacles) == 0:
            cactus = Cactus(SMALL_CACTUS)
            cactus2 = Cactus(LARGE_CACTUS)
            bird = Bird(BIRD)
            if self.aleatorio == 0:
                self.obstacles.append(cactus)
            elif self.aleatorio == 1:
                self.obstacles.append(cactus2)
            elif self.aleatorio == 2:
                self.obstacles.append(bird)







        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.death_count += 1
                game.playing = False
                break





    def draw(self,screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []


