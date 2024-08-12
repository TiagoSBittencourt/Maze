import pygame
from pygame import mixer
import globals
from genereteMazeDFS import mainMazeDFS
from guiClasses import Button, Slider

pygame.init()
pygame.mixer.init()
SC = pygame.display.set_mode(globals.RESOLUTION)
CLOCK = pygame.time.Clock()
BG = pygame.image.load("resources/BG image.png")
BG = pygame.transform.scale(BG, globals.RESOLUTION)
mixer.music.load("resources/MenuMusic.mp3")
mixer.music.play(-1)
pygame.mixer.music.set_volume(globals.VOLUME/100
                              )
def getFontSize(size): 
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
        MENU_RECT = MENU_TEXT.get_rect(center=(globals.WIDTH//2, 200))
        MENU_TEXT_SHADOW, MENU_RECT_SHADOW = makeShadow("MAIN MENU", 100, "#000000", ((globals.WIDTH+8)//2, 208))

        START_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=350, 
                            text="START", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        START_TEXT_SHADOW, START_RECT_SHADOW = makeShadow("START", 75, "#000000", ((globals.WIDTH+8)//2, 358))

        OPTIONS_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=500, 
                            text="OPTIONS", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        OPTIONS_TEXT_SHADOW, OPTIONS_RECT_SHADOW = makeShadow("OPTIONS", 75, "#000000", ((globals.WIDTH+8)//2, 508))

        QUIT_BUTTON = Button(image=pygame.image.load("resources/MenuButtonRect.png"), xCord=globals.WIDTH//2, yCord=650, 
                            text="QUIT", font=getFontSize(75), baseColor="#d7fcd4", hoveringColor="#0963DB")
        QUIT_TEXT_SHADOW, QUIT_RECT_SHADOW = makeShadow("QUIT", 75, "#000000", ((globals.WIDTH+8)//2, 658))


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
                    mainMazeDFS(SC, CLOCK)
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

    size_length_slider = Slider(350, 100, 500, 10, 100, globals.SIZE, global_vars, 'globals.SIZE', step=1, invert=True)
    wall_width_slider = Slider(350, 200, 500, 1, 9, globals.WALLWIDTH, global_vars, 'globals.WALLWIDTH', step=1)
    cave_speed_slider = Slider(350, 300, 500, 1, 5, globals.CAVESPEED, global_vars, 'globals.CAVESPEED', step=1, invert=True)  # Inverted
    fps_slider = Slider(350, 400, 500, 10, 120, globals.FPS, global_vars, 'globals.FPS', step=1)
    volume_slider = Slider(350, 500, 500, 0, 100, globals.VOLUME, global_vars, 'globals.VOLUME', step=1)

    size_length_text = getFontSize(40).render("Maze Size", True, "#0963DB")
    wall_width_text = getFontSize(40).render("Wall Width", True, "#0963DB")
    cave_speed_text = getFontSize(40).render("Cave Speed", True, "#0963DB")
    fps_text = getFontSize(40).render("FPS", True, "#0963DB")
    volume_text = getFontSize(40).render("VOLUME", True, "#0963DB")
    
    size_length_text_shadow = getFontSize(40).render("Maze Size", True, "#000000")
    wall_width_text_shadow = getFontSize(40).render("Wall Width", True, "#000000")
    cave_speed_text_shadow = getFontSize(40).render("Cave Speed", True, "#000000")
    fps_text_shadow = getFontSize(40).render("FPS", True, "#000000")
    volume_text_shadow = getFontSize(40).render("VOLUME", True, "#000000")

    SC.blit(size_length_text_shadow, (354, 64))
    SC.blit(wall_width_text_shadow, (354, 164))
    SC.blit(cave_speed_text_shadow, (354, 264))
    SC.blit(fps_text_shadow, (354, 364))
    SC.blit(volume_text_shadow, (354, 464))

    SC.blit(size_length_text, (350, 60))
    SC.blit(wall_width_text, (350, 160))
    SC.blit(cave_speed_text, (350, 260))
    SC.blit(fps_text, (350, 360))
    SC.blit(volume_text, (350, 460))


    while True:
        SC.fill(pygame.Color(40, 40, 40))
        SC.blit(BG, (0, 0))

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        BACK_BUTTON.mouseOnButton(OPTIONS_MOUSE_POS)
        BACK_BUTTON.displayButton(SC)

        SC.blit(size_length_text_shadow, (354, 64))
        SC.blit(wall_width_text_shadow, (354, 164))
        SC.blit(cave_speed_text_shadow, (354, 264))
        SC.blit(fps_text_shadow, (354, 364))
        SC.blit(volume_text_shadow, (354, 464))

        SC.blit(size_length_text, (350, 60))
        SC.blit(wall_width_text, (350, 160))
        SC.blit(cave_speed_text, (350, 260))
        SC.blit(fps_text, (350, 360))
        SC.blit(volume_text, (350, 460))

        # Draw sliders
        size_length_slider.draw(SC)
        wall_width_slider.draw(SC)
        cave_speed_slider.draw(SC)
        fps_slider.draw(SC)
        volume_slider.draw(SC)

        # Update and draw value texts
        size_length_value_text = getFontSize(45).render(str(size_length_slider.getValue()), True, "#0963DB")
        wall_width_value_text = getFontSize(45).render(str(wall_width_slider.getValue()), True, "#0963DB")
        cave_speed_value_text = getFontSize(45).render(str(cave_speed_slider.getValue()), True, "#0963DB")
        fps_value_text = getFontSize(45).render(str(fps_slider.getValue()), True, "#0963DB")
        volume_value_text = getFontSize(45).render(str(volume_slider.getValue()), True, "#0963DB")

        # Title Shadow
        size_length_value_text = getFontSize(45).render(str(size_length_slider.getValue()), True, "#000000")
        wall_width_value_text = getFontSize(45).render(str(wall_width_slider.getValue()), True, "#000000")
        cave_speed_value_text = getFontSize(45).render(str(cave_speed_slider.getValue()), True, "#000000")
        fps_value_text = getFontSize(45).render(str(fps_slider.getValue()), True, "#000000")
        volume_value_text = getFontSize(45).render(str(volume_slider.getValue()), True, "#000000")

        SC.blit(size_length_value_text, (350 + 500 // 2 - size_length_value_text.get_width() // 2 + 4, 124))
        SC.blit(wall_width_value_text, (350 + 500 // 2 - wall_width_value_text.get_width() // 2 + 4, 224))
        SC.blit(cave_speed_value_text, (350 + 500 // 2 - cave_speed_value_text.get_width() // 2 + 4, 324))
        SC.blit(fps_value_text, (350 + 500 // 2 - fps_value_text.get_width() // 2 + 4, 424))
        SC.blit(volume_value_text, (350 + 500 // 2 - volume_value_text.get_width() // 2 + 4, 524))
        
        # Title 
        size_length_value_text = getFontSize(45).render(str(size_length_slider.getValue()), True, "#0963DB")
        wall_width_value_text = getFontSize(45).render(str(wall_width_slider.getValue()), True, "#0963DB")
        cave_speed_value_text = getFontSize(45).render(str(cave_speed_slider.getValue()), True, "#0963DB")
        fps_value_text = getFontSize(45).render(str(fps_slider.getValue()), True, "#0963DB")
        volume_value_text = getFontSize(45).render(str(volume_slider.getValue()), True, "#0963DB")

        SC.blit(size_length_value_text, (350 + 500 // 2 - size_length_value_text.get_width() // 2, 120))
        SC.blit(wall_width_value_text, (350 + 500 // 2 - wall_width_value_text.get_width() // 2, 220))
        SC.blit(cave_speed_value_text, (350 + 500 // 2 - cave_speed_value_text.get_width() // 2, 320))
        SC.blit(fps_value_text, (350 + 500 // 2 - fps_value_text.get_width() // 2, 420))
        SC.blit(volume_value_text, (350 + 500 // 2 - volume_value_text.get_width() // 2, 520))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForClick(OPTIONS_MOUSE_POS):
                    globals.SIZE = global_vars["globals.SIZE"]
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
                pygame.mixer.music.set_volume(volume_slider.getValue()/100)

        pygame.display.flip()
        CLOCK.tick(globals.FPS)

if __name__ == "__main__":
    main()


