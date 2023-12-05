### SOFT FINISHED - pressing random keys works. Could possibly use a timer ###
# this is a skill check prototype - press the indicated keys before the time is up to pass

import pygame, sys, random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Skill Check: Keys")

target = chr(random.randint(97, 122))

boxX = 0
boxY = 0

def boxCoords():
    global boxX, boxY, target
    boxX = random.randint(30, 770)
    boxY = random.randint(30, 570)
    target = chr(random.randint(97, 122))

boxCoords()

box = pygame.Rect(boxX, boxY, 30, 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    pygame.draw.rect(screen, (255, 255, 255), box)
    box.x = boxX
    box.y = boxY

    # puts the letter on the box
    font = pygame.font.Font(None, 36)
    text = font.render(target, True, (0, 0, 0))
    textRect = text.get_rect(center=box.center)
    screen.blit(text, textRect)

    keys = pygame.key.get_pressed()
    targetKey = ord(target)
    if keys[targetKey]:
        boxCoords()

    pygame.display.flip()
