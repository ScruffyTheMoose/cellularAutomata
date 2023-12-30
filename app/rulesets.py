from constants import *
import numpy as np
import pygame


# https://en.wikipedia.org/wiki/Life-like_cellular_automaton


rules = {
    # B3/S23 - Life
    "life": {
        "survive": set([2, 3]),
        "birth": set([3])
    },
    # B34/S34 - 34 Life
    "34life": {
        "survive": set([3, 4]),
        "birth": set([3, 4])
    },
    # B35678/S5678 - Diamoeba
    "diamoeba": {
        "survive": set([5, 6, 7, 8]),
        "birth": set([3, 5, 6, 7, 8])
    },
    # B3/S012345678 - Life without Death
    "lwd": {
        "survive": set([0, 1, 2, 3, 4, 5, 6, 7, 8]),
        "birth": set([3])
    },
    # B1357/S1357 - Replicator
    "replicator": {
        "survive": set([1, 3, 5, 7]),
        "birth": set([1, 3, 5, 7])
    },
    # B2/S - Seeds
    "seeds": {
        "survive": set([]),
        "birth": set([2])
    },
    # B36/S125 - 2x2
    "2x2": {
        "survive": set([1, 2, 5]),
        "birth": set([3, 6])
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
                         row * size, size - 1, size - 1))

    return updated_cells
