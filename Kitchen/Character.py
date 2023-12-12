import pygame, os

class Character:  
  AssetsPath = f"{os.path.dirname(__file__)}\Assets\\"
  
  def __init__(self, name, size, position, imageFileNames, speed):
    self.Name = name
    self.Size = size
    self.Position = position
    self.Images = self.GetLoadedImages(imageFileNames)
    self.CurrentImageIndex = 0
    self.Stance = self.Images[self.CurrentImageIndex]
    self.Hitbox = self.Stance.get_rect(center = position)
    self.Speed = speed
    self.BlockedDirections = []
    self.Inventory = []
    self.ShowInventory = False

  def DrawInventory(self, screen):
    if self.ShowInventory:
      inventoryRectangle = pygame.Rect(50, 50, 100, 100)
      borderRectangle = inventoryRectangle.copy()
      borderRectangle.inflate_ip(4, 4)
      
      pygame.draw.rect(screen, (255, 255, 255), borderRectangle)
      pygame.draw.rect(screen, (100, 100, 100), inventoryRectangle)
      
      position = (60, 60)
      for item in self.Inventory:
        item.DrawItem(screen, position)
        position = (position[0] + 5, position[1])
    
  def AddItemToInventory(self, item):
    self.Inventory.append(item)

  def RemoveItemFromInventory(self, item):
    self.Inventory.remove(item)

  def GetLoadedImages(self, imageFileNames):
    images = []
    for imageFileName in imageFileNames:
      convertedImage = pygame.image.load(self.AssetsPath + imageFileName).convert_alpha()
      scaledImage = pygame.transform.scale(convertedImage, self.Size)
      images.append(scaledImage)
    
    return images
  
  def Move(self, direction):
    if self.CurrentImageIndex + 1 >= len(self.Images):
      self.CurrentImageIndex = 0
    else:
      self.CurrentImageIndex += 1
    
    self.Stance = self.Images[self.CurrentImageIndex]

    if direction not in self.BlockedDirections:
      match direction:
        case 'left':
          self.Hitbox.x -= self.Speed
        case 'right':
          self.Hitbox.x += self.Speed
        case 'up':
          self.Hitbox.y -= self.Speed
        case 'down':
          self.Hitbox.y += self.Speed
  
  def Stop(self):
    self.CurrentImageIndex = 0