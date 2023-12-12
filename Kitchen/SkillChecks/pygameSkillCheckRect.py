import pygame, sys

class TimingSkillCheck:
    Name = 'TimingSkillCheck'
    
    def Run(self, screen):
        red = ((255, 0, 0))
        green = ((0, 255, 0))
        purple = ((150, 0, 255))

        badArea = pygame.Rect(390, 310, 20, 100)
        midArea = pygame.Rect(390, 270, 20, 80)
        goodArea = pygame.Rect(390, 310, 20, 20)

        speed = 0.4 # how fast the marker will move. this must start as a pos num - the sign will change later
        marker = pygame.Rect(405, 400, 10, 3)
        collisionTolerance = 10
        markerHit = 'none'
        
        while markerHit == 'none':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        if abs(goodArea.right - marker.left) < collisionTolerance:
                            markerHit = 'good'
                        if abs(midArea.right - marker.left) < collisionTolerance:
                            markerHit = 'mid'
                        if abs(goodArea.right - marker.left) < collisionTolerance:
                            markerHit = 'you fucking suck'
            
            # displays the rectangles
            pygame.draw.rect(screen, (red), badArea)
            pygame.draw.rect(screen, (green), midArea)
            pygame.draw.rect(screen, (purple), goodArea)
            pygame.draw.rect(screen, (255, 255, 255), marker)

            # moves the marker
            marker.y -= speed

            if marker.top <= midArea.top:
                speed = -0.4
            if marker.bottom >= badArea.bottom:
                speed = 0.4
            
            print(marker.top, midArea.top)
            print(marker.bottom, badArea.bottom)
            print(speed)

        return markerHit
### not finished yet. the white bar on the side (known as "marker") should be moving for the player to stop ###