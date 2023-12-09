import pygame
import os

pygame.init()

pygame.display.set_caption("Dash")

WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    SQUARE_SIZE = 30

    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, self.SQUARE_SIZE, self.SQUARE_SIZE)
        self.x_vel = PLAYER_VEL
        self.y_vel = 0
        self.animation_count = 0
        self.fall_count = 0
        self.jump_count = 0
        self.hit = False
        self.hit_count = 0
        self.default_sprite = pygame.image.load(os.path.join("Brian", "sprite_9.png")).convert_alpha()
        self.jump_sprite = pygame.image.load(os.path.join("Brian", "sprite_8.png")).convert_alpha()
        self.current_sprite = self.default_sprite

    def jump(self):
        if self.jump_count < 2:
            self.y_vel = -self.GRAVITY * 8
            self.animation_count = 0
            self.jump_count += 1
            if self.jump_count == 1:
                self.fall_count = 0

    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def make_hit(self):
        self.hit = True

    def loop(self, fps):
        self.y_vel += min(1, (self.fall_count / fps) * self.GRAVITY)
        self.move(self.x_vel, self.y_vel)

        if self.hit:
            self.hit_count += 1
        if self.hit_count > fps * 2:
            self.hit = False
            self.hit_count = 0

        self.fall_count += 1

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0

    def hit_head(self):
        self.count = 0
        self.y_vel *= -1

    def draw(self, win, offset_x):
        win.blit(self.current_sprite, (self.rect.x - offset_x, self.rect.y))


def generate_terrain():
    block_size = 96
    terrain = [Block(i * block_size, HEIGHT - block_size, block_size)
               for i in range(-WIDTH // block_size, (WIDTH * 2) // block_size)]
    return terrain


def generate_background():
    background_color = (192, 192, 192)
    bg_image = pygame.Surface((WIDTH, HEIGHT))
    bg_image.fill(background_color)
    return bg_image


def draw(window, background, player, objects, offset_x):
    window.blit(background, (0, 0))

    for obj in objects:
        window.blit(obj.image, (obj.rect.x - offset_x, obj.rect.y))

    player.draw(window, offset_x)

    pygame.display.update()


def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:
        if pygame.sprite.collide_rect(player, obj):
            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()
            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects


def handle_move(player, objects):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        player.jump()

    vertical_collide = handle_vertical_collision(player, objects, player.y_vel)
    to_check = [*vertical_collide]

    for obj in to_check:
        if obj:
            player.make_hit()


def main(window):
    clock = pygame.time.Clock()

    player = Player(100, 100)
    terrain = generate_terrain()

    background = generate_background()

    objects = [*terrain, BLOCKSIZE(0, HEIGHT - 192, 96)]

    offset_x = 0
    scroll_area_width = 200

    run = True
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        player.loop(FPS)
        handle_move(player, objects)
        draw(window, background, player, objects, offset_x)

        if ((player.rect.right - offset_x >= WIDTH - scroll_area_width) and player.x_vel > 0) or (
                (player.rect.left - offset_x <= scroll_area_width) and player.x_vel < 0):
            offset_x += player.x_vel

    pygame.quit()
    quit()


if __name__ == "__main__":
    main(window)
