import pygame

class Cell:
    def __init__(self, cordX, cordY) -> None:
        self.cordX, self.cordY = cordX, cordY
        self.walls = [1, 1, 1, 1]
        self.visited = False

    def display(self, surface):
        x, y = self.cordX * WALL, self.cordY * WALL
        
        # Draw the cell background
        if self.visited:
            pygame.draw.rect(surface, pygame.Color(0, 50, 140), (x, y, WALL, WALL))
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
        
    
WIDTH, HEIGHT = 1200, 900
RESOLUTION = (WIDTH, HEIGHT)
WALL = 25
cols, rows = WIDTH // WALL, HEIGHT // WALL

pygame.init()
sc = pygame.display.set_mode(RESOLUTION)
clock = pygame.time.Clock()

# Create grid of cells
gridCells = []
for row in range(rows):
    for col in range(cols):
        gridCells.append(Cell(row, col))
        
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


