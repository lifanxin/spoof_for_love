# -*- coding: utf-8 -*-
"""
Constant file.

include the screen parameters, special point coords,
data file path, the RGB's order of color and more.

you can alter some parameters make sure it work like you want.
but be careful for do that, it may cause some interesting bugs.
"""

FPS = 60
SCREEN_WIDTH = 680
SCREEN_HEIGHT = 540
SCREEN_MARGIN = 20
SCREEN_TITLE = 'Spoof for love!'
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50
assert (BUTTON_WIDTH * 4 < SCREEN_WIDTH) and \
       (BUTTON_HEIGHT * 4 < SCREEN_HEIGHT), \
       "please make sure the button small or screen big!"

HALF_WIDTH = SCREEN_WIDTH / 2
HALF_HEIGHT = SCREEN_HEIGHT / 2
QUARTER_WIDTH = SCREEN_WIDTH / 4
QUARTER_HEIGHT = SCREEN_HEIGHT / 4
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
LEFT_TOP_QUARTER = (SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4)
LEFT_BOTTOM_QUARTER = (SCREEN_WIDTH / 4, CENTER[1] + SCREEN_HEIGHT / 4)
RIGHT_TOP_QUARTER = (CENTER[0] + SCREEN_WIDTH / 4, SCREEN_HEIGHT / 4)
RIGHT_BOTTOM_QUARTER = (CENTER[0] + SCREEN_WIDTH / 4,
                        CENTER[1] + SCREEN_HEIGHT / 4)

FONT = './fonts/AlexaStd.otf'
IMAGE = './images/propose.jpg'
MUSIC = './music/SakuraTears.mp3'

# RGB's order of color
# choose what color of you like
PINK = (255, 128, 128)
PALEPINK = (255, 192, 203)
GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

MUSIC_LOOP_TIME = -1  # -1 means always play
MUSIC_START_TIME = 0.0  # the song play from where
MUSIC_VOLUME = 0.25  # the song's volume

LUCKY_TEXT = 'I do'
BAD_TEXT = 'Fuck off'

FONT_SIZE = 30
THE_FIRST_SURFACE_TEXT = 'Would you marry me?'
THE_LAST_SURFACE_TEXT = 'I know you will accept it!'
