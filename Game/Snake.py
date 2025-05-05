from ursina import *
import pygame
from pygame.locals import *
import random
import time
import pyautogui as py



pygame.init()

pygame.mixer.init()







SIZE = 40

class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.image = pygame.image.load("food.png").convert()
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1, 500)
        self.y = random.randint(1, 500)


class Snake:

    def __init__(self, parent_screen, length):
        pygame.mixer.init()
        self.parent_screen = parent_screen
        self.block = pygame.image.load("game.png").convert()
        self.length = length
        self.x = [40]*length
        self.y = [40]*length
        self.direction = 'none'
        self.close = py
    def increase_length(self):
        self.length = self.length + 1
        self.x.append(-1)
        self.y.append(-1)


    def draw(self):
        self.parent_screen.fill((63, 204, 122))
        for i in range (self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()
        
    def right_block(self):
        self.direction = 'right'

    def left_block(self):
        self.direction = 'left'

    def up_block(self):
        self.direction = 'up'

    def down_block(self):
        self.direction = 'down'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'right':
            self.x[0] = self.x[0]+ 40
        elif self.direction == 'left':
            self.x[0] =  self.x[0]- 40
        elif self.direction == 'up':
            self.y[0] =  self.y[0]- 40
        elif self.direction == 'down' :
            self.y[0] =  self.y[0]+ 40
        self.draw()
        if self.x[0] > 1380:
            
            sound = pygame.mixer.Sound("over.flac")
            pygame.mixer.Sound.play(sound)

            
            raise "Game Over"
            

        if self.x[0] < 0:
            sound = pygame.mixer.Sound("over.flac")
            pygame.mixer.Sound.play(sound)

            
            raise "Game Over"
            
        if self.y[0] > 700:
            sound = pygame.mixer.Sound("over.flac")
            pygame.mixer.Sound.play(sound)

            
            raise "Game Over"
        

        if self.y[0] < 0:
            sound = pygame.mixer.Sound("over.flac")
            pygame.mixer.Sound.play(sound)

            
            raise "Game Over"


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.background_music()
        self.screen = pygame.display.set_mode((1380, 700))
        self.snake = Snake(self.screen, 1)
        self.snake.draw()

        self.apple = Apple(self.screen)
        self.apple.draw()

    def background_music(self):
        pygame.mixer.music.load("background.flac")
        pygame.mixer.music.play(-1, 0)
        
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 <= x2 + SIZE:
            if y1 >= y2 and y1 <= y2 + SIZE:
                return True
        return False
   

    def play(self):
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()

        #Colision Of Snake With Apple or when a snake bites a apple

        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

            self.sound = pygame.mixer.Sound("apple.flac")
            pygame.mixer.Sound.play(self.sound)




        #for i in range(2, self.snake.length):
            #if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                #print("Game Over")
                #exit(0)

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score, (1250, 10))

    def show_gameover(self):
        self.screen.fill((63, 204, 122))
        font = pygame.font.SysFont('arial', 30)
        line1 = font.render(f"Game Over: Your Score is {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(line1, (500, 300))

        line2 = font.render(f"To Play Again Press Enter To exit press Escape ", True, (255, 255, 255))
        self.screen.blit(line2, (500, 350 ))

        pygame.display.flip()

        pygame.mixer.music.pause()


    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)
    
    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:

                    if event.key == K_ESCAPE:
                            running = False

                    if event.key == K_RETURN:
                        py.press("esc")
                        pause = False
                        pygame.mixer.music.unpause()
                
                    if not pause:
                        if event.key == K_UP:
                            self.snake.up_block()
                        if event.key == K_DOWN:
                            self.snake.down_block()
                        if event.key == K_LEFT:
                            self.snake.left_block()
                        if event.key == K_RIGHT:
                            self.snake.right_block()
                elif event.type == QUIT:
                    running = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                    pause = True
                    self.show_gameover()
                    self.background_music()
                    self.reset()
            time.sleep(0.1)


if __name__ == "__main__":
    game = Game()
    game.run()
