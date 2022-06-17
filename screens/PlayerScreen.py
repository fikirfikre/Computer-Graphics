import sys
import time
import pygame
from OpenGL.GL import *
from platforms.Platforms import *
from pygame.locals import *

from screens.GameOverScreen import GameOver
from screens.WinnerScreen import Winner

HEIGHT = 650
WIDTH = 1000
FPS = 60
class PlayerScreen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.direction = pygame.math.Vector2(0, 0)
        self.all_platform = pygame.sprite.Group()
        self.player = pygame.sprite.Group()
        bg_img = pygame.image.load(r"..\images\ballThree.png")
        self.surf = pygame.transform.scale(bg_img, (30, 30))

        self.rect = self.surf.get_rect()
        self.rect.x = 10
        self.rect.y = 520
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        self.gravity = 0
        self.isjump = False
        self.winner = False
        self.startTime=time.time()

    def addPlatform(self):

        self.all_platform.add(PlatformOne())
        self.all_platform.add(PlatformTwo())
        self.all_platform.add(PlatformThree())
        self.all_platform.add(PlatformFour())
        self.all_platform.add(PlatformFive())
        self.all_platform.add(PlatformSix())
        self.all_platform.add(PlatformSeven())
        self.all_platform.add(PlatformEight())
        self.all_platform.add(PlatformNine())
        self.all_platform.add(PlatformTen())
        self.all_platform.add(PlatformEleven())
        self.all_platform.add(PlatformTwelve())
        self.all_platform.add(PlatformThirteen())
        self.all_platform.add(PlatformFourteen())
        self.all_platform.add(PlatformFifteen())
        self.all_platform.add(PlatformEighteen())
        self.all_platform.add(PlatformNineteen())
        self.all_platform.add(Platform1())
        self.all_platform.add(Platform2())
        self.all_platform.add(Platform3())
        self.all_platform.add(Platform4())
        self.all_platform.add(Platform5())
        self.all_platform.add(Platform6())
        self.all_platform.add(Platform7())
        self.all_platform.add(Platform8())
        self.all_platform.add(Platform9())
        self.all_platform.add(Platform10())
        self.all_platform.add(Platform11())
        self.all_platform.add(Platform12())
        self.all_platform.add(Platform13())
        self.all_platform.add(Platform14())
        self.all_platform.add(Platform15())


    def addPlayer(self):
        self.player.add(Screen)

    def move(self):

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.direction.x = -5
        elif pressed_keys[K_RIGHT]:
            self.direction.x = 5
        else:
            self.direction.x = 0

        if pressed_keys[K_SPACE] and self.isjump == False:
            self.rect.bottom += 1
            hits = pygame.sprite.spritecollide(self,self.all_platform,False)
            self.rect.bottom -= 1
            if hits:

               self.gravity = -7

            self.isjump = True

        if pressed_keys[K_SPACE]:
            self.isjump = False

        self.gravity += 1
        if self.gravity > 10:
            self.gravity = 10
        self.direction.y += self.gravity


        for platform in self.all_platform:

            if platform.rect.colliderect(self.rect.x + self.direction.x, self.rect.y, self.height, self.width):
                self.direction.x = 0

            if platform.rect.colliderect(self.rect.x, self.rect.y + self.direction.y, self.height, self.width):
                if self.direction.y > 0:  # gravity less than zero jumping
                    self.rect.bottom = platform.rect.top
                    self.direction.y = 0
                    # self.isjump=True

                elif self.direction.y < 0:
                    self.rect.top = platform.rect.bottom
                    self.direction.y = 0

        if self.isjump and self.direction.y != 0:
            self.isjump = False

        self.rect.x += self.direction.x
        self.rect.y += self.direction.y
        print(self.rect.bottom)
        if self.rect.bottom < 0:
            # f.mainFrame()
            self.direction.y = 0
            print("h")
            # sys.exit()
            self.winner = True
        if self.rect.bottom > HEIGHT:
            # self.rect.bottom = HEIGHT
            self.direction.y = 0
        if self.rect.x > WIDTH:
            print(self.rect.x)
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH



    def main(self):
        pygame.init()

        FramePerSec = pygame.time.Clock()

        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Game")
        bg_img = pygame.image.load(r"..\images\bg.jpg")
        bg_img = pygame.transform.scale(bg_img, (WIDTH, HEIGHT))
        time_limit = 20
        # start_time = time.time()
        Screen.addPlatform()
        Screen.addPlayer()

        while True:

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            display_surface.blit(bg_img, (0, 0))
            # display_surface.fill((0,0,0))
            for entity in self.all_platform:
                display_surface.blit(entity.surf, entity.rect)
            for player in self.player:
                display_surface.blit(player.surf,player.rect)
            Screen.move()

            elapsed_time = time.time() - self.startTime
            print(time_limit - elapsed_time)


            if elapsed_time > time_limit and Screen.winner == False:
                print("GAME OVer")
                GameOver().main()
            elif(Screen.winner == True):
                print("Winner")
                Winner().main()
                sys.exit()
            pygame.display.update()
            FramePerSec.tick(FPS)
    # time_limit = 10
Screen = PlayerScreen()


