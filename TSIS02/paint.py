import pygame
import math

def flood_fill(surface, start_pos, fill_color):
    target_color = surface.get_at(start_pos)
    if target_color == fill_color: return
    stack = [start_pos]
    while stack:
        x, y = stack.pop()
        if surface.get_at((x, y)) == target_color:
            surface.set_at((x, y), fill_color)
            if x > 0: stack.append((x - 1, y))
            if x < surface.get_width() - 1: stack.append((x + 1, y))
            if y > 0: stack.append((x, y - 1))
            if y < surface.get_height() - 1: stack.append((x, y + 1))

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 5
    mode = 'blue'
    tool = 1
    temp = 0
    points = []
    shape_start = None
    thickness = [2, 5, 10]
    thickness_index = 1
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 24)
    text_typing = ""
    text_pos = None
    is_typing = False
    while True:
        pressed = pygame.key.get_pressed()
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        for event in pygame.event.get():
            if event.type == pygame.QUIT: return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s and ctrl_held:
                    file_name = f"canvas_{temp}.png"
                    temp += 1
                    pygame.image.save(screen, file_name)
                    print(f"Canvas saved as {file_name}")
            if is_typing:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        points.append(("text", text_pos, text_typing, mode))
                        is_typing = False
                        text_typing = ""
                    elif event.key == pygame.K_ESCAPE:
                        is_typing = False
                        text_typing = ""
                    elif event.key == pygame.K_BACKSPACE: text_typing = text_typing[:-1]
                    else: text_typing += event.unicode
                continue
            if event.type == pygame.KEYDOWN:
                for i in range(1, 10):
                    if event.key == getattr(pygame, f"K_{i}"): tool = i
                if event.key == pygame.K_0: tool = 0
                if event.key == pygame.K_UP:
                    thickness_index = min(len(thickness) - 1, thickness_index + 1)
                    radius = thickness[thickness_index]
                if event.key == pygame.K_DOWN:
                    thickness_index = max(0, thickness_index - 1)
                    radius = thickness[thickness_index]
                if event.key == pygame.K_r: mode = 'red'
                elif event.key == pygame.K_g: mode = 'green'
                elif event.key == pygame.K_b: mode = 'blue'
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]: 
                    if tool == 1: points.append((event.pos, radius, mode))
                    elif tool == 4: points.append(("erase", event.pos, radius))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if tool == 0:
                        snap = screen.copy()
                        color = (0,0,255) if mode == 'blue' else (255,0,0) if mode == 'red' else (0,255,0)
                        flood_fill(snap, event.pos, color)
                        points.append(("flood", snap))
                    if tool in [2, 3, 5, 6, 7, 8]: 
                        if shape_start is None: shape_start = event.pos
                        else:
                            points.append((tool, shape_start, event.pos, mode, radius))
                            shape_start = None
                    elif tool == 1: points.append((event.pos, radius, mode))
                    elif tool == 4: points.append(("erase", event.pos, radius))
                    elif tool == 9:
                        is_typing = True
                        text_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 and tool == 1: points.append(None) 
        screen.fill((0, 0, 0))
        i = 0
        while i < len(points):
            p1 = points[i]
            if p1 is None:
                i += 1
                continue
            if isinstance(p1, tuple) and p1[0] == "flood":
                screen.blit(p1[1], (0, 0))
                i += 1
                continue
            if isinstance(p1, tuple) and p1[0] == "text":
                _, t_pos, t_str, t_mode = p1
                c = (0,0,255) if t_mode == 'blue' else (255,0,0) if t_mode == 'red' else (0,255,0)
                txt_surf = font.render(t_str, True, c)
                screen.blit(txt_surf, t_pos)
                i += 1
                continue
            if isinstance(p1, tuple) and len(p1) == 5:
                s_type, s_start, s_end, s_mode, s_radius = p1
                c = (0,0,255) if s_mode == 'blue' else (255,0,0) if s_mode == 'red' else (0,255,0)
                if s_type == 2:
                    x_min, y_min = min(s_start[0], s_end[0]), min(s_start[1], s_end[1])
                    w, h = abs(s_start[0]-s_end[0]), abs(s_start[1]-s_end[1])
                    pygame.draw.rect(screen, c, pygame.Rect(x_min, y_min, w, h), s_radius)
                elif s_type == 3:
                    dist = math.sqrt((s_end[0]-s_start[0])**2 + (s_end[1]-s_start[1])**2)
                    pygame.draw.circle(screen, c, s_start, int(dist), s_radius)
                elif s_type == 5:
                    pygame.draw.polygon(screen, c, [(s_start[0], s_start[1]), (s_end[0], s_end[1]), (s_start[0], s_end[1])], s_radius)
                elif s_type == 6:
                    x1, y1, x2, y2 = s_start[0], s_start[1], s_end[0], s_end[1]
                    tdt = ((math.sqrt(3)) / 2)
                    third_point = [(((x1+x2) / 2) + tdt * (y1 - y2)), (((y1+y2) / 2) + tdt * (x2 - x1)), ]
                    pygame.draw.polygon(screen, c, [(x1, y1), (x2, y2), (third_point[0], third_point[1])], s_radius)
                elif s_type == 7:
                    x1, y1, x2, y2 = s_start[0], s_start[1], s_end[0], s_end[1]
                    pt1 = [(x2 + x1) / 2, y1] 
                    pt4 = [x2, (y1 + y2) / 2] 
                    pt2 = [x1, (y1 + y2) / 2] 
                    pt3 = [(x2 + x1) / 2, y2]
                    pygame.draw.polygon(screen, c, [pt1, pt2, pt3, pt4], s_radius)
                elif s_type == 8:
                    x1, y1, x2, y2 = s_start[0], s_start[1], s_end[0], s_end[1]
                    pygame.draw.line(screen, c, (x1, y1), (x2, y2), s_radius)
                i += 1
                continue

            if i < len(points) - 1:
                p2 = points[i + 1]
                if p2 is not None and len(p2) == 3:
                    if p1[0] == "erase": pos1, rad1, col1 = p1[1], p1[2], 'black'
                    else: pos1, rad1, col1 = p1[0], p1[1], p1[2]
                    pos2 = p2[1] if p2[0] == "erase" else p2[0]
                    if isinstance(pos1, tuple) and isinstance(pos2, tuple): drawLineBetween(screen, i, pos1, pos2, rad1, col1)
            i += 1
        if is_typing:
            c = (0,0,255) if mode == 'blue' else (255,0,0) if mode == 'red' else (0,255,0)
            live_surf = font.render(text_typing + "|", True, c)
            screen.blit(live_surf, text_pos)
        if shape_start and tool == 8:
            current_mouse_pos = pygame.mouse.get_pos()
            preview_c = (0,0,255) if mode == 'blue' else (255,0,0) if mode == 'red' else (0,255,0)
            pygame.draw.line(screen, preview_c, shape_start, current_mouse_pos, radius)
            pygame.draw.circle(screen, (255, 255, 255), shape_start, 2)
        if shape_start and tool in [2, 3, 5, 6, 7, 8]: pygame.draw.circle(screen, (255, 255, 255), shape_start, 5)
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    if color_mode == 'blue': color = (0, 0, 255)
    elif color_mode == 'red': color = (255, 0, 0)
    elif color_mode == 'green': color = (0, 255, 0)
    else: 
        color = (0, 0, 0) # Default for 'black' / eraser
    dx, dy = start[0] - end[0], start[1] - end[1]
    iterations = max(abs(dx), abs(dy), 1)
    for i in range(iterations):
        progress = 1.0 * i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
main()