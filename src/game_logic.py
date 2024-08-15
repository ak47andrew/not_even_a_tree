import random
from config import LINE_LENGTH, SET_BORDER_GAMERULE, SCREEN_HEIGHT, SCREEN_WIDTH, STARTING_POS
import pygame
from colors import LINE, BG

def gen_new_end_pos(end_pos: tuple[int, int], last_direction: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    while True:
        n = (random.randint(-1, 1), random.randint(-1, 1))
        if n != last_direction:
            break
    new_end_pos = (end_pos[0] + (LINE_LENGTH * n[0]), end_pos[1] + (LINE_LENGTH * n[1]))

    if SET_BORDER_GAMERULE:
        new_end_pos = (
            max(LINE_LENGTH, min(new_end_pos[0], SCREEN_WIDTH - LINE_LENGTH)),
            max(LINE_LENGTH, min(new_end_pos[1], SCREEN_HEIGHT - LINE_LENGTH))
        )
        
    return new_end_pos, n


def initialize_game(screen):
    global LINE
    end_pos: tuple[int, int] = STARTING_POS
    last_dir: tuple[int, int] = (0, 0)
    
    screen.fill(BG)
    pygame.draw.line(screen, LINE, end_pos, end_pos)
    
    return end_pos, last_dir
