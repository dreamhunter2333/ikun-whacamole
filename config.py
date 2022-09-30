import os

ROOT_DIR = os.path.dirname(__file__)


class Config:
    # 根目录
    # FPS
    FPS = 100
    # 屏幕大小
    SCREENSIZE = (993, 477)
    TIMEOUT = 61000
    # 标题
    TITLE = '打地鼠 - 鸡你太美 ikun 版'
    # 游戏常量参数
    HOLE_POSITIONS = [
        (90, -20), (405, -20), (720, -20),
        (90, 140), (405, 140), (720, 140),
        (90, 290), (405, 290), (720, 290)
    ]
    BROWN = (150, 75, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    # 背景音乐路径
    BGM_PATH = os.path.join(ROOT_DIR, 'resources/audios/bgm.mp3')
    SOUND_COUNTDONE = os.path.join(ROOT_DIR, 'resources/audios/count_down.wav')
    SOUND_NI_GAN_MA = os.path.join(ROOT_DIR, 'resources/audios/niganma.mp3')

    IMAGE_BUCKET_0 = os.path.join(ROOT_DIR, 'resources/images/bucket0.png')
    IMAGE_BUCKET_1 = os.path.join(ROOT_DIR, 'resources/images/bucket1.png')
    IMAGE_BEGIN = os.path.join(ROOT_DIR, 'resources/images/begin.png')
    IMAGE_BACK = os.path.join(ROOT_DIR, 'resources/images/background.png')
    IMAGE_END = os.path.join(ROOT_DIR, 'resources/images/end.png')
    IMAGE_AGAIN_1 = os.path.join(ROOT_DIR, 'resources/images/again1.png')
    IMAGE_AGAIN_2 = os.path.join(ROOT_DIR, 'resources/images/again2.png')
    IMAGE_KUN = os.path.join(ROOT_DIR, 'resources/images/kun.png')
    IMAGE_JI = os.path.join(ROOT_DIR, 'resources/images/ji.png')

    # 字体路径
    FONT_PATH = os.path.join(ROOT_DIR, 'resources/fonts/Gabriola.ttf')
