import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
FPS = 50
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()


horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()


class Border(pygame.sprite.Sprite):
    def __init__(self, vert, x, y):
        super().__init__(all_sprites)
        if vert:
            self.add(vertical_borders)
            self.image = pygame.Surface([50, 800])
            self.rect = pygame.Rect(x, y, 50, 800)
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([800, 50])
            self.rect = pygame.Rect(x, y, 800, 50)


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites)
        self.image = pygame.Surface([50, 50])
        self.rect = pygame.Rect(x - 25, y - 25, 100, 100)
        self.a = 0
        self.amax = 10
        self.vx, self.vy = self.v = (0, 0)
        self.x, self.y = self.coords = (x, y)

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)


def start_screen():
    intro_text = ["Перемещение героя", "",
                  "Герой двигается",
                  "Карта на месте"]

    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)


running = True
while running:
    screen.fill(pygame.Color("white"))
    Border(1, 0, 0)
    Border(0, 0, 0)
    Border(0, 0, 750)
    Border(1, 750, 0)
    pers = MainCharacter(400, 400)
    all_sprites.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_w:
            pers.move_but_key_pressed('up')
        elif event.type == pygame.K_s:
            pers.move_but_key_pressed('down')
        elif event.type == pygame.K_a:
            pers.move_but_key_pressed('left')
        elif event.type == pygame.K_d:
            pers.move_but_key_pressed('right')
    all_sprites.update()
    pygame.display.flip()
pygame.quit()
