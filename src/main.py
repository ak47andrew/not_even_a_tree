import pygame
import os
from config import SCREEN_HEIGHT, SCREEN_WIDTH, CAPTION, TIMEOUT
from game_logic import initialize_game, gen_new_end_pos
from colors import LINE, get_new_color

pygame.init()


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)


def main():
    global LINE
    end_pos, last_dir = initialize_game(screen)
    color = LINE
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        new_end_pos, last_dir = gen_new_end_pos(end_pos, last_dir)
        pygame.draw.line(screen, color, end_pos, new_end_pos)        
        end_pos = new_end_pos
        color = get_new_color(color)
        
        pygame.display.update()
        pygame.time.delay(TIMEOUT)


if __name__ == "__main__":
    main()
