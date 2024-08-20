import pygame
import random
import globals
from cellClass import Cell

def get_grid_dimensions():
    return globals.WIDTH // globals.SIZE, globals.HEIGHT // globals.SIZE

def caveMazeDFS(window, gridCells):
    cols, rows = get_grid_dimensions()
    
    visited = set()
    currentCell = gridCells[0]
    currentCell.visited = True
    currentCell.current = True
    stack = []

    def findNeighbors(currentCell):
        possibles = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighborsList = []
        for (dx, dy) in possibles:
            newX, newY = currentCell.cordX + dx, currentCell.cordY + dy
            if 0 <= newX < cols and 0 <= newY < rows:
                neighbor = gridCells[newY * cols + newX]
                if not neighbor.visited:
                    neighborsList.append(neighbor)
        return neighborsList
    
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

    def DFS():
        nonlocal currentCell
        while stack or currentCell:
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


            currentCell.current = False
            neighbors = findNeighbors(currentCell)
            if neighbors:
                nextCell = random.choice(neighbors)
                removeWalls(currentCell, nextCell)
                nextCell.current = True
                nextCell.visited = True
                visited.add(nextCell)
                stack.append(currentCell)
                currentCell = nextCell
            elif stack:
                currentCell.complete = True
                currentCell = stack.pop()
                currentCell.current = True
            else:
                currentCell.complete = True
                currentCell.current = False
                break

    DFS()

def mainMazeDFS(window, clock):
    print(f"\n\n MAIN MAZE\nSIZE: {globals.SIZE},\n globals.WALLWIDTH: {globals.WALLWIDTH},\n globals.FPS: {globals.FPS},\n globals.CAVESPEED: {globals.CAVESPEED}")

    # Create grid of cells
    cols, rows = get_grid_dimensions()
    gridCells = [Cell(col, row, (255, 255, 255), (0, 50, 140), (0, 175, 255)) for row in range(rows) for col in range(cols)]

    caveMazeDFS(window, gridCells)

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