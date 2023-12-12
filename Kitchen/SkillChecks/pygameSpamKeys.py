import pygame, sys

class SpamKeys:
    Name = 'SpamKeys'
    def Run(self, screen):
        box = pygame.Rect(375, 225, 50, 50) # the box the target letter will appear in
        score = pygame.Rect(375, 150, 50, 50) # the rectangle object to contain the score

        # the ASCII values for w and s
        w = chr(119)
        s = chr(115)

        font = pygame.font.Font(None, 36)
        targetKey = ord(w)

        count = 0
        target = 10

        while target - count > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            screen.fill((0, 0, 0))

            pygame.draw.rect(screen, (255, 255, 255), box)
            textKey = font.render(chr(targetKey), True, (0, 0, 0)) # textKey is the current target key
            textRect = textKey.get_rect(center=box.center) # textRect is the rectangle object containing the target key
            screen.blit(textKey, textRect) # displays the target key in the key rectangle

            keys = pygame.key.get_pressed()

            if keys[targetKey]:
                if count < target:
                    count += 1
                    if targetKey == ord(w):
                        targetKey = ord(s)
                    else:
                        targetKey = ord(w)
            
            scoreText = font.render(f"Remaining: {target - count}", True, (255, 255, 255))
            screen.blit(scoreText, (290, 100))

        return 'good'
        