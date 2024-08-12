import pygame

class Button():
    def __init__(self, image, xCord=0, yCord=0, text=None, font=None, baseColor=None, hoveringColor=None) -> None:
        self.buttonImage = image
        self.xCord = xCord
        self.yCord = yCord
        self.buttonRect = self.buttonImage.get_rect(center=(self.xCord, self.yCord))
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        if text:
            self.text = text
            self.buttonFont = font
            self.textObj = self.buttonFont.render(self.text, True, self.baseColor)
            self.textRect = self.textObj.get_rect(center=(self.xCord,self.yCord))
        else:
            self.text = None
        
    def displayButton(self, window):
        window.blit(self.buttonImage, self.buttonRect)
        if self.text:
            window.blit(self.textObj, self.textRect)

    def checkForClick(self, mouseCord):
        if mouseCord[0] in range(self.buttonRect.left, self.buttonRect.right) and mouseCord[1] in range(self.buttonRect.top, self.buttonRect.bottom):
            return True
        return False
    
    def mouseOnButton(self, mouseCord):
        if self.text:
            if self.buttonRect.collidepoint(mouseCord):
                self.textObj = self.buttonFont.render(self.text, True, self.hoveringColor)
            else:
                self.textObj = self.buttonFont.render(self.text, True, self.baseColor)


import pygame

class Slider:
    def __init__(self, x, y, width, min_val, max_val, initial_val, var_dict, key, step=1, invert=False):
        self.rect = pygame.Rect(x, y, width, 20)
        self.min_val = min_val
        self.max_val = max_val
        self.value = initial_val
        self.dragging = False
        self.handle_radius = 10
        self.track_radius = 10
        self.handle_color = "#0963DB"
        self.track_color = "#A9A9A9"
        self.var_dict = var_dict  
        self.key = key
        self.step = step
        self.invert = invert  # Added parameter

    def draw(self, surface):
        pygame.draw.rect(surface, self.track_color, self.rect, border_radius=self.track_radius)
        
        handle_x = self.rect.left + (self.value - self.min_val) / (self.max_val - self.min_val) * (self.rect.width - self.handle_radius * 2)
        handle_y = self.rect.top + (self.rect.height - self.handle_radius * 2) // 2
        
        handle_rect = pygame.Rect(handle_x, handle_y, self.handle_radius * 2, self.handle_radius * 2)
        pygame.draw.ellipse(surface, self.handle_color, handle_rect)
        pygame.draw.ellipse(surface, "#A9A9A9", handle_rect, 1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(self.rect.left + (self.value - self.min_val) / (self.max_val - self.min_val) * (self.rect.width - self.handle_radius * 2),
                           self.rect.top, self.handle_radius * 2, self.rect.height).collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            x = event.pos[0]
            new_value = self.min_val + (x - self.rect.left) / (self.rect.width - self.handle_radius * 2) * (self.max_val - self.min_val)
            self.value = min(max(new_value, self.min_val), self.max_val)
            self.value = round(self.value / self.step) * self.step 
            # Invert value if needed
            if self.invert:
                self.var_dict[self.key] = int(self.max_val - self.value + 10)
            else:
                self.var_dict[self.key] = int(self.value)

    def getValue(self):
        # I don't implemented the invert here, because i want to be an ilusion to the user
        return int(self.value)