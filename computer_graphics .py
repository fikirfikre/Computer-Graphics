import sys
import pygame
from pygame import *
import  time

HEIGHT = 550
WIDTH = 500
FPS = 60


class platform1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(50, 500))


class platform2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((0, 255, 0))
        self.rect = self.surf.get_rect(center=(150, 450))  # 150 - distance from right 350- distnace from top


class platform3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(200, 400))


class platform4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(400, 420))


class platform6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(330, 450))


class platform7(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(300, 350))


class platform8(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(450, 300))


class platform9(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(50, 300))


class platform5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((450, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(50, 50))


class platform10(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(250, 250))


class platform11(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(150, 200))


class platform12(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(90, 250))


class platform13(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(430, 250))


class platform14(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((250, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(450, 50))


class platform15(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((100, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(300, 100))


class platform16(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((250, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(450, 50))


class platform17(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((250, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(450, 50))
class platform18(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((1000, 10))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(500, 545))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128, 255, 40))
        self.rect = self.surf.get_rect()
        self.rect.x = 10
        self.rect.y = 520
        self.width = self.surf.get_width()
        self.height = self.surf.get_height()
        self.gravity = 0
        self.isjump = False
        self.winner = False

        self.direction = pygame.math.Vector2(0, 0)
        self.all_platform = pygame.sprite.Group()

    def add(self):
        self.all_platform.add(platform1())
        self.all_platform.add(platform2())
        self.all_platform.add(platform3())
        self.all_platform.add(platform4())
        self.all_platform.add(platform5())
        self.all_platform.add(platform6())
        self.all_platform.add(platform7())
        self.all_platform.add(platform8())
        self.all_platform.add(platform9())
        self.all_platform.add(platform10())
        self.all_platform.add(platform11())
        self.all_platform.add(platform12())
        self.all_platform.add(platform13())
        self.all_platform.add(platform14())
        self.all_platform.add(platform15())
        self.all_platform.add(platform16())
        self.all_platform.add(platform17())
        self.all_platform.add(platform18())

    def move(self):

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.direction.x = -5
        elif pressed_keys[K_RIGHT]:
            self.direction.x = 5
        else:
            self.direction.x = 0

        if pressed_keys[K_SPACE] and self.isjump == False:
            self.gravity = -5
            self.isjump = True

        if pressed_keys[K_SPACE]:
            self.isjump = False

        self.gravity += 1
        if self.gravity > 10:
            self.gravity = 10
        self.direction.y += self.gravity
        # self.rect.y += self.direction.y
        # detection of collision
        # collison to top

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
        if self.rect.bottom < HEIGHT:
            print("Winner")
            self.winner = True

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            self.direction.y = 0
        if self.rect.x > WIDTH:
            print(self.rect.x)
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = WIDTH






class main():
    pygame.init()

    FramePerSec = pygame.time.Clock()

    displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game")
    player = pygame.sprite.Group()
    P1 = Player()
    player.add(P1)
    P1.add()
    time_limit = 5
    start_time = time.time()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        displaysurface.fill((0, 0, 0))

        # JUMP -= 1
        # print(JUMP)
        P1.move()
        # P1.jump()
        for entity in P1.all_platform:
            displaysurface.blit(entity.surf, entity.rect)
        displaysurface.blit(P1.surf, P1.rect)
        pygame.display.update()
        FramePerSec.tick(FPS)
        elapsed_time = time.time()-start_time
        print(time_limit-elapsed_time)
        print(P1.winner)
        if elapsed_time > time_limit and P1.winner == False:
            print("GAME OVer")
            sys.exit()
        # elif(P1.winner == True):
        #     print("Winner")
        #     sys.exit()


# time_limit = 10

main()
# start_time = 10
# while start_time>0:
#             m,s =divmod(start_time,60)
#             h,m = divmod(m,60)
#             print(str(h).zfill(2)+ ":" + str(m).zfill(2)+ ":" + str(s).zfill(2))
#             time.sleep(1)
#             start_time -=1
