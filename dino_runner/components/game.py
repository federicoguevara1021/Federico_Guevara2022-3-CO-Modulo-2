import pygame

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS , FONT_STYLE
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import  DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.score = 0
        self.high_score = 0
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager
        self.running = False
        self.death_count = 0



    def execute(self):
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()


    def run(self):
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self,):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self)
        self.update_score()
        self.highest_score()


    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_power_up_time()
        self.draw_score()
        pygame.display.update()
        pygame.display.flip()


    def show_menu(self):
        if self.death_count == 0:
            self.screen.fill((255,255,255))
            half_screen_heigth = SCREEN_HEIGHT //2
            half_screen_width = SCREEN_WIDTH //2

            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("press any key to start... ", True , (0,128,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width,half_screen_heigth)
            self.screen.blit(text, text_rect)
        else:
            self.screen.fill((255,255,255))
            half_screen_heigth = SCREEN_HEIGHT //2
            half_screen_width = SCREEN_WIDTH //2

            font = pygame.font.Font(FONT_STYLE, 30)
            text = font.render("GAME OVER. Press any key to restar. ", True, (255, 0, 0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_heigth-50)

            score_text = font.render(f"Your score: {self.score}",True,(255, 0, 0))
            score_text_rect = score_text.get_rect()
            score_text_rect.x = (half_screen_width-100)
            score_text_rect.y = (half_screen_heigth+50)


            hscore_text = font.render(f"Highest score: {self.high_score}",True,(255, 0, 0))
            hscore_text_rect = hscore_text.get_rect()
            hscore_text_rect.x = (half_screen_width-100)
            hscore_text_rect.y = (half_screen_heigth+100)

            deaths_text =font.render(f"Total deaths: {self.death_count}",True,(255, 0, 0))
            deaths_text_rect = deaths_text.get_rect()
            deaths_text_rect.x = (half_screen_width-100)
            deaths_text_rect.y = (half_screen_heigth+150)




            self.screen.blit(ICON,(half_screen_width-50,half_screen_heigth-240))
            self.screen.blit(score_text,score_text_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(hscore_text,hscore_text_rect)
            self.screen.blit(deaths_text,deaths_text_rect)


        pygame.display.update()
        self.handle_events_on_menu()

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 30)
        text = font.render(f"Score: {self.score}" ,True,(255, 0, 255))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text,text_rect)

    def draw_power_up_time(self):
        if self.player.has_powe_up:
            time_to_show = round((self.player.power_time_up- pygame.time.get_ticks())/1000 ,2)
            if time_to_show >= 0:
                draw_message=(f"{self.player.type} enable for {time_to_show} seconds", self.screen)
            else:
                self.player.has_powe_up = False
                self.player.type = DEFAULT_TYPE



    def update_score(self):
        self.score += 1
        if self.score % 100 == 0 and self.game_speed <500:
            self.game_speed += 5


    def highest_score(self):
        if self.high_score>self.score:
            self.high_score = self.high_score

        elif self.high_score<= self.score:
            self.high_score = self.score

    def reset(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self)
        self.score=0
        self.game_speed = 20
        self.playing = True


    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
