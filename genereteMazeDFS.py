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
        if self.visited:
            pygame.draw.rect(surface, pygame.Color(0, 50, 140), (x, y, WALL, WALL))
        elif self.current:
            pygame.draw.rect(surface, pygame.Color(0, 0, 0), (x, y, WALL, WALL))
        else:
            pygame.draw.rect(surface, pygame.Color(0, 175, 255), (x, y, WALL, WALL))
        
        # Draw walls
        if self.walls[0]:  # TOP WALL
            pygame.draw.line(surface, pygame.Color("black"), (x, y), (x + WALL, y), width=2)
        if self.walls[1]:  # RIGHT WALL
            pygame.draw.line(surface, pygame.Color("black"), (x + WALL, y), (x + WALL, y + WALL), width=2)
        if self.walls[2]:  # BOTTOM WALL
            pygame.draw.line(surface, pygame.Color("black"), (x + WALL, y + WALL), (x, y + WALL), width=2)
        if self.walls[3]:  # LEFT WALL
            pygame.draw.line(surface, pygame.Color("black"), (x, y + WALL), (x, y), width=2)
        
    
def caveMazeDFS(window, gridCells):
    visitedList = [gridCells[0]]
    gridCells[0].visited = True
    gridCells[0].current = True
    stack = []

    def findNeighbors(gridCells, currentCell):
        possibles = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighborsList = []
        for (x, y) in possibles:
            newX, newY = currentCell.cordX + x, currentCell.cordY + y
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
        

    def DFS(gridCells, currentCell):
        nonlocal stack
        while len(stack) > 0 or currentCell:
            # Update display and pause
            for cell in gridCells:
                cell.display(window)
            pygame.display.flip()
            pygame.time.delay(100) 

            currentCell.current = False
            neighbors = findNeighbors(gridCells, currentCell)
            if neighbors:
                nextCell = random.choice(neighbors)
                removeWalls(startCell=currentCell, endCell=nextCell)
                nextCell.current = True
                nextCell.visited = True
                stack.append(currentCell)
                currentCell = nextCell
                visitedList.append(currentCell)
            elif stack:
                currentCell = stack.pop()
            else:
                break

    DFS(gridCells, gridCells[0])

        
        


WIDTH, HEIGHT = 1200, 900
RESOLUTION = (WIDTH, HEIGHT)
WALL = 100
cols, rows = WIDTH // WALL, HEIGHT // WALL

pygame.init()
sc = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Create grid of cells
gridCells = []
for row in range(rows):
    for col in range(cols):
        gridCells.append(Cell(col, row))

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
