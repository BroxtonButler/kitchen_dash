import pygame, os, Appliance, Character, InventoryItem
from sys import exit

ImagePath = os.path.dirname(__file__) + '\Assets\\'

pygame.init()
screenWidth, screenHeight = 800, 800
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Kitchen-Dash')
clock = pygame.time.Clock()

# Kitchen Background
SIZE_OF_KITCHEN_SURFACE = (800, 800)
KITCHEN_POS = (0,0)

kitchen_surface = pygame.image.load(ImagePath + 'KitchenDash_Kitchen_i3.png').convert()
kitchen_surface = pygame.transform.scale(kitchen_surface, SIZE_OF_KITCHEN_SURFACE)

# Litte guy and pic frame
SIZE_OF_LILGUY = (75, 75)
SIZE_OF_PIC_FRAME = (125, 125)

lil_guy = pygame.image.load(ImagePath + 'KitchenDash_LittleGuy.png').convert_alpha()
pic_frame = pygame.image.load(ImagePath + 'KitrchenDash_PictureFrame.png').convert_alpha()

lil_guy = pygame.transform.scale(lil_guy, SIZE_OF_LILGUY)
pic_frame = pygame.transform.scale(pic_frame, SIZE_OF_PIC_FRAME)

#Kitchen Appliances
fridge = Appliance.Appliance("Refridgerator", (180, 200), (20, 450),'KitchenDash_Fridge_Closed.png', 'Open', 'center', 'none', [InventoryItem.FoodItem('Raw food item', 'Cooked food item', False, 'Refridgerator')])
oven = Appliance.Appliance('Oven', (170, 170), (186, 268), 'KitchenDash_Oven.png', 'Use', 'center', 'RandomKeys')
grill = Appliance.Appliance('Grill', (165, 165), (465, 273), 'KitchenDash_Grill_Off.png', 'Use', 'center', 'RandomKeys')
deepFryer = Appliance.Appliance('Deep Fryer', (200, 200), (595, 450), 'KitchenDash_DeepFryer_On.gif', 'Use', 'center', 'RandomKeys')
cuttingBoard = Appliance.Appliance('Cutting Board', (175, 146), (313, 292), 'KitchenDash_Counter2_Middle_CuttingBoard.png', 'Use', 'midtop', 'RandomKeys')

appliances = [fridge, oven, grill, deepFryer, cuttingBoard]

# Marlo 
playerCharacter = Character.Character('Marlo', (175, 200), (400, screenHeight - 200), ['marlo_0.png', 'marlo_3.png', 'marlo_4.png'], 4)

def CheckWindowCollision():
    if playerCharacter.Hitbox.right >= screenWidth:
        if 'right' not in playerCharacter.BlockedDirections:
            playerCharacter.BlockedDirections.append('right')
    elif 'right' in playerCharacter.BlockedDirections:
        playerCharacter.BlockedDirections.remove('right')

    if playerCharacter.Hitbox.left <= 0:
        if 'left' not in playerCharacter.BlockedDirections:
            playerCharacter.BlockedDirections.append('left')
    elif 'left' in playerCharacter.BlockedDirections:
        playerCharacter.BlockedDirections.remove('left')
    
    if playerCharacter.Hitbox.bottom >= screenHeight:
        if 'down' not in playerCharacter.BlockedDirections:
            playerCharacter.BlockedDirections.append('down')
    elif 'down' in playerCharacter.BlockedDirections:
        playerCharacter.BlockedDirections.remove('down')
    
    if playerCharacter.Hitbox.top <= 0:
        if 'up' not in playerCharacter.BlockedDirections:
            playerCharacter.BlockedDirections.append('up')
    elif 'up' in playerCharacter.BlockedDirections:
        playerCharacter.BlockedDirections.remove('up')

def CheckCharacterApplianceCollision(character, appliance):
    if character.Hitbox.colliderect(appliance.Hitbox):
        appliance.TextBubble.Show(screen)
        collisionTolerance = 10
        if abs(appliance.Hitbox.right - character.Hitbox.left) < collisionTolerance:
            if 'left' not in character.BlockedDirections:
                character.BlockedDirections.append('left')
        elif 'left' in character.BlockedDirections:
            character.BlockedDirections.remove('left')
        
        if abs(appliance.Hitbox.top - character.Hitbox.bottom) < collisionTolerance:
            if 'down' not in character.BlockedDirections:
                character.BlockedDirections.append('down')
        elif 'down' in character.BlockedDirections:
            character.BlockedDirections.remove('down')

        if abs(appliance.Hitbox.bottom - character.Hitbox.top) < collisionTolerance:
            if 'up' not in character.BlockedDirections:
                character.BlockedDirections.append('up')
        elif 'up' in character.BlockedDirections:
            character.BlockedDirections.remove('up')

        if abs(appliance.Hitbox.left - character.Hitbox.right) < collisionTolerance:
            if 'right' not in character.BlockedDirections:
                character.BlockedDirections.append('right')
        elif 'right' in character.BlockedDirections:
            character.BlockedDirections.remove('right')
    else:
        appliance.TextBubble.Hide()
        appliance.ShowInventory = False

InTheKitchen = True
currentSkillCheck = 'none'
while InTheKitchen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN, pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]:
                playerCharacter.Stop()
                            
        
        if event.type == pygame.KEYDOWN:
            if not currentSkillCheck == 'none':
                if event.key == ord(currentSkillCheck.TargetKey):
                    currentSkillCheck.CorrectCount += 1
                currentSkillCheck.PressesRemaining -= 1
                currentSkillCheck.GetNewBoxCoords()
            elif event.key == pygame.K_i:
                playerCharacter.ShowInventory = not playerCharacter.ShowInventory

        
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_a] or keyPressed[pygame.K_LEFT]:
        playerCharacter.Move('left')
    if keyPressed[pygame.K_d] or keyPressed[pygame.K_RIGHT]:
        playerCharacter.Move('right')
    if keyPressed[pygame.K_s] or keyPressed[pygame.K_DOWN]:
        playerCharacter.Move('down')
    if keyPressed[pygame.K_w] or keyPressed[pygame.K_UP]:
        playerCharacter.Move('up')
    
    #drawing textures on the screen
    screen.blit(kitchen_surface,KITCHEN_POS)
    screen.blit(fridge.Surface, fridge.Position)
    screen.blit(cuttingBoard.Surface, cuttingBoard.Position)
    screen.blit(oven.Surface, oven.Position)
    screen.blit(grill.Surface, grill.Position)
    screen.blit(deepFryer.Surface, deepFryer.Position)
    screen.blit(pic_frame, (100, 100))
    screen.blit(lil_guy, (125, 135))
    screen.blit(playerCharacter.Stance, playerCharacter.Hitbox)
    
    CheckWindowCollision()
    for appliance in appliances:
        CheckCharacterApplianceCollision(playerCharacter, appliance)
        appliance.TextBubble.CheckForMouse()
        appliance.TextBubble.CheckMouseClick(screen, appliance, playerCharacter)
        appliance.DrawInventory(screen)
        
        for item in appliance.Inventory:
            item.CheckForMouse(appliance.ShowInventory)
            item.CheckMouseClick(appliance, playerCharacter)

        if appliance.ShowSkillCheck:
            if appliance.SkillCheck.PressesRemaining > 0:
                currentSkillCheck = appliance.SkillCheck
            elif appliance.SkillCheck == currentSkillCheck:
                currentSkillCheck = 'none'
            
            appliance.PlaySkillCheck(screen, playerCharacter)
            match appliance.LastSkillCheckPerformance:
                case 'none':
                    pass
                case 'good': 
                    appliance.TextBubble.ShowSkillCheck = False
                    appliance.ShowSkillCheck = False
                    playerCharacter.Inventory[0].CookItem()
                    appliance.LastSkillCheckPerformance = 'none'
                case 'mid':
                    appliance.TextBubble.ShowSkillCheck = False
                    appliance.ShowSkillCheck = False
                    playerCharacter.Inventory[0].CookItem()
                    appliance.LastSkillCheckPerformance = 'none'
                case 'you fucking suck':
                    appliance.TextBubble.ShowSkillCheck = False
                    appliance.ShowSkillCheck = False
                    appliance.LastSkillCheckPerformance = 'none'
                    print('You are bad')

    playerCharacter.DrawInventory(screen)
    for item in playerCharacter.Inventory:
        item.CheckForMouse(playerCharacter.ShowInventory)
        item.CheckMouseClick(fridge, playerCharacter)
    pygame.display.update()
    clock.tick(60)

