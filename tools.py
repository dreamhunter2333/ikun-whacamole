import pygame

from config import Config


class Tools:

    @staticmethod
    def playbgm(bgm_path: str) -> None:
        pygame.mixer.music.load(bgm_path)
        pygame.mixer.music.play(-1, 0.0)

    @staticmethod
    def startInterface(screen, begin_image):
        '''游戏开始界面'''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return True
            screen.blit(begin_image, (0, 0))
            pygame.display.update()

    @staticmethod
    def endInterface(screen, end_image, again_image0, again_image1, your_score):
        '''结束界面'''
        again_image = again_image0
        font = pygame.font.Font(Config.FONT_PATH, 50)
        your_score_text = font.render(
            f'ikun Score: {your_score}', True, Config.RED
        )
        your_score_rect = your_score_text.get_rect()
        your_score_rect.left = (
            Config.SCREENSIZE[0] - your_score_rect.width
        ) / 2
        your_score_rect.top = 215
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] in list(range(419, 574)) and mouse_pos[1] in list(range(374, 416)):
                        again_image = again_image1
                    else:
                        again_image = again_image0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if event.button == 1 and mouse_pos[0] in list(range(419, 574)) and mouse_pos[1] in list(range(374, 416)):
                        return True
            screen.blit(end_image, (0, 0))
            screen.blit(again_image, (416, 370))
            screen.blit(your_score_text, your_score_rect)
            pygame.display.update()
