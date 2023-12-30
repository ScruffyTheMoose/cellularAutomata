from constants import *
import numpy as np
import pygame

rules = {
    "life": {
        "survive": set([2, 3]),
        "birth": set([3])
    },
    "34life": {
        "survive": set([3, 4]),
        "birth": set([3, 4])
    },
    "diamoeba": {
        "survive": set([5, 6, 7, 8]),
        "birth": set([3, 5, 6, 7, 8])
    },
    "lwd": {
        "survive": set([0, 1, 2, 3, 4, 5, 6, 7, 8]),
        "birth": set([3])
    },
    "replicator": {
        "survive": set([1, 3, 5, 7]),
        "birth": set([1, 3, 5, 7])
    },
}


def update(screen, cells, rule: dict, size=CELL_WIDTH, with_progress=False) -> np.ndarray:
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    survive = rules[rule]["survive"]
    birth = rules[rule]["birth"]

    for row, col in np.ndindex(cells.shape):
        alive = np.sum(cells[row - 1: row + 2, col -
                       1: col + 2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_ALIVE

        # survive
        if cells[row, col] == 1:
            if alive not in survive:
                if with_progress == True:
                    color = COLOR_DIE

            else:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE

        # birth
        else:
            if alive in birth:
                updated_cells[row, col] = 1
                if with_progress:
                    color = COLOR_ALIVE

        pygame.draw.rect(screen, color, (col * size,
                         row * size, size, size))

    return updated_cells
