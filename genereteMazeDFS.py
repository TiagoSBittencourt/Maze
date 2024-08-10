import pygame
import random

class Cell:
    def __init__(self, cordX, cordY) -> None:
        self.cordX, self.cordY = cordX, cordY
        self.walls = [1, 1, 1, 1]
        self.visited = False
        self.current = False

    def display(self, surface):
        x, y = self.cordX * WALL, self.cordY * WALL
        
        # Draw the cell background
        if self.current:
            pygame.draw.rect(surface, pygame.Color(0, 0, 0), (x, y, WALL, WALL))
        elif self.visited:
            pygame.draw.rect(surface, pygame.Color(0, 50, 140), (x, y, WALL, WALL))
        else:
            pygame.draw.rect(surface, pygame.Color(0, 175, 255), (x, y, WALL, WALL))
        
        # Draw walls
        if self.walls[0]:  # TOP WALL
            pygame.draw.line(surface, pygame.Color("black"), (x, y), (x + WALL, y), width=WALLWIDHT)
        if self.walls[1]:  # RIGHT WALL
            pygame.draw.line(surface, pygame.Color("black"), (x + WALL, y), (x + WALL, y + WALL), width=WALLWIDHT)
        if self.walls[2]:  # BOTTOM WALL
            pygame.draw.line(surface, pygame.Color("black"), (x + WALL, y + WALL), (x, y + WALL), width=WALLWIDHT)
        if self.walls[3]:  # LEFT WALL
            pygame.draw.line(surface, pygame.Color("black"), (x, y + WALL), (x, y), width=WALLWIDHT)

        
def caveMazeDFS(window, gridCells):
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
            for cell in gridCells:
                cell.display(window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            pygame.display.flip()
            pygame.time.delay(100) 

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
                currentCell = stack.pop()
                currentCell.current = True
            else:
                break

    DFS()

WIDTH, HEIGHT = 1200, 900
RESOLUTION = (WIDTH, HEIGHT)
WALL =  100
WALLWIDHT = 3
cols, rows = WIDTH // WALL, HEIGHT // WALL

pygame.init()
sc = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Create grid of cells
gridCells = [Cell(col, row) for row in range(rows) for col in range(cols)]

caveMazeDFS(sc, gridCells)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    sc.fill(pygame.Color(40, 40, 40))

    # Display all cells
    for cell in gridCells:
        cell.display(sc)

    pygame.display.flip()
    clock.tick(60)