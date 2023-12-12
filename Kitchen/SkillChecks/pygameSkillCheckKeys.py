import pygame, sys, random

class RandomKeys:
    Name = 'RandomKeys'
    
    def __init__(self) -> None:
        self.PressesRemaining = 8
        self.CorrectCount = 0
        self.GetNewBoxCoords()
        #self.KeysPressed = pygame.key.get_pressed()
    
    def DrawSkillCheck(self, screen):
        if self.PressesRemaining == 0:
            return
        
        screen.fill((0,0,0))
        pygame.draw.rect(screen, (255, 255, 255), self.TargetBox)

        # puts the letter on the box
        font = pygame.font.Font(None, 36)
        text = font.render(self.TargetKey, True, (0, 0, 0))
        textRect = text.get_rect(center = self.TargetBox.center)
        screen.blit(text, textRect)

        # pressedKeys = pygame.key.get_pressed()
        # if pressedKeys[ord(self.TargetKey)]:
        #     print('correct')
        #     self.CorrectCount += 1
        


    def GetNewBoxCoords(self):
        self.TargetBox = pygame.Rect(random.randint(30, 770), random.randint(30, 570), 30, 30)
        self.TargetKey = chr(random.randint(97, 122))
        self.KeyPressed = False
    
    def Run(self, screen):
        remaining = 8
        correct = 0
        while self.PressesRemaining > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    remaining -= 1
                    self.GetNewBoxCoords()
            

            pygame.draw.rect(screen, (255, 255, 255), self.TargetBox)

            # puts the letter on the box
            font = pygame.font.Font(None, 36)
            text = font.render(self.TargetKey, True, (0, 0, 0))
            textRect = text.get_rect(center = self.TargetBox.center)
            screen.blit(text, textRect)

            keys = pygame.key.get_pressed()
            if keys[self.TargetKey]:
                correct += 1
        
        if correct > 6:
            return 'good'
        elif correct > 4:
            return 'mid'
        else:
            return 'you fucking suck'
            

