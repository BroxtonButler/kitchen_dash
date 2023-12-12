import pygame

class TextBubble:

  def __init__(self, text, textColor, bgColor, size, position):
    self.Text = text
    self.TextColor = textColor
    self.BackgroundColor = bgColor
    self.Position = position
    
    self.font = pygame.font.SysFont(None, size)
    self.TextSurface = self.font.render(text, True, textColor)
    self.TextRectangle = self.TextSurface.get_rect(midtop = self.Position)

    self.BackgroundRectangle = self.TextRectangle.copy()
    self.BackgroundRectangle.inflate_ip(10, 10)

    self.FrameRectangle = self.BackgroundRectangle.copy()
    self.FrameRectangle.inflate_ip(4, 4)

    self.IsVisible = False
    self.IsMouseOver = False
  
  def Show(self, screen):
    self.IsVisible = True
    pygame.draw.rect(screen, self.TextColor, self.FrameRectangle)
    pygame.draw.rect(screen, self.BackgroundColor, self.BackgroundRectangle)
    screen.blit(self.TextSurface, self.TextRectangle)
  
  def Hide(self):
    self.IsVisible = False

  def CheckForMouse(self):
    if self.IsVisible and self.FrameRectangle.collidepoint(pygame.mouse.get_pos()):
      self.IsMouseOver = True
      self.BackgroundColor = (150, 150, 0)
    else:
      self.IsMouseOver = False
      self.BackgroundColor = (0, 0, 0)
  
  def CheckMouseClick(self, screen, appliance, character):
    if not self.IsMouseOver:
      return
    
    if pygame.mouse.get_pressed()[0] == 1 and appliance.ShowSkillCheck is False:
      if appliance.Name == 'Refridgerator':
        appliance.ShowInventory = True
      else:
        appliance.ShowSkillCheck = True
      

