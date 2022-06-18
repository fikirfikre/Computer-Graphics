import pygame
import sys
from OpenGL.GL import *

from pygame.locals import *

# from screens.PlayerScreen import PlayerScreen, Screen
# from screens.start import Start

HEIGHT = 650
WIDTH = 1000


class GameOver:

    def draw_text(self, x, y, text, size):
        font = pygame.font.SysFont('arial', size, True)
        textSurface = font.render(text, True, (255, 0,0,255)).convert_alpha()
        textData = pygame.image.tostring(textSurface, "RGBA", True)
        glWindowPos2d(x, y)
        glDrawPixels(textSurface.get_width(), textSurface.get_height(), GL_RGBA, GL_UNSIGNED_BYTE, textData)
    def main(self):
        pygame.display.set_mode((WIDTH, HEIGHT), OPENGL | DOUBLEBUF)
        glEnable(GL_BLEND)
        surf = pygame.image.load(r"..\images\bgstart.jpg")
        bg_img = pygame.transform.scale(surf, (WIDTH, HEIGHT))
        s = pygame.image.tostring(bg_img, 'RGBA')
        texID = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texID)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, WIDTH, HEIGHT, 0, GL_RGBA, GL_UNSIGNED_BYTE, s)
        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, 0)
       

    # create pygame clock
        pygame.init()
        MAINCLOCK = pygame.time.Clock()

        while True:
            # get quit event
            mousex, mousey = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                print(mousex)
                print(mousey)
                if 461 < mousex < 506 and 425 < mousey < 440:
                    if event.type == pygame.MOUSEBUTTONUP:
                        sys.exit()


                # if 453 < mousex < 541 and 325 < mousey < 344:
                #     if event.type == pygame.MOUSEBUTTONUP:
                #         if __name__ == '__main__':
                #             Start()

            # prepare to render screen
            glClear(GL_COLOR_BUFFER_BIT)
            glLoadIdentity()
            glDisable(GL_LIGHTING)
            glEnable(GL_TEXTURE_2D)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
            glClearColor(0, 0, 0, 1.0)

            # draw texture
            glBindTexture(GL_TEXTURE_2D, texID)
            glBegin(GL_QUADS)
            glTexCoord2f(0, 0); glVertex2f(1, 1)
            glTexCoord2f(0, 1); glVertex2f(1, -1)
            glTexCoord2f(1, 1); glVertex2f(-1, -1)
            glTexCoord2f(1, 0); glVertex2f(-1, 1)
            glEnd()

            #draw rectangle
            glColor3fv((1, 1, 1))
            GameOver().draw_text(380, 380, "GAME OVER", 40)
            GameOver().draw_text(460, 200, "QUIT", 26)

            pygame.display.flip()
            MAINCLOCK.tick(60)

