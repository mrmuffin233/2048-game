import random,sys,pygame

from settings import Settings
from game_functions import *

def run_game():
    #标题
    pygame.display.set_caption("2048")
    add_number()
    add_number()

    while True:
        screen.fill(settings.bg_color)#这个操作有清除之前绘制内容的作用，必须放在循环内。
        draw_grid()
        check_if_over()
        check_events()
        show_score()

        pygame.display.flip()

run_game()