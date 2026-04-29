import pygame
import random
import psycopg2
pygame.init()

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="snakeDatabase",
            user="postgres",
            password="manjarro",
            client_encoding='utf8'
        )
        return connection
    except Exception as error:
        print(f"Error connecting to database: {error}")
        return None
def show_leaderboard():
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT p.username, l.score, l.level 
            FROM leaderboard l 
            JOIN players p ON l.player_id = p.player_id 
            ORDER BY l.score DESC LIMIT 10
        """)
        return cur.fetchall()
    return []
def save_final_score(name, final_score, final_level):
    conn = get_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING", (name,))
        cur.execute("SELECT player_id FROM players WHERE username = %s", (name,))
        p_id = cur.fetchone()[0]
        cur.execute("INSERT INTO leaderboard (player_id, score, level) VALUES (%s, %s, %s)", (p_id, final_score, final_level))
        conn.commit()
        cur.close()
        conn.close()
        print("Score saved to leaderboard!")
MENU = "menu"
GAME = "game"
GAMEOVER = "gameover"
LEADERBOARD = "leaderboard"
SETTINGS = "settings"
current_screen = MENU
grid_enabled = True
height, width = 720, 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
running = True
game_over = False
pos_x = screen.get_width() / 2
pos_y = screen.get_height() / 2
block = 40
direction = "right"
snake = [(pos_x, pos_y)]
WHITE, GREEN, RED, BLACK = (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 0)
REDISH, DARK_RED = (174, 36, 72), (139, 0, 0)
YELLOW, BLUE, CYAN = (255, 255, 0), (0, 0, 255), (0, 255, 255)
MENU, GAME, GAMEOVER, LEADERBOARD, SETTINGS = "menu", "game", "gameover", "leaderboard", "settings"
current_screen = MENU
font = pygame.font.SysFont("Roboto", 28)
snake_color = GREEN
fontFruit = pygame.font.SysFont("Roboto", 16)
score = 0
fruit_time = 5000
old_level = 0
score_saved = False
def draw_button(text, x, y, w, h, inactive_color, active_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, active_color, (x, y, w, h))
        if click[0] == 1:
            pygame.time.delay(150)
            return True
    else:
        pygame.draw.rect(screen, inactive_color, (x, y, w, h))
    txt = font.render(text, True, WHITE)
    screen.blit(txt, (x + (w // 2 - txt.get_width() // 2), y + (h // 2 - txt.get_height() // 2)))
    return False
def reset_game():
    global score, level, old_level, snake, direction, game_over, score_saved, obstacles, has_shield, powerup_effect, current_powerup
    score = 0
    level = 0
    old_level = 0
    snake = [(width // 2, height // 2)]
    direction = "right"
    game_over = False
    score_saved = False
    obstacles = []
    has_shield = False
    powerup_effect = None
    current_powerup = None
def get_safe_pos():
    while True:
        x = random.randint(1, (width - 2 * block) // block) * block
        y = random.randint(1, (height - 2 * block) // block) * block
        test_rect = pygame.Rect(x, y, block, block)
        hit_obstacle = any(obs.colliderect(test_rect) for obs in obstacles)
        hit_snake = any(pygame.Rect(s[0], s[1], block, block).colliderect(test_rect) for s in snake)
        if not hit_obstacle and not hit_snake:
            return x, y
def spawn_powerup():
    x, y = get_safe_pos()
    p_type = random.choice(["Speed", "Slow", "Shield"])
    return [x, y, p_type, pygame.time.get_ticks()]
def food():
    x, y = get_safe_pos()
    weight = random.randint(1, 100) % 10
    if weight == 0: weight += 6
    return [x, y, weight]
def poison():
    x, y = get_safe_pos()
    return [x, y]
def disappearing_food():
    x, y = get_safe_pos()
    weight = random.randint(1, 100) % 10
    if weight == 0: weight += 4
    fruit_time = 50
    return [x, y, weight, fruit_time]
obstacles = []
def generate_obstacles(level):
    global obstacles
    obstacles = []
    if level < 3: return
    num_obstacles = (level - 1) * 2
    while len(obstacles) < num_obstacles:
        x = random.randint(1, (width - 2 * block) // block) * block
        y = random.randint(1, (height - 2 * block) // block) * block
        new_rect = pygame.Rect(x, y, block, block)
        head_rect = pygame.Rect(snake[0][0], snake[0][1], block * 3, block * 3)
        if not any(new_rect.collidepoint(p) for p in snake) and not new_rect.colliderect(head_rect):
            obstacles.append(new_rect)
f_pos1 = food()
f_pos2 = food()
f_dis1 = disappearing_food()
f_dis2 = disappearing_food()
f_pois = poison()
current_powerup = None
powerup_effect = None
effect_expiry = 0
has_shield = False
base_speed = 10
def get_username():
    user_text = ""
    entering = True
    while entering:
        screen.fill(WHITE)
        prompt = font.render("Enter Username: " + user_text, True, BLACK)
        screen.blit(prompt, (width // 2 - 150, height // 2))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: entering = False
                elif event.key == pygame.K_BACKSPACE: user_text = user_text[:-1]
                else: user_text += event.unicode
    return user_text
username = get_username()

while running:
    if current_screen == MENU:
        screen.fill(WHITE)
        title = font.render(f"WELCOME, {username.upper()}", True, BLACK)
        screen.blit(title, (width // 2 - title.get_width() // 2, 100))
        if draw_button("PLAY", 540, 250, 200, 50, BLACK, GREEN):
            reset_game()
            current_screen = GAME
        if draw_button("LEADERBOARD", 540, 320, 200, 50, BLACK, BLUE):
            current_screen = LEADERBOARD
        if draw_button("QUIT", 540, 390, 200, 50, DARK_RED, RED):
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        pygame.display.flip()
    elif current_screen == GAME:
        level = score // 15
        if level != old_level:
            generate_obstacles(level)
            old_level = level
            f_pos1 = food()
            f_pos2 = food()
        time_now = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(WHITE)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and direction != "down":
            direction = "up"
        elif keys[pygame.K_s] and direction != "up":
            direction = "down"
        elif keys[pygame.K_a] and direction != "right":
            direction = "left"
        elif keys[pygame.K_d] and direction != "left":
            direction = "right"
        h_x, h_y = snake[0]
        if direction == "up":
            h_y -= block
        elif direction == "down":
            h_y += block
        elif direction == "left":
            h_x -= block
        elif direction == "right":
            h_x += block
        new_h = (h_x, h_y)
        if h_x < 0 or h_x >= width or h_y < 0 or h_y >= height or new_h in snake or any(obs.collidepoint(new_h) for obs in obstacles):
            if has_shield:
                has_shield = False
            else:
                current_screen = GAMEOVER
                continue
        if current_powerup is None and random.random() < 0.2:
            current_powerup = spawn_powerup()
        if current_powerup and time_now - current_powerup[3] > 8000:
            current_powerup = None
        if h_x < 0 or h_x >= width or h_y < 0 or h_y >= height or new_h in snake:
            if has_shield:
                has_shield = False
            else:
                game_over = True
                break
        snake.insert(0, new_h)
        f_dis1[3] -= 1
        if f_dis1[3] <= 0: f_dis1 = disappearing_food()
        f_dis2[3] -= 1
        if f_dis2[3] <= 0: f_dis2 = disappearing_food()
        if h_x == f_pos1[0] and h_y == f_pos1[1]:
            score += int(f_pos1[2])
            f_pos1 = food()
        elif h_x == f_pos2[0] and h_y == f_pos2[1]:
            score += int(f_pos2[2])
            f_pos2 = food()
        elif h_x == f_dis1[0] and h_y == f_dis1[1]:
            score += int(f_dis1[2])
            f_dis1 = disappearing_food()
        elif h_x == f_dis2[0] and h_y == f_dis2[1]:
            score += int(f_dis2[2])
            f_dis2 = disappearing_food()
        elif current_powerup and h_x == current_powerup[0] and h_y == current_powerup[1]:
            p_type = current_powerup[2]
            if p_type == "Shield":
                has_shield = True
            else:
                powerup_effect = p_type
                effect_expiry = time_now + 5000
            current_powerup = None
        elif h_x == f_pois[0] and h_y == f_pois[1]:
            for _ in range(3):
                if len(snake) > 1: snake.pop()
            if len(snake) <= 1: game_over = True
            f_pois = poison()
        else:
            snake.pop()

        for obs in obstacles:
            pygame.draw.rect(screen, BLACK, obs)
        pygame.draw.rect(screen, RED, (f_pos1[0], f_pos1[1], block, block))
        pygame.draw.rect(screen, RED, (f_pos2[0], f_pos2[1], block, block))
        pygame.draw.rect(screen, REDISH, (f_dis1[0], f_dis1[1], block, block))
        pygame.draw.rect(screen, REDISH, (f_dis2[0], f_dis2[1], block, block))
        pygame.draw.rect(screen, DARK_RED, (f_pois[0], f_pois[1], block, block))

        text_f1_weight = font.render(f"{f_pos1[2]}", True, WHITE)
        screen.blit(text_f1_weight, (f_pos1[0], f_pos1[1]))
        text_f2_weight = font.render(f"{f_pos2[2]}", True, WHITE)
        screen.blit(text_f2_weight, (f_pos2[0], f_pos2[1]))

        text_fd1_weight = font.render(f"{f_dis1[2]}", True, WHITE)
        screen.blit(text_fd1_weight, (f_dis1[0], f_dis1[1]))
        text_fd2_weight = font.render(f"{f_dis2[2]}", True, WHITE)
        screen.blit(text_fd2_weight, (f_dis2[0], f_dis2[1]))

        text_fd1_time = font.render(f"{f_dis1[3] // 10}", True, WHITE)
        screen.blit(text_fd1_time, (f_dis1[0] + 28, f_dis1[1] + 20))
        text_fd2_time = font.render(f"{f_dis2[3] // 10}", True, WHITE)
        screen.blit(text_fd2_time, (f_dis2[0] + 28, f_dis2[1] + 20))
        screen.blit(font.render(f"Level: {level}", True, BLACK), (20, 30))
        if current_powerup:
            p_type = current_powerup[2]
            p_color = YELLOW if p_type == "Shield" else CYAN if p_type == "Speed" else BLUE
            pygame.draw.rect(screen, p_color, (*current_powerup[:2], block, block))
        for s in snake:
            s_color = YELLOW if has_shield else GREEN
            pygame.draw.rect(screen, s_color, (s[0], s[1], block, block))
        screen.blit(font.render(f"Score: {score}", True, BLACK), (width - 180, 30))
        if powerup_effect:
            screen.blit(font.render(f"Effect: {powerup_effect}", True, BLACK), (20, 60))
        pygame.display.flip()
        current_fps = base_speed
        if powerup_effect == "Speed": current_fps = 15
        elif powerup_effect == "Slow": current_fps = 8
        clock.tick(current_fps)
    elif current_screen == GAMEOVER:
        if not score_saved:
            save_final_score(username, score, level)
            score_saved = True
            top_scores = show_leaderboard()
        screen.fill(WHITE)
        msg = font.render("GAME OVER", True, RED)
        screen.blit(msg, (width // 2 - msg.get_width() // 2, 50))
        for i, (name, s, lvl) in enumerate(top_scores):
            txt = font.render(f"{i+1}. {name}: {s} (Lvl {lvl})", True, BLACK)
            screen.blit(txt, (width // 2 - 100, 150 + i * 30))
        if draw_button("RETRY", 400, 550, 200, 50, BLACK, GREEN):
            reset_game()
            current_screen = GAME
        if draw_button("MENU", 650, 550, 200, 50, BLACK, BLUE):
            current_screen = MENU
        pygame.display.flip()
    elif current_screen == LEADERBOARD:
        screen.fill(WHITE)
        top_scores = show_leaderboard()
        title = font.render("GLOBAL TOP 10", True, BLACK)
        screen.blit(title, (width // 2 - title.get_width() // 2, 50))
        for i, (name, s, lvl) in enumerate(top_scores):
            txt = font.render(f"{i+1}. {name} - Score: {s} (Lvl: {lvl})", True, BLACK)
            screen.blit(txt, (width // 2 - 150, 150 + i * 40))
        if draw_button("BACK", 540, 600, 200, 50, BLACK, RED):
            current_screen = MENU  
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
        pygame.display.flip()
pygame.quit()