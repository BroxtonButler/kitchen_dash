import pygame

class FoodItem:  
  def __init__(self, uncookedName, cookedName, isCooked, location):
    self.Names = [uncookedName, cookedName]
    self.IsCooked = isCooked
    self.Name = self.Names[0] if not self.IsCooked else self.Names[1]
    self.Color = self.GetColor()
    self.IsMouseOver = False
    self.Location = location
  
  def DrawItem(self, screen, position):
    if self.IsCooked:
      self.Rectangle = pygame.Rect(position[0], position[1], 25, 25)
      pygame.draw.rect(screen, self.Color, self.Rectangle)
    else:
      self.Rectangle = pygame.Rect(position[0], position[1], 25, 25)
      pygame.draw.rect(screen, self.Color, self.Rectangle)

  def CookItem(self):
    self.IsCooked = True
    self.Name = self.Names[1]

  def GetColor(self):
      return (50, 100, 50) if self.IsCooked else (100, 50, 50)
  
  def CheckForMouse(self, visible):
    if visible and self.Rectangle.collidepoint(pygame.mouse.get_pos()):
      self.IsMouseOver = True
      self.Color = (150, 150, 0)
    else:
      self.IsMouseOver = False
      self.Color = self.GetColor()

  def CheckMouseClick(self, appliance, character):
    if not self.IsMouseOver:
      return
    
    if pygame.mouse.get_pressed()[0] == 1:
      if self.Location == 'Refridgerator' and self not in character.Inventory:
        character.Inventory.append(self)
        appliance.Inventory.remove(self)
        self.Location = 'Character'
      elif self.Location == 'Character' and self not in appliance.Inventory:
        appliance.Inventory.append(self)
        character.Inventory.remove(self)
        self.Location = 'Refridgerator'