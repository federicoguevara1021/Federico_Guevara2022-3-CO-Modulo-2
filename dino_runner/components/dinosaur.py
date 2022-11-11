import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import  DEFAULT_TYPE,SHIELD_TYPE,RUNNING,JUMPING,DUCKING,RUNNING_SHIELD,DUCKING_SHIELD,JUMPING_SHIELD

RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_SPEED = 8.5
    Y_DUCKING = 350


    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.jump_speed = 8.5
        self.has_powe_up = False
        self.power_time_up = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_ducking = False
        self.clock = 3

    def update(self, user_input):
        if self.dino_run:
           self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_ducking:
            self.ducking()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_ducking = False

        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_ducking = False


        if user_input[pygame.K_DOWN] and not self.dino_ducking:
            self.dino_ducking = True
            self.dino_run = False


        if self.step_index >= 9:
            self.step_index = 0


    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type]
        self.dino_rect.y -= self.jump_speed * 2

        self.jump_speed -= 0.5
        if self.jump_speed < -self.JUMP_SPEED:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_speed = self.JUMP_SPEED

    def ducking(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_DUCKING
        self.step_index +=1







    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x,self.dino_rect.y))
