import pygame
import datetime
pygame.init()

height = 720
width = 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()
running = True
pos_x = width / 2
pos_y = height / 2
WHITE = (255, 255, 255)

clock_face = pygame.image.load("./sprites/watch.png")
secondHand = pygame.image.load("./sprites/seconds.png")
minuteHand = pygame.image.load("./sprites/minutes.png")
hourHand = pygame.image.load("./sprites/hours.png")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    screen.blit(clock_face, (pos_x - 264, pos_y - 266))
    
    current = datetime.datetime.now()
    seconds = current.second
    minutes = current.minute
    hours = current.hour % 12

    sR = pygame.transform.rotate(secondHand, -(seconds*6))
    sA = sR.get_rect(center = secondHand.get_rect(center = (pos_x - 2, pos_y - 1)).center)
    screen.blit(sR, sA)

    mR = pygame.transform.rotate(minuteHand, -(minutes * 6))
    mA = mR.get_rect(center = minuteHand.get_rect(center = (pos_x - 2, pos_y)).center)
    screen.blit(mR, mA)
    
    hR = pygame.transform.rotate(hourHand, -(hours * 30))
    hA = hR.get_rect(center = hourHand.get_rect(center = (pos_x - 3, pos_y)).center)
    screen.blit(hR, hA)
    
    pygame.display.flip()
    dt = clock.tick(60)
pygame.quit()
