import pygame
from globals import *
from genereteMazeDFS import mainMazeDFS as caveMazeDFS
from button import Button

pygame.init()
SC = pygame.display.set_mode(RESOLUTION)
CLOCK = pygame.time.Clock()
BG = pygame.image.load("resources/BG image.png")
BG = pygame.transform.scale(BG, RESOLUTION)

def getFontSize(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("resources/Pixellari.ttf", size)


def main():

    def makeShadow(txt, fontSize, color, position):
        textShadow = getFontSize(fontSize).render(txt, True, color)
        rectShadow = textShadow.get_rect(center=position)
        return textShadow, rectShadow

    while True:
        SC.fill(pygame.Color(40, 40, 40))
        SC.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = getFontSize(100).render("MAIN MENU", True, "#0963DB")
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH//2, 200))
        MENU_TEXT_SHADOW, MENU_RECT_SHADOW = makeShadow("MAIN MENU", 100, "#000000", ((WIDTH+8)//2, 208))

        START_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=WIDTH//2, yCord=350, 
                            text="START", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        START_TEXT_SHADOW, START_RECT_SHADOW = makeShadow("START", 75, "#000000", ((WIDTH+8)//2, 358))

        OPTIONS_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=WIDTH//2, yCord=500, 
                            text="OPTIONS", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        OPTIONS_TEXT_SHADOW, OPTIONS_RECT_SHADOW = makeShadow("OPTIONS", 75, "#000000", ((WIDTH+8)//2, 508))

        QUIT_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=WIDTH//2, yCord=650, 
                            text="QUIT", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        QUIT_TEXT_SHADOW, QUIT_RECT_SHADOW = makeShadow("QUIT", 75, "#000000", ((WIDTH+8)//2, 658))


        for textShadow, rectShadow in [(MENU_TEXT_SHADOW, MENU_RECT_SHADOW), (START_TEXT_SHADOW, START_RECT_SHADOW), (OPTIONS_TEXT_SHADOW, OPTIONS_RECT_SHADOW), (QUIT_TEXT_SHADOW, QUIT_RECT_SHADOW)]:
            SC.blit(textShadow, rectShadow)


        SC.blit(MENU_TEXT, MENU_RECT)
        for button in [START_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.displayButton(SC)
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if START_BUTTON.checkForClick(MENU_MOUSE_POS):
                    caveMazeDFS(SC, CLOCK)
                if OPTIONS_BUTTON.checkForClick(MENU_MOUSE_POS):
                    print("options clicked")
                if QUIT_BUTTON.checkForClick(MENU_MOUSE_POS):
                    pygame.quit()
                    exit()

        pygame.display.flip()
        CLOCK.tick(FPS)


if __name__ == "__main__":
    main()


