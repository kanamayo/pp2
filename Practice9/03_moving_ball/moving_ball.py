import pygame
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball Game")
clock = pygame.time.Clock()
running = True
pos_x = screen.get_width() / 2
pos_y = screen.get_height() / 2
moving = 20
WHITE = (255, 255, 255)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    pygame.draw.circle(screen, "red", (pos_x, pos_y), 25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if pos_y - (moving + 25) >= 0:
            pos_y -= moving
    if keys[pygame.K_s]:
        if pos_y + (moving + 25) <= height:
            pos_y += moving
    if keys[pygame.K_a]:
        if pos_x - (moving + 25) >= 0:
            pos_x -= moving
    if keys[pygame.K_d]:
        if pos_x + (moving + 25) <= width:
            pos_x += moving

    pygame.display.flip()
    dt = clock.tick(60) / 1000
pygame.quit()
