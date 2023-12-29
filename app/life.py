import time
import pygame
import numpy as np

COLOR_BG = (0, 255, 0)  # will show green if missing cells
COLOR_GRID = (40, 40, 40)
COLOR_DIE = (255, 100, 100)
COLOR_ALIVE = (255, 255, 255)
DISPLAY_SIZE = (1000, 800)
CELL_WIDTH = 10


def update(screen, cells, size=CELL_WIDTH, with_progress=False):
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


def main():
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
