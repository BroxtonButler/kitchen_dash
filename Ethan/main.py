import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Kitchen-Dash')
clock = pygame.time.Clock()

# Kitchen Background
SIZE_OF_KITCHEN_SURFACE = (800, 800)
KITCHEN_POS = (0,0)

kitchen_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_Kitchen_i3.png').convert()
kitchen_surface = pygame.transform.scale(kitchen_surface, SIZE_OF_KITCHEN_SURFACE)

# Litte guy and pic frame
SIZE_OF_LILGUY = (75, 75)
SIZE_OF_PIC_FRAME = (125, 125)

lil_guy = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_LittleGuy.png').convert_alpha()
pic_frame = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitrchenDash_PictureFrame.png').convert_alpha()

lil_guy = pygame.transform.scale(lil_guy, SIZE_OF_LILGUY)
pic_frame = pygame.transform.scale(pic_frame, SIZE_OF_PIC_FRAME)

# Fridge
FRIDGE_POS = (20,450)
SIZE_OF_FRIDGE = (180, 200)

fridge_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_Fridge_Closed.png').convert_alpha()
fridge_surface = pygame.transform.scale(fridge_surface, SIZE_OF_FRIDGE)

# Kitchen Counters
SIZE_OF_COUNTER = (175, 145)

counter_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_Counter2_Middle_CuttingBoard.png').convert_alpha()
counter_surface = pygame.transform.scale(counter_surface, SIZE_OF_COUNTER)

# Oven
SIZE_OF_OVEN = (170, 175)
OVEN_POS = (186, 268)

oven_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_Oven.png').convert_alpha()
oven_surface = pygame.transform.scale(oven_surface, SIZE_OF_OVEN)

# Grill
SIZE_OF_GRILL = (165, 170)
GRILL_POS = (465, 273)

grill_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_Grill_Off.png').convert_alpha()
grill_surface = pygame.transform.scale(grill_surface, SIZE_OF_GRILL)

# Deep Fryer
SIZE_OF_DEEPFRYER = (200, 200)
DEEP_FRY_POS = (595, 450)

deepfryer_surface = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\KitchenDash_DeepFryer_On.gif').convert_alpha()
deepfryer_surface = pygame.transform.scale(deepfryer_surface, SIZE_OF_DEEPFRYER)

# Marlo 
SIZE_OF_MARLO = (175, 200)

marlo_stance = pygame.image.load('kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\marlo_0.png').convert_alpha()
marlo_stance = pygame.transform.scale(marlo_stance, SIZE_OF_MARLO)
marlo_rect = marlo_stance.get_rect(midtop = (400,400))

# MARLO Walking
walking = False
value = 0
marlo_walking = [pygame.image.load("kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\marlo_3.png"),
				pygame.image.load("kitchen_dash-davyBranch\kitchen_dash-davyBranch\Assets\marlo_4.png")]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Marlo animation
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                walking = False
                value = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                walking = False
                value = 0

    key_pressed_is = pygame.key.get_pressed()
    if key_pressed_is[pygame.K_LEFT]:
        marlo_rect.x -= 8
        walking = True
        
    if key_pressed_is[pygame.K_RIGHT]:
        marlo_rect.x += 8
        walking = True
        

    if key_pressed_is[pygame.K_UP]:
        marlo_rect.y -= 8
        walking = True
    if key_pressed_is[pygame.K_DOWN]:
        marlo_rect.y += 8
        walking = True

    if walking:
        value += 1

    if value >= len(marlo_walking):
        value = 0


    marlo_stance = marlo_walking[value]
    #drawing textures on the screen
    screen.blit(kitchen_surface,KITCHEN_POS)
    screen.blit(fridge_surface,FRIDGE_POS)
    screen.blit(counter_surface, (313, 292))
    screen.blit(oven_surface, OVEN_POS)
    screen.blit(grill_surface, GRILL_POS)
    screen.blit(deepfryer_surface, DEEP_FRY_POS)
    screen.blit(pic_frame, (100, 100))
    screen.blit(lil_guy, (125, 135))
    screen.blit(marlo_stance, marlo_rect)

    pygame.display.update()
    clock.tick(60)

