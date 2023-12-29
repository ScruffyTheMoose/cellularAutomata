from constants import *
import numpy as np
import pygame


def life(screen, cells, size=CELL_WIDTH, with_progress=False):
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1: row + 2, col -
                       1: col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE

        if cells[row, col] == 1:
            if alive < 2 or alive > 3:
                if with_progress == True:
                    color = COLOR_DIE

            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE

        else:
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE

        pygame.draw.rect(screen, color, (col * size,
                         row * size, size, size))

    return updated_cells
