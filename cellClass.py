import pygame
import globals

class Cell:
    def __init__(self, cordX, cordY, currentColor, completeColor, notCompleteColor, bgColor=(50,50,50), wallColor=(0,0,0)) -> None:
        self.cordX, self.cordY = cordX, cordY
        self.currentColor = currentColor
        self.completeColor = completeColor
        self.notCompleteColor = notCompleteColor
        self.bgColor = bgColor
        self.wallColor = wallColor
        self.walls = [1, 1, 1, 1]
        self.complete = False
        self.visited = False
        self.current = False
        self.setID = None  # Add setID attribute for the Eller's algorithm

    def display(self, surface):
        x, y = self.cordX * globals.SIZE, self.cordY * globals.SIZE
        
        # Draw the cell background
        if self.current:
            pygame.draw.rect(surface, pygame.Color(self.currentColor), (x, y, globals.SIZE, globals.SIZE))
        elif self.visited:
            if self.complete:
                pygame.draw.rect(surface, pygame.Color(self.completeColor), (x, y, globals.SIZE, globals.SIZE))
            else:
                pygame.draw.rect(surface, pygame.Color(self.notCompleteColor), (x, y, globals.SIZE, globals.SIZE))
        else:
            pygame.draw.rect(surface, pygame.Color(self.bgColor), (x, y, globals.SIZE, globals.SIZE))
        
        # Draw walls
        if self.walls[0]:  # TOP WALL
            pygame.draw.line(surface, pygame.Color(self.wallColor), (x, y), (x + globals.SIZE, y), width=globals.WALLWIDTH)
        if self.walls[1]:  # RIGHT WALL
            pygame.draw.line(surface, pygame.Color(self.wallColor), (x + globals.SIZE, y), (x + globals.SIZE, y + globals.SIZE), width=globals.WALLWIDTH)
        if self.walls[2]:  # BOTTOM WALL
            pygame.draw.line(surface, pygame.Color(self.wallColor), (x + globals.SIZE, y + globals.SIZE), (x, y + globals.SIZE), width=globals.WALLWIDTH)
        if self.walls[3]:  # LEFT WALL
            pygame.draw.line(surface, pygame.Color(self.wallColor), (x, y + globals.SIZE), (x, y), width=globals.WALLWIDTH)