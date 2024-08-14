import pygame
import random
import globals
from cellClass import Cell

def get_grid_dimensions():
    return globals.WIDTH // globals.SIZE, globals.HEIGHT // globals.SIZE

def caveMazePrins(window, gridCells):
    cols, rows = get_grid_dimensions()

    # Choose a random start cell and mark it as visited
    start_cell = random.choice(gridCells)
    start_cell.visited = True
    start_cell.current = True

    # Initialize the walls list with the walls of the initial cell
    walls = [(start_cell, direction) for direction in range(4)]  # 0: TOP, 1: RIGHT, 2: BOTTOM, 3: LEFT

    def get_neighbor(cell, direction):
        # The return is the cell that is in the orientention by a formula -> (gridCells is on 1D array)
        col, row = cell.cordX, cell.cordY
        if direction == 0 and row > 0:  # TOP
            return gridCells[(row - 1) * cols + col]
        elif direction == 1 and col < cols - 1:  # RIGHT
            return gridCells[row * cols + (col + 1)]
        elif direction == 2 and row < rows - 1:  # BOTTOM
            return gridCells[(row + 1) * cols + col]
        elif direction == 3 and col > 0:  # LEFT
            return gridCells[row * cols + (col - 1)]
        return None

    def removeWalls(startCell, endCell):
        if startCell.cordX - endCell.cordX == 1: # Moving Left
            startCell.walls[3] = 0  # LEFT wall
            endCell.walls[1] = 0  # RIGHT wall

        elif startCell.cordX - endCell.cordX == -1: # Moving Right 
            startCell.walls[1] = 0  # RIGHT wall
            endCell.walls[3] = 0  # LEFT wall

        elif startCell.cordY - endCell.cordY == 1: # Moving Up
            startCell.walls[0] = 0  # TOP wall
            endCell.walls[2] = 0  # BOTTOM wall

        elif startCell.cordY - endCell.cordY == -1: # Moving Down
            startCell.walls[2] = 0  # BOTTOM wall
            endCell.walls[0] = 0  # TOP wall

    def isNeighbors(cell):
        col, row = cell.cordX, cell.cordY
        # Check all four possible directions
        neighbors = []
        if row > 0:
            neighbors.append(gridCells[(row - 1) * cols + col])  # TOP
        if col < cols - 1:
            neighbors.append(gridCells[row * cols + (col + 1)])  # RIGHT
        if row < rows - 1:
            neighbors.append(gridCells[(row + 1) * cols + col])  # BOTTOM
        if col > 0:
            neighbors.append(gridCells[row * cols + (col - 1)])  # LEFT

        # If all neighbors are visited, the cell is complete
        for neighbor in neighbors:
            if not neighbor.visited:
                return False
        return True

    def primsAlgorithm():
        while walls:
            # Update display and pause
            window.fill(pygame.Color(40, 40, 40))
            for cell in gridCells:
                cell.display(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            pygame.display.flip()

            if globals.CAVESPEED == 1:
                pygame.time.delay(1000) 
            elif globals.CAVESPEED == 2:
                pygame.time.delay(100) 
            elif globals.CAVESPEED == 3:
                pygame.time.delay(10) 
            elif globals.CAVESPEED == 4:
                pygame.time.delay(0) 

            # Randomly select a wall from the list
            currentCell, direction = random.choice(walls)
            neighborCell = get_neighbor(currentCell, direction)

            if neighborCell and not neighborCell.visited:
                # Remove the wall between the current cell and the neighbor
                removeWalls(currentCell, neighborCell)
                
                # Mark the neighbor as visited and add its walls to the list
                neighborCell.visited = True
                neighborCell.current = True
                for new_direction in range(4):
                    walls.append((neighborCell, new_direction))

            # Remove the wall from the list after processing
            walls.remove((currentCell, direction))

            currentCell.current = False
            if isNeighbors(currentCell):
                currentCell.complete = True

    primsAlgorithm()

def mainMazePrins(window, clock):
    print(f"\n\n MAIN MAZE\nSIZE: {globals.SIZE},\n globals.WALLWIDTH: {globals.WALLWIDTH},\n globals.FPS: {globals.FPS},\n globals.CAVESPEED: {globals.CAVESPEED}")

    # Create grid of cells
    cols, rows = get_grid_dimensions()
    gridCells = [Cell(col, row, (255, 255, 255), (0, 50, 140), (0, 175, 255)) for row in range(rows) for col in range(cols)]

    caveMazePrins(window, gridCells)

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