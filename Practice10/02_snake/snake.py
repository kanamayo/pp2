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
font = pygame.font.SysFont("Roboto", 32)

def food():
    x = random.randint(1, (width - 2 * block) // block) * block
    y = random.randint(1, (height - 2 * block) // block) * block
    return (x, y)

f_pos1 = food()
f_pos2 = food()

while running:
    while not game_over:
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
        if new_h == f_pos1:
            f_pos1 = food()
        elif new_h == f_pos2:
            f_pos2 = food()
        else:
            snake.pop()
        pygame.draw.rect(screen, (255, 0, 0), (f_pos1[0], f_pos1[1], block, block))
        pygame.draw.rect(screen, (255, 0, 0), (f_pos2[0], f_pos2[1], block, block))
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
