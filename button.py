class Button():
    def __init__(self, image, xCord, yCord, text, font, baseColor, hoveringColor) -> None:
        self.buttonImage = image
        self.xCord = xCord
        self.yCord = yCord
        self.buttonRect = self.buttonImage.get_rect(center=(self.xCord, self.yCord))
        self.baseColor, self.hoveringColor = baseColor, hoveringColor
        self.text = text
        self.buttonFont = font
        self.textObj = self.buttonFont.render(self.text, True, self.baseColor)
        self.textRect = self.textObj.get_rect(center=(self.xCord,self.yCord))
        
    def displayButton(self, window):
        window.blit(self.buttonImage, self.buttonRect)
        window.blit(self.textObj, self.textRect)

    def checkForClick(self, mouseCord):
        if mouseCord[0] in range(self.buttonRect.left, self.buttonRect.right) and mouseCord[1] in range(self.buttonRect.top, self.buttonRect.bottom):
            return True
        return False
    
    def changeColor(self, mouseCord):
        if self.buttonRect.collidepoint(mouseCord):
            self.textObj = self.buttonFont.render(self.text, True, self.hoveringColor)
        else:
            self.textObj = self.buttonFont.render(self.text, True, self.baseColor)
