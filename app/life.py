import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 800 # window dimensions
GRID_SIZE = 100 # (100, 100) world size
CELL_SIZE = WIDTH // GRID_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
NEIGHBORS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)] # for checking the next state of a cell

# Initialize Pygame
pygame.init()

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Initialize a world of dead cells
grid = np.zeros((GRID_SIZE, GRID_SIZE))

# Main loop
# begin static so user can select live cells
running = False

while True:
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            pygame.quit()
            exit
        
        # start/stop
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running # negate the current state
        
        # switch state of cell when clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # getting relative position of cell
            x, y = pygame.mouse.get_pos()
            grid_col = x // GRID_SIZE
            grid_row = y // GRID_SIZE
            grid[grid_row, grid_col] = 1 - grid[grid_row, grid_col]
            
            # updating the world
            screen.fill(BLACK)
            for i in range(GRID_SIZE):
                for j in range(GRID_SIZE):
                    if grid[i, j] == 1:
                        color = WHITE
                    else:
                        color = BLACK
                    pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            

    # Update the grid (implement Conway's rules here)
    new_grid = np.copy(grid)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # summing the surrounding cell state values
            total = 0
            for r, c in NEIGHBORS:
                nr = i - r
                nc = j - c
                if 0 <= nr < GRID_SIZE and 0 <= nc < GRID_SIZE:
                    total += grid[nr, nc]
                
            if total < 2 or total > 3:
                new_grid[i, j] = 0
            else:
                new_grid[i, j] = 1

    grid = np.copy(new_grid)

    # Draw the grid
    screen.fill(BLACK)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i, j] == 1:
                color = WHITE
            else:
                color = RED
            pygame.draw.rect(screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(10)  # Adjust the argument for desired frames per second

# Quit Pygame
pygame.quit()
