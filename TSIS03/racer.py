import pygame, sys, random, time
from pygame.locals import *
pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
DISTANCE = 0
ACTIVE_POWERUP = None
POWERUP_TIME = 0
font_small = pygame.font.SysFont("Arial", 20)
font_large = pygame.font.SysFont("Arial", 60)
game_over_text = font_large.render("Game Over", True, (0, 0, 0))
background = pygame.image.load("AnimatedStreet.png")
DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer")

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.type = type
        if self.type == "oil":
            self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (50, 50, 50), (20, 20), 20)
        else:
            self.image = pygame.Surface((50, 30))
            self.image.fill((200, 100, 0))
        self.rect = self.image.get_rect()
        self.spawn()
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
class PowerUp(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.type = random.choice(["Nitro", "Shield", "Repair"])
        self.image = pygame.Surface((30, 30))
        colors = {"Nitro": (255, 255, 0), "Shield": (0, 255, 255), "Repair": (0, 255, 0)}
        self.image.fill(colors[self.type])
        self.rect = self.image.get_rect()
        self.spawn_time = time.time()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -50)
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT or time.time() - self.spawn_time > 8:
            self.kill()
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.spawn()
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(-900, -100))
    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            return True
        return False
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Coin.png"), (40, 40))
        self.rect = self.image.get_rect()
        self.spawn()
    def spawn(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), -100)
        self.weight = random.choice([1, 2, 3])
    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        m_speed = 12 if ACTIVE_POWERUP == "Nitro" else 6
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-m_speed, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(m_speed, 0)
menu = True
while menu:
    DISPLAYSURF.fill((0,0,0))
    DISPLAYSURF.blit(font_large.render("Racer Game", True, (255,255,255)), (100, 200))
    DISPLAYSURF.blit(font_small.render("Press SPACE to Start", True, (255,255,255)), (110, 300))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT: pygame.quit(); sys.exit()
        if event.type == KEYDOWN and event.key == K_SPACE: menu = False
P1 = Player()
E1 = Enemy()
C1 = Coin()
enemies = pygame.sprite.Group(E1)
coins = pygame.sprite.Group(C1)
obstacles = pygame.sprite.Group()
powerups = pygame.sprite.Group()
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
SPAWN_OBSTACLE = pygame.USEREVENT + 2
pygame.time.set_timer(SPAWN_OBSTACLE, 3000)
SPAWN_POWERUP = pygame.USEREVENT + 3
pygame.time.set_timer(SPAWN_POWERUP, 10000)
bg_y1, bg_y2 = 0, -SCREEN_HEIGHT

while True:
    required_enemies = (SCORE + (COINS // 5)) // 10
    if required_enemies < 1: 
        required_enemies = 1
    current_enemy_count = len(enemies)
    if current_enemy_count < required_enemies:
        new_enemy = Enemy()
        enemies.add(new_enemy)
    elif current_enemy_count > required_enemies:    
        for en in enemies:
            if en.rect.top > SCREEN_HEIGHT or en.rect.bottom < 0:
                en.kill()
                break
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.1 
            DISTANCE += 1
        if event.type == SPAWN_OBSTACLE:
            obstacles.add(Obstacle(random.choice(["oil", "barrier"])))
        if event.type == SPAWN_POWERUP:
            if len(powerups) == 0: powerups.add(PowerUp())
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    bg_y1 += SPEED
    bg_y2 += SPEED
    if bg_y1 >= SCREEN_HEIGHT: bg_y1 = -SCREEN_HEIGHT
    if bg_y2 >= SCREEN_HEIGHT: bg_y2 = -SCREEN_HEIGHT
    DISPLAYSURF.blit(background, (0, bg_y1))
    DISPLAYSURF.blit(background, (0, bg_y2))
    DISPLAYSURF.blit(P1.image, P1.rect)
    P1.move()
    for en in enemies:
        if en.move():
            SCORE += 1
            en.spawn()
        DISPLAYSURF.blit(en.image, en.rect)
    for c in coins:
        DISPLAYSURF.blit(c.image, c.rect)
        c.move()
    for obs in obstacles:
        DISPLAYSURF.blit(obs.image, obs.rect)
        obs.move()
    for p in powerups:
        DISPLAYSURF.blit(p.image, p.rect)
        p.move()
    c_hit = pygame.sprite.spritecollideany(P1, coins)
    if c_hit:
        COINS += c_hit.weight
        c_hit.spawn()
    p_hit = pygame.sprite.spritecollideany(P1, powerups)
    if p_hit:
        ACTIVE_POWERUP = p_hit.type
        POWERUP_TIME = time.time() + 5
        if ACTIVE_POWERUP == "Nitro": SPEED += 5
        p_hit.kill()
    if ACTIVE_POWERUP and time.time() > POWERUP_TIME:
        if ACTIVE_POWERUP == "Nitro": SPEED -= 5
        ACTIVE_POWERUP = None
    if pygame.sprite.spritecollideany(P1, enemies) or pygame.sprite.spritecollideany(P1, obstacles):
        if ACTIVE_POWERUP == "Shield":
            ACTIVE_POWERUP = None
            for h in pygame.sprite.spritecollide(P1, enemies, False): h.rect.top = -100
            for h in pygame.sprite.spritecollide(P1, obstacles, True): pass
        else:
            DISPLAYSURF.fill((255, 0, 0))
            DISPLAYSURF.blit(game_over_text, (30, 250))
            pygame.display.update()
            time.sleep(2)
            pygame.quit()
            sys.exit()
    s_txt = font_small.render(f"Score: {SCORE} | Coins: {COINS}", True, (0,0,0))
    d_txt = font_small.render(f"Dist: {DISTANCE}m | Power: {ACTIVE_POWERUP}", True, (0,0,0))
    DISPLAYSURF.blit(s_txt, (10, 10))
    DISPLAYSURF.blit(d_txt, (10, 35))
    pygame.display.update()
    FramePerSec.tick(FPS)