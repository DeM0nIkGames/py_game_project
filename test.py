import pygame
import os
import random
from random import randint


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites1)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


class AnimatedGoat(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(all_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns, sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert_alpha()
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def first_map():
    Box(200, 200)
    Box(550, 550)
    Box(200, 550)
    Box(550, 200)


def main_fire(hero, direction):
    bullet = Bullet(hero, direction, False)
    bullet.add(good_bullets)


def enemy_fire(x, y, direction):
    bullet = EnemyBullets(x, y, direction)
    bullet.add(bad_bullets)


all_sprites1 = pygame.sprite.Group()
pygame.init()
screen_size = (800, 800)
screen = pygame.display.set_mode(screen_size)
FPS = 100
clock = pygame.time.Clock()
left = load_image("left_goat.png")
right = load_image("right_goat.png")
horizontal_borders = pygame.sprite.Group()
vertical_borders = pygame.sprite.Group()
main_character = pygame.sprite.Group()
bad_bullets = pygame.sprite.Group()
good_bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
boxes = pygame.sprite.Group()
main = pygame.sprite.Group()
e_l = AnimatedSprite(load_image("enemy_left.png"), 3, 1, 800, 800)
e_r = AnimatedSprite(load_image("enemy_right.png"), 3, 1, 800, 800)
goat_left = AnimatedSprite(load_image("goat_ani_1.png"), 6, 1, 800, 800)
goat_right = AnimatedSprite(load_image("goat_ani.png"), 6, 1, 800, 800)
# left_enemy = AnimatedSprite(load_image("enemy_left.png"), 3, 2, 200, 200)
# right_enemy = AnimatedSprite(load_image("enemy_right.png"), 3, 2, 300, 300)
floor = load_image("floor.png")
vertical = load_image("horizontal.png")
horizontal = load_image("vertical.png")
enemy_left = load_image("enemy_left.png")
enemy_right = load_image("enemy_right.png")
rockets = pygame.sprite.Group()
bosses = pygame.sprite.Group()


class FirstBoss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites1)
        self.image = e_r.image
        self.rect = self.image.get_rect().move(x, y)
        self.hp = 50
        self.dir = "right"
        self.x = self.rect.x
        self.y = self.rect.y
        self.counter = 10
        self.add(bosses)

    def move(self):
        move = randint(1, 5)
        if move == 1:
            self.image = e_l.image
            self.rect.x -= 10
            self.x = self.rect.x
            self.y = self.rect.y
            self.dir = "left"
        elif move == 2:
            self.image = e_r.image
            self.rect.x += 10
            self.x = self.rect.x
            self.y = self.rect.y
            self.dir = "right"
        elif move == 3:
            self.rect.y += 10
            self.x = self.rect.x
            self.y = self.rect.y
        else:
            self.rect.y -= 10
            self.x = self.rect.x
            self.y = self.rect.y
        if self.rect.x + 4 > 700:
            self.rect.x -= 10
            self.x = self.rect.x
            self.y = self.rect.y
        elif self.rect.x - 4 < 50:
            self.rect.x += 10
            self.x = self.rect.x
            self.y = self.rect.y
        elif self.rect.y + 4 > 700:
            self.rect.y -= 10
            self.x = self.rect.x
            self.y = self.rect.y
        elif self.rect.y - 4 < 50:
            self.rect.y += 10
            self.x = self.rect.x
            self.y = self.rect.y
        if (140 <= self.rect.x + 10 <= 240 or 500 <= self.rect.x + 10 <= 630) and (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630):
            self.rect.x -= 20
        if (140 <= self.rect.x - 10 <= 270 or 500 <= self.rect.x - 10 <= 630) and (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630):
            self.rect.x += 20
        if (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630) and (140 <= self.rect.x + 10 <= 270 or 500 <= self.rect.x + 10 <= 630):
            self.rect.y -= 20
        if (120 <= self.rect.y - 10 <= 270 or 500 <= self.rect.y - 10 <= 630) and (140 <= self.rect.x - 10 <= 270 or 500 <= self.rect.x - 10 <= 630):
            self.rect.y += 20

    def shoot(self, dir):
        if dir == "left":
            self.dir = "left"
            self.image = e_l.image
        else:
            self.dir = "right"
            self.image = e_r.image
        enemy_fire(self.x, self.y, self.dir)

    def rockets(self):
        if self.dir == "left":
            Rockets(self.x, self.y, "left")
        else:
            Rockets(self.x, self.y, "right")

    def update(self):
        if pygame.sprite.spritecollide(self, good_bullets, True):
            self.hp -= 1
        if self.hp <= 0:
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, hero, direction, bad):
        super().__init__(all_sprites1)
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect().move(hero.rect.x + 10, hero.rect.y + 10)
        if direction == 'left':
            self.vx = -40
        else:
            self.vx = 40
        if bad:
            self.add(bad_bullets)
        else:
            self.add(good_bullets)

    def update(self):
        self.rect.x += self.vx
        if pygame.sprite.spritecollide(self, horizontal_borders, True) or pygame.sprite.spritecollide(self, vertical_borders, True) or pygame.sprite.spritecollide(self, boxes, False):
            self.remove(all_sprites1)


class EnemyBullets(pygame.sprite.Sprite):
    def __init__(self, x, y, direction="untitled", vx=0, vy=0):
        super().__init__(all_sprites1)
        self.image = load_image("bullet.png")
        self.rect = self.image.get_rect().move(x + 10, y + 10)
        if direction == "left":
            self.vx = -10
        elif direction == "right":
            self.vx = 10
        else:
            self.vx = vx
        self.vy = vy
        self.add(bad_bullets)

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if pygame.sprite.spritecollide(self, horizontal_borders, True) or pygame.sprite.spritecollide(self, vertical_borders, True) or pygame.sprite.spritecollide(self, boxes, False):
            self.remove(all_sprites1)


class Rockets(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__(all_sprites1)
        if direction == 'left':
            self.vx = -5
            self.image = load_image("rocket_left.png")
        else:
            self.vx = 5
            self.image = load_image("rocket.png")
        self.rect = self.image.get_rect().move(x + 10, y + 10)
        self.add(rockets)

    def update(self):
        self.rect.x += self.vx
        if pygame.sprite.spritecollide(self, horizontal_borders, True) or pygame.sprite.spritecollide(self, vertical_borders, True) or pygame.sprite.spritecollide(self, boxes, False):
            EnemyBullets(self.rect.x, self.rect.y, vx=-10, vy=0)
            EnemyBullets(self.rect.x, self.rect.y, vx=10, vy=0)
            EnemyBullets(self.rect.x, self.rect.y, vx=0, vy=10)
            EnemyBullets(self.rect.x, self.rect.y, vx=0, vy=-10)
            EnemyBullets(self.rect.x, self.rect.y, vx=10, vy=-10)
            EnemyBullets(self.rect.x, self.rect.y, vx=-10, vy=-10)
            EnemyBullets(self.rect.x, self.rect.y, vx=-10, vy=10)
            EnemyBullets(self.rect.x, self.rect.y, vx=10, vy=10)
            self.remove(all_sprites1)


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites1)
        self.add(boxes)
        self.image = load_image("box.png")
        self.rect = pygame.Rect(x, y, 100, 100)


class Border(pygame.sprite.Sprite):
    def __init__(self, vert, x, y):
        super().__init__(all_sprites1)
        if vert:
            self.add(vertical_borders)
            self.image = vertical
            self.rect = pygame.Rect(x, y, 50, 800)
        else:
            self.add(horizontal_borders)
            self.image = horizontal
            self.rect = pygame.Rect(x, y, 800, 50)


class MainCharacter1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites1)
        self.image = goat_right.image
        self.rect = self.image.get_rect().move(x - 50, y - 50)
        self.vx, self.vy = 0, 0
        self.add(main)
        self.hp = 5
        self.dir = right

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        self.vx = 0
        self.vy = 0
        if pygame.sprite.spritecollide(self, bad_bullets, True):
            self.hp -= 1
        if pygame.sprite.spritecollide(self, rockets, True):
            self.hp -= 2
        self.rect = self.rect.move(self.vx, self.vy)

    def move(self, movement):
        if movement == "up":
            self.vy -= 10
        elif movement == "down":
            self.vy += 10
        elif movement == "left":
            self.dir = left
            self.vx -= 10
        elif movement == "right":
            self.dir = right
            self.vx += 10
        if self.rect.x + 10 > 670:
            self.rect.x -= 20
        elif self.rect.x - 10 < 50:
            self.rect.x += 20
        elif self.rect.y + 10 > 650:
            self.rect.y -= 20
        elif self.rect.y - 10 < 50:
            self.rect.y += 20
        if (140 <= self.rect.x + 10 <= 240 or 500 <= self.rect.x + 10 <= 630) and (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630):
            self.rect.x -= 20
        if (140 <= self.rect.x - 10 <= 270 or 500 <= self.rect.x - 10 <= 630) and (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630):
            self.rect.x += 20
        if (140 <= self.rect.y + 10 <= 270 or 500 <= self.rect.y + 10 <= 630) and (140 <= self.rect.x + 10 <= 270 or 500 <= self.rect.x + 10 <= 630):
            self.rect.y -= 20
        if (120 <= self.rect.y - 10 <= 270 or 500 <= self.rect.y - 10 <= 630) and (140 <= self.rect.x - 10 <= 270 or 500 <= self.rect.x - 10 <= 630):
            self.rect.y += 20


p, e = 0, 0


# pygame.init()
# screen_size = (800, 800)
# screen = pygame.display.set_mode(screen_size)
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
# clock = pygame.time.Clock()
f = 0
arrows = pygame.sprite.Group()


class Arrow(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__(all_sprites2)
        self.image = load_image('стрела.png')
        self.pos = (0, 0)
        self.add(arrows)
        if position in (1, 3, 5):
            self.im_code = 1
        else:
            self.im_code = 2
        self.direction = 1
        self.update(position)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            self.pos[0], self.pos[1])

    def update(self, position):
        if self.im_code == 1:
            self.image = self.image = load_image('стрела.png')
        else:
            self.image = load_image('стрела2.png')
        if position == 1:
            self.direction = -1
            self.pos = (800, 165)
            x, y = self.pos
            self.rect = self.image.get_rect().move(x, y)
        elif position == 2:
            self.direction = 1
            self.pos = (-135, 255)
            x, y = self.pos
            self.rect = self.image.get_rect().move(x, y)
        elif position == 3:
            self.direction = -1
            self.pos = (800, 390)
            x, y = self.pos
            self.rect = self.image.get_rect().move(x, y)
        elif position == 4:
            self.direction = 1
            self.pos = (-135, 525)
            x, y = self.pos
            self.rect = self.image.get_rect().move(x, y)
        elif position == 5:
            self.direction = -1
            self.pos = (800, 635)
            x, y = self.pos
            self.rect = self.image.get_rect().move(x, y)


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(all_sprites2)
        self.image = load_image('goat(1).png')
        self.im_code = 1
        self.add(all_sprites2)
        self.rect = self.image.get_rect().move(x, y)
        self.pos = x, y

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            self.pos[0], self.pos[1])

    def update(self, key):
        x = self.pos[0]
        if key == 0:
            self.im_code = 2
            if x // 50 % 2 == 0:
                self.image = load_image('goat21.png')
            else:
                self.image = load_image('goat22.png')
        elif key == 1:
            self.im_code = 1
            if x // 50 % 2 == 0:
                self.image = load_image('goat11.png')
            else:
                self.image = load_image('goat12.png')
        elif key == 2:
            self.im_code = 3
            self.image = load_image('goat3.png')

    def falling(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(
            self.pos[0], self.pos[1])


def move(hero, movement):
    x = hero.pos[0]
    y = hero.pos[1]
    if movement == "up":
        if (x in range(70, 210) or x in range(480, 620)) and y > 100:
            hero.update(2)
            hero.move(x, y - 1)
    elif movement == "down":
        if (x in range(70, 210) or x in range(480, 620)) and y < 575:
            hero.update(2)
            hero.move(x, y + 1)
    elif movement == "left":
        if x in range(0, 810):
            hero.update(0)
            hero.move(x - 1, y)
    elif movement == "right":
        if x in range(-200, 700):
            hero.update(1)
            hero.move(x + 1, y)


def move_arrow(ar, coords, l_code):
    x, y = coords
    ar.move(x + 5 * l_code * ar.direction, y)


def terminate_arrow(pos):
    global arrow
    x = pos[0]
    if x > 800 or x < -140:
        arrow.kill()
        position = random.randint(1, 5)
        arrow = Arrow(position)


def correct_cords(pers):
    y = pers.pos[1]
    global f
    if f in (1, 2) and y in (range(225, 236)):
        f = 0
        pers.move(pers.pos[0], 225)
    elif f in (1, 2) and y > 575:
        f = 0
        pers.move(pers.pos[0], 575)


def check():
    global f
    if pers.pos[1] not in (225, 575) and (pers.pos[0] in range(250, 450) or pers.pos[0] < 40 or pers.pos[0] > 650):
        if pers.im_code == 1:
            f = 1
        else:
            f = 2
    else:
        f = 0


def fall(hero):
    x = hero.pos[0]
    y = hero.pos[1]
    if f == 1:
        hero.falling(x + 2, y + 10)
    if f == 2:
        hero.falling(x - 2, y + 10)


running = True
running1 = False
running2 = False
pers = MainCharacter(400, 575)
arrow = Arrow(1)


def start_screen():
    fon = pygame.transform.scale(load_image('fon.jpg'), screen_size)
    FPS = 10
    goat = AnimatedGoat(load_image("goat_ani(1).png"), 6, 1, 300, 100)
    global running, running1, running2

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x in range(100, 350) and y in range(670, 750):
                    running1 = True
                elif x in range(430, 690) and y in range(670, 750):
                    running2 = True
                else:
                    break
                running = False
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.flip()

        clock.tick(FPS)


def game1():
    global running, running1, running2
    perss = MainCharacter1(150, 150)
    en = FirstBoss(650, 650)
    global p, e
    p = perss.hp
    e = en.hp
    first_map()
    while running1:
        if perss.hp <= 0 or en.hp <= 0:
            p = perss.hp
            e = en.hp
            perss.kill()
            en.kill()
            end = True
            while end:
                fon1 = pygame.transform.scale(load_image('wasted.png'), screen_size)
                screen.blit(fon1, (0, 0))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        end = False
                        running1 = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if pos[0] in range(250, 550) and pos[1] in range(550, 600):
                            perss.kill()
                            en.kill()
                            end = False
                            running1 = True
                            game1()
                pygame.display.flip()
        Border(1, 0, 0)
        Border(0, 0, 0)
        Border(0, 0, 750)
        Border(1, 750, 0)
        screen.blit(floor, (0, 0))
        all_sprites1.draw(screen)
        vertical_borders.draw(screen)
        horizontal_borders.draw(screen)
        if randint(1, 5) == 1:
            en.move()
        if randint(1, 100) == 1:
            en.rockets()
            if -10 <= en.y - perss.rect.y <= 10:
                if en.x < perss.rect.x:
                    en.shoot("right")
                elif en.x > perss.rect.x:
                    en.shoot("left")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running1 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if x in range(750, 800) and y in range(0, 50):
                    en.kill()
                    perss.kill()
                    running1 = False
                    running = True
                else:
                    if perss.dir == "left":
                        main_fire(perss, "left")
                    else:
                        main_fire(perss, "right")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            perss.move("up")
        elif keys[pygame.K_s]:
            perss.move("down")
        elif keys[pygame.K_a]:
            perss.move("left")
            perss.dir = "left"
            perss.image = goat_left.image
        elif keys[pygame.K_d]:
            perss.move("right")
            perss.dir = "right"
            perss.image = goat_right.image
        perss.update()
        all_sprites1.update()
        font = pygame.font.Font(None, 30)
        text = font.render(f"Здоровья осталось у игрока: {perss.hp}", True, (100, 255, 100))
        screen.blit(text, (0, 0))
        font = pygame.font.Font(None, 30)
        text = font.render(f"Здоровья осталось у противника: {en.hp}", True, (100, 255, 100))
        screen.blit(text, (350, 0))
        screen.blit(load_image("home_button.png"), (750, 0))
        pygame.display.flip()

        clock.tick(FPS)
        pygame.display.update()
    running1 = False


def game_2():
    global running, running1, running2, pers, arrow
    FPS1 = 50
    pygame.key.set_repeat(2)
    level_cerf = load_image('lev1.png')
    l_code = 1
    while running2:
        fon1 = pygame.transform.scale(load_image('fon2.png'), screen_size)
        while pygame.sprite.spritecollideany(pers, arrows):
            fon1 = pygame.transform.scale(load_image('wasted.png'), screen_size)
            screen.blit(fon1, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pers.kill()
                    arrow.kill()
                    running2 = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] in range(250, 550) and pos[1] in range(550, 600):
                        pers.kill()
                        arrow.kill()
                        pers = MainCharacter(400, 575)
                        arrow = Arrow(1)
            pygame.display.flip()
        screen.blit(fon1, (0, 0))
        screen.blit(level_cerf, (350, 25))
        all_sprites2.draw(screen)
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if x in range(740, 800) and y in range(0, 60):
                    running = True
                    running2 = False
                if x in range(350, 370) and y in range(25, 70):
                    if l_code == 2:
                        l_code = 1
                        level_cerf = load_image('lev1.png')
                    elif l_code == 3:
                        l_code = 2
                        level_cerf = load_image('lev2.png')
                if x in range(450, 470) and y in range(25, 70):
                    if l_code == 1:
                        l_code = 2
                        level_cerf = load_image('lev2.png')
                    elif l_code == 2:
                        l_code = 3
                        level_cerf = load_image('lev3.png')
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    move(pers, "up")
                elif event.key == pygame.K_s:
                    move(pers, "down")
                elif event.key == pygame.K_a:
                    move(pers, "left")
                elif event.key == pygame.K_d:
                    move(pers, "right")
        move_arrow(arrow, arrow.pos, l_code)
        terminate_arrow(arrow.pos)
        check()
        correct_cords(pers)
        fall(pers)
        clock.tick(FPS1)
        pygame.display.update()


while running or running1 or running2:
    if running:
        start_screen()
    elif running1:
        game1()
    elif running2:
        game_2()
pygame.quit()
