import pygame
import random
pygame.init()

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
WHITE = (255, 255, 255)
font = pygame.font.SysFont("Roboto", 28)
fontFruit = pygame.font.SysFont("Roboto", 16)
score = 0
fruit_time = 5000

def food():
    x = random.randint(1, (width - 2 * block) // block) * block
    y = random.randint(1, (height - 2 * block) // block) * block
    weight = random.randint(1, 100) % 10
    if weight == 0: weight += 6
    return [x, y, weight]
def disappearing_food():
    x = random.randint(1, (width - 2 * block) // block) * block
    y = random.randint(1, (height - 2 * block) // block) * block
    weight = random.randint(1, 100) % 10
    if weight == 0: weight += 4
    fruit_time = 50
    return [x, y, weight, fruit_time]


f_pos1 = food()
f_pos2 = food()
f_dis1 = disappearing_food()
f_dis2 = disappearing_food()

while running:
    while not game_over:
        # time_now = 
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
        # if new_h in snake:
        
        if h_x < 0 or h_x >= width or h_y < 0 or h_y >= height or new_h in snake:
            game_over = True
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
        else:
            snake.pop()
        pygame.draw.rect(screen, (255, 0, 0), (f_pos1[0], f_pos1[1], block, block))
        pygame.draw.rect(screen, (255, 0, 0), (f_pos2[0], f_pos2[1], block, block))
        pygame.draw.rect(screen, (174, 36, 72), (f_dis1[0], f_dis1[1], block, block))
        pygame.draw.rect(screen, (174, 36, 72), (f_dis2[0], f_dis2[1], block, block))
        
        text_f1_weight = font.render(f"{f_pos1[2]}", True, (255, 255, 255))
        screen.blit(text_f1_weight, (f_pos1[0], f_pos1[1]))
        text_f2_weight = font.render(f"{f_pos2[2]}", True, (255, 255, 255))
        screen.blit(text_f2_weight, (f_pos2[0], f_pos2[1]))

        text_fd1_weight = font.render(f"{f_dis1[2]}", True, (255, 255, 255))
        screen.blit(text_fd1_weight, (f_dis1[0], f_dis1[1]))
        text_fd2_weight = font.render(f"{f_dis2[2]}", True, (255, 255, 255))
        screen.blit(text_fd2_weight, (f_dis2[0], f_dis2[1]))

        text_fd1_time = font.render(f"{f_dis1[3] // 10}", True, (255, 255, 255))
        screen.blit(text_fd1_time, (f_dis1[0] + 28, f_dis1[1] + 20))
        text_fd2_time = font.render(f"{f_dis2[3] // 10}", True, (255, 255, 255))
        screen.blit(text_fd2_time, (f_dis2[0] + 28, f_dis2[1] + 20))



        score_text = font.render(str(score), True, (0, 0, 0))
        screen.blit(score_text, (width - 100, 30))
        for s in snake:
            pygame.draw.rect(screen, (0, 255, 0), (s[0], s[1], block, block))
        pygame.display.flip()
        dt = clock.tick(10) / 1000
    text1 = font.render("Game Over", True, (0, 0, 0))
    text2 = font.render("Press any key to Exit", True, (0, 0, 0))
    screen.blit(text1, (width // 2 -100, height // 2))
    screen.blit(text2, (width // 2 -100, height // 2 +30))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            running = False
            game_over = False
    pygame.display.flip()
pygame.quit()
