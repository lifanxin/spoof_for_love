# -*- coding: utf-8 -*-
"""Spoof for love.

Introduce:
    it just a spoof, maybe you can use it for court the girl.
    the girl can't refuse you in this program, but if she
    still can't accept you, please don't cry.

Notice:
    if your folder path include Chinese character, it may be
    raise exception when you run this module. of course in
    this module, I use many constants from 'constant.py', you
    can alter them if them don't match your taste.

The last:
    in data folder, also has another interesting font, image
    and music. you can use it for fun!

python: 3.4.4
Copyright @lifanxin
"""

import sys
import random

import pygame
from pygame.locals import *

from constant import *


def ct_text(content, screen, color, pos, size):
    """Create the text."""
    text = pygame.font.Font(FONT, size)
    text_render = text.render(content, True, color)
    text_rect = text_render.get_rect()
    text_rect.center = pos
    screen.blit(text_render, text_rect)


def ct_button(title, screen, color, rect, thickness=0):
    """Create button."""
    pygame.draw.rect(screen, color, rect, thickness)
    ct_text(title, screen, WHITE, rect.center, FONT_SIZE)


def get_random_pos():
    """Generate random position."""
    x = random.randint(0, SCREEN_WIDTH - BUTTON_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT - BUTTON_HEIGHT)
    return x, y


def mv_button(rect):
    """Move button randomly."""
    x, y = pygame.mouse.get_pos()
    if rect.collidepoint(x, y):
        new_x, new_y = get_random_pos()
        return (new_x, new_y)
    return (None, None)


def main():
    """Run the logic in here."""
    # init window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(SCREEN_TITLE)
    fps_clock = pygame.time.Clock()

    # play music
    pygame.mixer.music.load(MUSIC)
    pygame.mixer.music.play(MUSIC_LOOP_TIME, MUSIC_START_TIME)
    pygame.mixer.music.set_volume(MUSIC_VOLUME)

    # load image
    img_sf = pygame.image.load(IMAGE).convert()
    img_rect = img_sf.get_rect()
    img_rect.midtop = (HALF_WIDTH, SCREEN_MARGIN)

    # say something
    text_pos = (HALF_WIDTH, img_rect.bottom + (FONT_SIZE + SCREEN_MARGIN) / 2)

    # put button
    l_but_x = QUARTER_WIDTH - BUTTON_WIDTH / 2
    b_but_x = HALF_WIDTH + l_but_x
    but_y = SCREEN_HEIGHT - BUTTON_HEIGHT - SCREEN_MARGIN
    lucky_button_rect = pygame.Rect(l_but_x, but_y,
                                    BUTTON_WIDTH, BUTTON_HEIGHT)
    bad_button_rect = pygame.Rect(b_but_x, but_y,
                                  BUTTON_WIDTH, BUTTON_HEIGHT)

    # main loop
    accept = False
    while True:
        screen.fill(PINK)

        if accept:
            ct_text(THE_LAST_SURFACE_TEXT, screen, WHITE, CENTER, FONT_SIZE)
            for event in pygame.event.get():
                # when she accept it, the window is allowed to close!
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        else:
            screen.blit(img_sf, img_rect)
            ct_button(LUCKY_TEXT, screen, PALEPINK, lucky_button_rect)
            ct_button(BAD_TEXT, screen, PALEPINK, bad_button_rect)
            ct_text(THE_FIRST_SURFACE_TEXT, screen, WHITE, text_pos, FONT_SIZE)

            for event in pygame.event.get():
                # can't close the window
                if event.type == MOUSEMOTION:
                    pos = mv_button(bad_button_rect)
                    if pos[0]:
                        bad_button_rect.x = pos[0]
                        bad_button_rect.y = pos[1]
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if lucky_button_rect.collidepoint(x, y):
                        accept = True

        pygame.display.update()
        fps_clock.tick(FPS)


# the program say go
if __name__ == '__main__':
    main()
