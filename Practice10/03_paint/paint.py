import pygame
import math

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    tool = 1
    points = []
    shape_start = None
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return
                if event.key == pygame.K_1: tool = 1
                if event.key == pygame.K_2: tool = 2
                if event.key == pygame.K_3: tool = 3
                if event.key == pygame.K_4: tool = 4
                
                if event.key == pygame.K_UP: radius = min(200, radius + 1)
                if event.key == pygame.K_DOWN: radius = max(1, radius - 1)
                
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]: 
                    if tool == 1:
                        points.append(event.pos)
                    elif tool == 4:
                        points.append(("erase", event.pos, radius))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool in [2, 3]: 
                        if shape_start is None:
                            shape_start = event.pos
                        else:
                            points.append((tool, shape_start, event.pos, mode))
                            shape_start = None
                    elif tool == 1:
                        points.append(event.pos)
                    elif tool == 4:
                        points.append(("erase", event.pos, radius))
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and tool == 1:
                    points.append(None)
                   
        screen.fill((0, 0, 0))
        i = 0
        while i < len(points) - 1:
            p1 = points[i]
            p2 = points[i + 1]
            if p1 is not None and p2 is not None:
                if isinstance(p1, tuple) and len(p1) == 4:
                    s_type, s_start, s_end, s_mode = p1
                    c = (0,0,255) if s_mode == 'blue' else (255,0,0) if s_mode == 'red' else (0,255,0)
                    if s_type == 2:
                        x_min, y_min = min(s_start[0], s_end[0]), min(s_start[1], s_end[1])
                        w, h = abs(s_start[0]-s_end[0]), abs(s_start[1]-s_end[1])
                        pygame.draw.rect(screen, c, pygame.Rect(x_min, y_min, w, h), 2)
                    elif s_type == 3:
                        dist = math.sqrt((s_end[0]-s_start[0])**2 + (s_end[1]-s_start[1])**2)
                        pygame.draw.circle(screen, c, s_start, int(dist), 2)
                
                else:
                    if isinstance(p1, tuple) and p1[0] == "erase":
                        pos1, rad1, col1 = p1[1], p1[2], 'black'
                    else:
                        pos1, rad1, col1 = p1, radius, mode
                    pos2 = p2[1] if (isinstance(p2, tuple) and p2[0] == "erase") else p2
                    if isinstance(pos2, tuple) and len(pos2) == 2:
                        drawLineBetween(screen, i, pos1, pos2, rad1, col1)
            i += 1
        if shape_start and tool == 2:
            pygame.draw.circle(screen, (255, 255, 255), shape_start, 5)

        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    if color_mode == 'blue': 
        color = (c1, c1, c2)
    elif color_mode == 'red': 
        color = (c2, c1, c1)
    elif color_mode == 'green': 
        color = (c1, c2, c1)
    else: 
        color = (0, 0, 0)
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy), 1)
    for i in range(iterations):
        progress = 1.0 * i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()