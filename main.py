import random
import pygame

from config import Config
from kun import Kun
from bucket import Bucket
from tools import Tools


class IkunWhacAMoleGame:

    def __init__(self):
        self.initialize()

    def run(self):
        '''运行游戏'''
        while self.GamingInterface():
            continue

    def GamingInterface(self):
        '''游戏进行界面'''
        # 播放背景音乐
        Tools.playbgm(Config.BGM_PATH)
        # 加载字体
        font = pygame.font.Font(Config.FONT_PATH, 40)
        # 加载背景图片
        bg_img = self.image_back
        # 开始界面
        if not Tools.startInterface(self.screen, self.image_begin):
            return False
        # 坤坤改变位置的计时
        hole_pos = random.choice(Config.HOLE_POSITIONS)
        change_hole_event = pygame.USEREVENT
        pygame.time.set_timer(change_hole_event, 800)
        # 坤坤
        kun = Kun(self.image_kun, self.image_ji, hole_pos)
        # 篮球
        bucket = Bucket(self.bucket0, self.bucket1, (500, 250))
        # 时钟
        clock = pygame.time.Clock()
        # 分数
        your_score = 0
        flag = False
        # 初始时间
        init_time = pygame.time.get_ticks()
        # 游戏主循环
        while True:
            # --游戏时间为60s
            time_remain = round(
                (Config.TIMEOUT - (pygame.time.get_ticks() - init_time)) / 1000
            )
            # --游戏时间减少, 坤坤变位置速度变快
            if time_remain == 40 and not flag:
                hole_pos = random.choice(Config.HOLE_POSITIONS)
                kun.reset()
                kun.setPosition(hole_pos)
                pygame.time.set_timer(change_hole_event, 650)
                flag = True
            elif time_remain == 20 and flag:
                hole_pos = random.choice(Config.HOLE_POSITIONS)
                kun.reset()
                kun.setPosition(hole_pos)
                pygame.time.set_timer(change_hole_event, 500)
                flag = False
            # --倒计时音效
            if time_remain == 10:
                self.sound_count_down.play()
            # --游戏结束
            if time_remain < 0:
                break
            count_down_text = font.render(
                'Time: '+str(time_remain), True, Config.WHITE)
            # --按键检测
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False
                elif event.type == pygame.MOUSEMOTION:
                    bucket.setPosition(pygame.mouse.get_pos())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        bucket.setHammering()
                elif event.type == change_hole_event:
                    hole_pos = random.choice(Config.HOLE_POSITIONS)
                    kun.reset()
                    kun.setPosition(hole_pos)
            # --碰撞检测
            if bucket.is_hammering and not kun.is_hammer:
                is_hammer = pygame.sprite.collide_mask(bucket, kun)
                if is_hammer:
                    self.sound_nigama.play()
                    kun.setBeHammered()
                    your_score += 1
            # --分数
            your_score_text = font.render(
                f'Score: {your_score}', True, Config.BROWN
            )
            # --绑定必要的游戏元素到屏幕(注意顺序)
            self.screen.blit(bg_img, (0, 0))
            self.screen.blit(count_down_text, (875, 8))
            self.screen.blit(your_score_text, (800, 430))
            kun.draw(self.screen)
            bucket.draw(self.screen)
            # --更新
            pygame.display.flip()
            clock.tick(60)
        # 结束界面
        return Tools.endInterface(
            self.screen,
            self.image_end,
            self.image_again_1,
            self.image_again_2,
            your_score
        )

    def initialize(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(Config.TITLE)
        self.screen = pygame.display.set_mode(Config.SCREENSIZE)
        self.image_back = pygame.image.load(Config.IMAGE_BACK)
        self.image_begin = pygame.image.load(Config.IMAGE_BEGIN)
        self.image_end = pygame.image.load(Config.IMAGE_END)
        self.image_again_1 = pygame.image.load(Config.IMAGE_AGAIN_1)
        self.image_again_2 = pygame.image.load(Config.IMAGE_AGAIN_2)
        self.bucket0 = pygame.image.load(Config.IMAGE_BUCKET_0)
        self.bucket1 = pygame.image.load(Config.IMAGE_BUCKET_1)
        self.image_kun = pygame.image.load(Config.IMAGE_KUN)
        self.image_ji = pygame.image.load(Config.IMAGE_JI)
        self.sound_count_down = pygame.mixer.Sound(Config.SOUND_COUNTDONE)
        self.sound_nigama = pygame.mixer.Sound(Config.SOUND_NI_GAN_MA)


IkunWhacAMoleGame().run()
