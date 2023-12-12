import pygame, os, TextBubble
from SkillChecks.pygameSkillCheckKeys import RandomKeys
from SkillChecks.pygameSpamKeys import SpamKeys
from SkillChecks.pygameSkillCheckRect import TimingSkillCheck

class Appliance:
  AssetsPath = f"{os.path.dirname(__file__)}\Assets\\"
  SkillChecks = [TimingSkillCheck(), RandomKeys(), SpamKeys()]
  def __init__(self, name, size, position, image, textBubbleInteractText, textPositionString, skillCheckName, inventory = []):
    self.Name = name
    self.Size = size
    self.Position = position
    self.Image = pygame.image.load(self.AssetsPath + image).convert_alpha()
    self.Surface = pygame.transform.scale(self.Image, self.Size)
    self.Hitbox = self.Surface.get_rect(topleft=position)
    self.TextBubble = TextBubble.TextBubble(f'{textBubbleInteractText} {self.Name}', (255, 255, 255), (0, 0, 0), 25, self.Hitbox.__getattribute__(textPositionString))
    self.Inventory = inventory
    self.ShowInventory = False
    self.SkillCheckName = skillCheckName
    self.ShowSkillCheck = False
    self.LastSkillCheckPerformance = 'none'
    self.SkillCheck = RandomKeys()
    
  def PlaySkillCheck(self, screen, character):
    if not self.ShowSkillCheck:
      return 
    
    if len(character.Inventory) == 0:
      print('Need and Item in your inventory')
      self.ShowSkillCheck = False
      return

    if self.SkillCheck.Name == self.SkillCheckName:
      performance = ''
      if self.SkillCheck.PressesRemaining > 0:
        self.SkillCheck.DrawSkillCheck(screen)
      else:
        print(self.SkillCheck.CorrectCount)
        if self.SkillCheck.CorrectCount >= 6:
          performance = 'good'
        elif self.SkillCheck.CorrectCount >= 3:
          performance = 'mid'
        else:
          performance = 'you fucking suck'
        self.ShowSkillCheck = False
        self.LastSkillCheckPerformance = performance
        

  def RemoveItemFromInventory(self, item):
    self.Inventory.remove(item)
  
  def AddItemToInventory(self, item):
    self.Inventory.remove(item)

  def GetTextBubblePosition(self, positionString):
    return self.Hitbox[positionString]
  
  def DrawInventory(self, screen):
    if self.ShowInventory:
      inventoryRectangle = pygame.Rect(self.Position[0], self.Position[1], 100, 100)
      borderRectangle = inventoryRectangle.copy()
      borderRectangle.inflate_ip(4, 4)
      
      pygame.draw.rect(screen, (255, 255, 255), borderRectangle)
      pygame.draw.rect(screen, (100, 100, 100), inventoryRectangle)
      
      position = (self.Position[0] + 10, self.Position[1] + 10)
      for item in self.Inventory:
        item.DrawItem(screen, position)
        position = (position[0] + 5, position[1])
      
