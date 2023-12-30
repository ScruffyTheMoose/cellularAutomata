import time
import pygame
import numpy as np

import rulesets as rs
from constants import *


def main(update=rs.life):
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    # matrix of cells specific to size of game display and individual cell
    cells = np.zeros(
        (DISPLAY_SIZE[1] // CELL_WIDTH, DISPLAY_SIZE[0] // CELL_WIDTH))
    screen.fill(COLOR_GRID)
    update(screen, cells)

    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells)
                    pygame.display.update()

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // CELL_WIDTH, pos[0] // CELL_WIDTH] = 1
                update(screen, cells)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells = update(screen, cells, with_progress=True)
            pygame.display.update()

            # slow down refresh rate to better observe evolution
            time.sleep(0.01)

        else:
            # faster refresh rate for smooth editing
            time.sleep(0.001)


if __name__ == "__main__":
    main()