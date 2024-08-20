import pygame
import random
import globals
from cellClass import Cell

def get_grid_dimensions():
    return globals.WIDTH // globals.SIZE, globals.HEIGHT // globals.SIZE

def caveMazeEller(window, gridCells):
    cols, rows = get_grid_dimensions()

    def removeWalls(startCell, endCell):
        if startCell.cordX - endCell.cordX == 1:  # Moving Left
            startCell.walls[3] = 0  # LEFT wall
            endCell.walls[1] = 0  # RIGHT wall
        elif startCell.cordX - endCell.cordX == -1:  # Moving Right
            startCell.walls[1] = 0  # RIGHT wall
            endCell.walls[3] = 0  # LEFT wall
        elif startCell.cordY - endCell.cordY == 1:  # Moving Up
            startCell.walls[0] = 0  # TOP wall
            endCell.walls[2] = 0  # BOTTOM wall
        elif startCell.cordY - endCell.cordY == -1:  # Moving Down
            startCell.walls[2] = 0  # BOTTOM wall
            endCell.walls[0] = 0  # TOP wall

    def merge_sets_horizontally(gridCells, cols, row, set1, set2):
        for col in range(cols):
            cell = gridCells[row * cols + col]
            if cell.setID == set2:
                cell.setID = set1

    def merge_sets_vertically(gridCells, cols, row, set1, set2):
        for col in range(cols):
            cell = gridCells[row * cols + col]
            if cell.setID == set2:
                cell.setID = set1

    def ellerAlgorithm():
        next_id = 1
        for row in range(rows):
            # Initialize sets for the first row
            for col in range(cols):
                cell = gridCells[row * cols + col]
                if cell.setID is None:
                    cell.setID = next_id
                    next_id += 1

            # Merge horizontally
            for col in range(cols - 1):
                cell = gridCells[row * cols + col]
                right_cell = gridCells[row * cols + col + 1]
                if cell.setID != right_cell.setID and random.choice([True, False]):
                    removeWalls(cell, right_cell)
                    merge_sets_horizontally(gridCells, cols, row, cell.setID, right_cell.setID)

            # Merge vertically
            if row < rows - 1:
                for col in range(cols):
                    cell = gridCells[row * cols + col]
                    down_cell = gridCells[(row + 1) * cols + col]
                    if random.choice([True, False]):
                        removeWalls(cell, down_cell)
                        down_cell.setID = cell.setID

            # Ensure all cells in the row have the same ID after merging
            if row < rows - 1:  # Only do this if not the last row
                for col in range(cols):
                    cell = gridCells[row * cols + col]
                    for next_col in range(col + 1, cols):
                        next_cell = gridCells[row * cols + next_col]
                        if cell.setID != next_cell.setID:
                            removeWalls(cell, next_cell)
                            merge_sets_horizontally(gridCells, cols, row, cell.setID, next_cell.setID)

        # Ensure in the last row that all cells have the same ID
        if rows > 1:  # Ensure there is more than one row
            last_row = rows - 1
            for col in range(cols - 1):
                cell = gridCells[last_row * cols + col]
                right_cell = gridCells[last_row * cols + col + 1]
                if cell.setID != right_cell.setID:
                    removeWalls(cell, right_cell)
                    merge_sets_horizontally(gridCells, cols, last_row, cell.setID, right_cell.setID)

            # Ensure all cells in the last row have the same ID
            last_set_id = gridCells[last_row * cols].setID
            for col in range(1, cols):
                cell = gridCells[last_row * cols + col]
                if cell.setID != last_set_id:
                    merge_sets_horizontally(gridCells, cols, last_row, last_set_id, cell.setID)

            # Merge vertically to ensure all cells are connected
            for row in range(rows - 1):
                for col in range(cols):
                    cell = gridCells[row * cols + col]
                    down_cell = gridCells[(row + 1) * cols + col]
                    if cell.setID != down_cell.setID:
                        removeWalls(cell, down_cell)
                        merge_sets_vertically(gridCells, cols, row + 1, cell.setID, down_cell.setID)

            # Update display
            window.fill(pygame.Color(40, 40, 40))
            for cell in gridCells:
                cell.display(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.flip()

            # Adjust speed
            if globals.CAVESPEED == 1:
                pygame.time.delay(1000)
            elif globals.CAVESPEED == 2:
                pygame.time.delay(100)
            elif globals.CAVESPEED == 3:
                pygame.time.delay(10)
            elif globals.CAVESPEED == 4:
                pygame.time.delay(0)

    ellerAlgorithm()

def mainMazeEllers(window, clock):
    print(f"\n\n MAIN MAZE\nSIZE: {globals.SIZE},\n globals.WALLWIDTH: {globals.WALLWIDTH},\n globals.FPS: {globals.FPS},\n globals.CAVESPEED: {globals.CAVESPEED}")

    # Create grid of cells
    cols, rows = get_grid_dimensions()
    gridCells = [Cell(col, row, (255, 255, 255), (0, 50, 140), (0, 175, 255)) for row in range(rows) for col in range(cols)]

    caveMazeEller(window, gridCells)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.fill(pygame.Color(40, 40, 40))

        # Display all cells
        for cell in gridCells:
            cell.display(window)

        pygame.display.flip()
        clock.tick(globals.FPS)