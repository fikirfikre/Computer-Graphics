import pygame


class PlatformOne(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.fill((255, 0, 0))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(80, 550))


class PlatformTwo(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(120, 480))  # 150 - distance from right 350- distnace from top


class PlatformThree(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (220, 20))
        self.surf = pygame.Surface((220, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(170, 360))


class PlatformFour(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (100, 20))
        self.surf = pygame.Surface((100, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(50, 420))


class PlatformSix(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (100, 20))
        self.surf = pygame.Surface((100, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(280, 510))


class PlatformSeven(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(330, 450))


class PlatformEight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(280, 300))


class PlatformNine(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(50, 300))


class PlatformFive(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (700, 20))
        self.surf = pygame.Surface((700, 20))
        self.surf.fill((255, 0, 0))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(150, 50))


class PlatformTen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(120, 170))


class PlatformEleven(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(20, 200))


class PlatformTwelve(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(120, 250))


class PlatformThirteen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(430, 250))


class PlatformFourteen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (700, 20))
        self.surf = pygame.Surface((700, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(900, 50))


class PlatformFifteen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(300, 120))
#
#
# class PlatformSixteen(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#
#         bg_img = pygame.image.load(r"..\images\plat.jpg")
#         bg_img = pygame.transform.scale(bg_img, (450, 20))
#         self.surf = pygame.Surface((450, 20))
#         self.surf.blit(bg_img, (0, 0))
#         self.rect = self.surf.get_rect(center=(450, 50))
#
#
# class PlatformSeventeen(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         bg_img = pygame.image.load(r"..\images\plat.jpg")
#         bg_img = pygame.transform.scale(bg_img, (300, 20))
#         self.surf = pygame.Surface((300, 20))
#         self.surf.blit(bg_img, (0, 0))
#         self.rect = self.surf.get_rect(center=(450, 50))


class PlatformEighteen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (1000, 40))
        self.surf = pygame.Surface((1000, 40))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(500, 630))


class PlatformNineteen(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(210, 200))


class Platform1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.fill((255, 0, 0))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(900, 550))


class Platform2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(850, 480))  # 150 - distance from right 350- distnace from top


class Platform3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (220, 20))
        self.surf = pygame.Surface((220, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(800, 360))


class Platform4(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (100, 20))
        self.surf = pygame.Surface((100, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(950, 420))


class Platform5(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (100, 20))
        self.surf = pygame.Surface((100, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(700, 510))


class Platform6(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(580, 450))


class Platform7(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(950, 300))


class Platform8(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(730, 300))


class Platform15(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.fill((255, 0, 0))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(540,300))


class Platform9(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(820, 170))


class Platform10(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (50, 20))
        self.surf = pygame.Surface((50, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(980, 200))


class Platform11(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(880, 250))


class Platform12(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(650, 250))


class Platform14(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (250, 20))
        self.surf = pygame.Surface((250, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(550, 180))


class Platform13(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bg_img = pygame.image.load(r"..\images\plat.jpg")
        bg_img = pygame.transform.scale(bg_img, (130, 20))
        self.surf = pygame.Surface((130, 20))
        self.surf.blit(bg_img, (0, 0))
        self.rect = self.surf.get_rect(center=(700, 120))
