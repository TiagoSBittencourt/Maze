import pygame
from globals import *
from genereteMazeDFS import mainMazeDFS as caveMazeDFS


def main():
    pygame.init()
    window = pygame.display.set_mode(RESOLUTION)
    clock = pygame.time.Clock()

    caveMazeDFS(window, clock)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        window.fill(pygame.Color(40, 40, 40))
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()