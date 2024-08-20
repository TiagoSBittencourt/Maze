import pygame
from pygame import mixer
import globals
from generateMazeDFS import mainMazeDFS
from generateMazePrins import mainMazePrins
from generateMazeEllers import mainMazeEllers
from guiClasses import Button, Slider

"""
                                                TODO: Bug fix on Maze Generation of Ellers
"""

pygame.init()
pygame.mixer.init()
SC = pygame.display.set_mode(globals.RESOLUTION)
CLOCK = pygame.time.Clock()
BG = pygame.image.load("resources/BG image.png")
BG = pygame.transform.scale(BG, globals.RESOLUTION)
mixer.music.load("resources/MenuMusic.mp3")
mixer.music.play(-1)
pygame.mixer.music.set_volume(globals.VOLUME/100)

def getFontSize(size): 
    return pygame.font.Font("resources/Pixellari.ttf", size)

def render_text_with_shadow(text, font_size, color, shadow_color, position):
    text_shadow = getFontSize(font_size).render(text, True, shadow_color)
    text_main = getFontSize(font_size).render(text, True, color)
    SC.blit(text_shadow, (position[0] + 4, position[1] + 4))  # Offset shadow slightly
    SC.blit(text_main, position)

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
        MENU_RECT = MENU_TEXT.get_rect(center=(globals.WIDTH//2, globals.HEIGHT*1/5))
        MENU_TEXT_SHADOW, MENU_RECT_SHADOW = makeShadow("MAIN MENU", 100, "#000000", ((globals.WIDTH+8)//2, globals.HEIGHT*1/5 + 8))

        START_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=globals.HEIGHT*2/5, 
                            text="START", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        START_TEXT_SHADOW, START_RECT_SHADOW = makeShadow("START", 75, "#000000", ((globals.WIDTH+8)//2, globals.HEIGHT*2/5 + 8))

        OPTIONS_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=globals.HEIGHT*3/5, 
                            text="OPTIONS", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        OPTIONS_TEXT_SHADOW, OPTIONS_RECT_SHADOW = makeShadow("OPTIONS", 75, "#000000", ((globals.WIDTH+8)//2, globals.HEIGHT*3/5 + 8))

        QUIT_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=globals.HEIGHT*4/5, 
                            text="QUIT", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        QUIT_TEXT_SHADOW, QUIT_RECT_SHADOW = makeShadow("QUIT", 75, "#000000", ((globals.WIDTH+8)//2, globals.HEIGHT*4/5 + 8))


        for textShadow, rectShadow in [(MENU_TEXT_SHADOW, MENU_RECT_SHADOW), (START_TEXT_SHADOW, START_RECT_SHADOW), (OPTIONS_TEXT_SHADOW, OPTIONS_RECT_SHADOW), (QUIT_TEXT_SHADOW, QUIT_RECT_SHADOW)]:
            SC.blit(textShadow, rectShadow)


        SC.blit(MENU_TEXT, MENU_RECT)
        for button in [START_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.mouseOnButton(MENU_MOUSE_POS)
            button.displayButton(SC)
        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BUTTON.checkForClick(MENU_MOUSE_POS):
                    optionsMenu()
                    print(f"WALL: {globals.SIZE},\n globals.WALLWIDTH: {globals.WALLWIDTH},\n globals.FPS: {globals.FPS},\n globals.VOLUME: {globals.VOLUME},\n globals.CAVESPEED: {globals.CAVESPEED}")
                if START_BUTTON.checkForClick(MENU_MOUSE_POS):
                    choseMazeGenerationMenu()
                if QUIT_BUTTON.checkForClick(MENU_MOUSE_POS):
                    pygame.quit()
                    exit()

        pygame.display.flip()
        CLOCK.tick(globals.FPS)


def optionsMenu():
    global_vars = {
        "globals.SIZE": globals.SIZE,
        "globals.WALLWIDTH": globals.WALLWIDTH,
        "globals.FPS": globals.FPS,
        "globals.VOLUME": globals.VOLUME,
        "globals.CAVESPEED": globals.CAVESPEED
    }

    BACK_BUTTON = Button(image=pygame.transform.scale(pygame.image.load("resources/BlueBackArrow.png"), (40, 40)), xCord=40, yCord=40)

    size_length_text_dict = {1: "SMALL", 2: "MEDIUM", 3: "LARGE"}
    size_resp_wall = {3: 35, 2: 65, 1: 100}


    size_length_slider = Slider(350, 100, 500, 1, 3, 2, global_vars, 'globals.SIZE', step=1)
    wall_width_slider = Slider(350, 200, 500, 1, 9, globals.WALLWIDTH, global_vars, 'globals.WALLWIDTH', step=1)
    cave_speed_slider = Slider(350, 300, 500, 1, 5, globals.CAVESPEED, global_vars, 'globals.CAVESPEED', step=1, invert=True)  # Inverted
    fps_slider = Slider(350, 400, 500, 10, 120, globals.FPS, global_vars, 'globals.FPS', step=1)
    volume_slider = Slider(350, 500, 500, 0, 100, globals.VOLUME, global_vars, 'globals.VOLUME', step=1)

    labels = [
        ("Maze Size", 40, (350, 60)),
        ("Wall Width", 40, (350, 160)),
        ("Cave Speed", 40, (350, 260)),
        ("FPS", 40, (350, 360)),
        ("VOLUME", 40, (350, 460))
    ]

    while True:
        SC.fill(pygame.Color(40, 40, 40))
        SC.blit(BG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON.mouseOnButton(OPTIONS_MOUSE_POS)
        BACK_BUTTON.displayButton(SC)

        # Render all labels with shadows
        for label, font_size, pos in labels:
            render_text_with_shadow(label, font_size, "#0963DB", "#000000", pos)

        # Draw sliders
        size_length_slider.draw(SC)
        wall_width_slider.draw(SC)
        cave_speed_slider.draw(SC)
        fps_slider.draw(SC)
        volume_slider.draw(SC)

        # Value Text with Shadow and Main Text
        values = [
            (str(size_length_text_dict[size_length_slider.getValue()]), 40, (350 + 500 // 2, 120)),
            (str(wall_width_slider.getValue()), 45, (350 + 500 // 2, 220)),
            (str(cave_speed_slider.getValue()), 45, (350 + 500 // 2, 320)),
            (str(fps_slider.getValue()), 45, (350 + 500 // 2, 420)),
            (str(volume_slider.getValue()), 45, (350 + 500 // 2, 520))
        ]

        for value, font_size, pos in values:
            render_text_with_shadow(value, font_size, "#0963DB", "#000000", (pos[0] - getFontSize(font_size).render(value, True, "#0963DB").get_width() // 2, pos[1]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForClick(OPTIONS_MOUSE_POS):
                    # Not the best implementetion of size
                    globals.SIZE = size_resp_wall.get(global_vars.get("globals.SIZE", 2), 50)
                    globals.WALLWIDTH = global_vars["globals.WALLWIDTH"]
                    globals.FPS = global_vars["globals.FPS"]
                    globals.VOLUME = global_vars["globals.VOLUME"]
                    globals.CAVESPEED = global_vars["globals.CAVESPEED"]
                    print(f"globals.SIZE: {globals.SIZE},\n globals.WALLWIDTH: {globals.WALLWIDTH},\n globals.FPS: {globals.FPS},\n globals.VOLUME: {globals.VOLUME},\n globals.CAVESPEED: {globals.CAVESPEED}")
                    return
                size_length_slider.handle_event(event)
                wall_width_slider.handle_event(event)
                cave_speed_slider.handle_event(event)
                fps_slider.handle_event(event)
                volume_slider.handle_event(event)
            if event.type == pygame.MOUSEBUTTONUP:
                size_length_slider.handle_event(event)
                wall_width_slider.handle_event(event)
                cave_speed_slider.handle_event(event)
                fps_slider.handle_event(event)
                volume_slider.handle_event(event)
            if event.type == pygame.MOUSEMOTION:
                size_length_slider.handle_event(event)
                wall_width_slider.handle_event(event)
                cave_speed_slider.handle_event(event)
                fps_slider.handle_event(event)
                volume_slider.handle_event(event)
                # Update the music volume
                pygame.mixer.music.set_volume(volume_slider.getValue() / 100)

        pygame.display.flip()
        CLOCK.tick(globals.FPS)


def choseMazeGenerationMenu():
    SC.fill(pygame.Color(40, 40, 40))
    SC.blit(BG, (0, 0))

    # Button positions
    button_positions = [
        (globals.WIDTH // 4, 200),
        (globals.WIDTH // 4, 400),
        (globals.WIDTH // 4, 600),
        (globals.WIDTH // 4, 800),
        (globals.WIDTH * 3 // 4, 200),
        (globals.WIDTH * 3 // 4, 400),
        (globals.WIDTH * 3 // 4, 600),
        (globals.WIDTH * 3 // 4, 800)
    ]

    # Creating buttons
    buttons = []
    button_texts = ["DFS", "Prim's", "Eller's", "Hunt-Kill", "Binarry Tree", "Kruskal's", "Sizewinder", "Bronder"]
    
    for i, pos in enumerate(button_positions):
        buttons.append(Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=pos[0], yCord=pos[1],
                              text=button_texts[i], font=getFontSize(60), baseColor="#d7fcd4", hoveringColor="#0963DB"))
    
    while True:
        SC.fill(pygame.Color(40, 40, 40))
        SC.blit(BG, (0, 0))

        MAZE_MOUSE_POS = pygame.mouse.get_pos()

        # Draw all buttons
        for button in buttons:
            button.mouseOnButton(MAZE_MOUSE_POS)
            button.displayButton(SC)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, button in enumerate(buttons):
                    if button.checkForClick(MAZE_MOUSE_POS):
                        if i == 0:
                            mainMazeDFS(SC, CLOCK)
                        elif i == 1:
                            mainMazePrins(SC, CLOCK)
                        elif i == 2:
                            mainMazeEllers(SC, CLOCK)


        pygame.display.flip()
        CLOCK.tick(globals.FPS)

if __name__ == "__main__":
    main()


