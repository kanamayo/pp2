import pygame
import os

pygame.init()

height, width = 720, 1280
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
font32 = pygame.font.SysFont("meiryo", 32)
font52 = pygame.font.SysFont("meiryo", 52)
playlist = [
    {"file": "music/911 Mr.Lonely.mp3", "title": "911 / Mr. Lonely", "artist": "Tyler, The Creator", "art": "music/cover arts/FLOWERBOY.webp", "album": "Flower Boy"},
    {"file": "music/EARFQUAKE.mp3", "title": "EARFQUAKE", "artist": "Tyler, The Creator", "art": "music/cover arts/IGOR.jpg", "album": "IGOR"},
    {"file": "music/HOT WIND BLOWS.mp3", "title": "HOT WIND BLOWS", "artist": "Tyler, The Creator", "art": "music/cover arts/CMIYGLTES.jpg", "album": "CALL ME IF YOU GET LOST: The Estate Sale"},
    {"file": "music/NEW MAGIC WAND.mp3", "title": "NEW MAGIC WAND", "artist": "Tyler, The Creator", "art": "music/cover arts/IGOR.jpg", "album": "IGOR"},
    {"file": "music/錯乱 - TERRA ver..mp3", "title": "錯乱 - TERRA ver.", "artist": "Sheena Ringo", "art": "music/cover arts/平成風俗.jpg", "album": "平成風俗"}
]
current = 0
playing = False
loaded = False
volume = 0.1
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    if not loaded:
                        pygame.mixer.music.load(playlist[current]["file"])
                        pygame.mixer.music.play()
                        loaded = True
                    else:
                        pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_RIGHT:
                current = (current + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current]["file"])
                pygame.mixer.music.play()
                playing = True
                loaded = True
            elif event.key == pygame.K_LEFT:
                current = (current - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current]["file"])
                pygame.mixer.music.play()
                playing = True
                loaded = True
            elif event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                pygame.mixer.music.set_volume(volume)
            elif event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                pygame.mixer.music.set_volume(volume)

    screen.fill((255, 255, 255))
    queue = font32.render(f"playlist: {current + 1}/{len(playlist)}", True, (0, 0, 0))
    name = font52.render(f"track: {playlist[current]['title']}", True, (0, 0, 0))
    artist = font32.render(f"artist: {playlist[current]['artist']}", True, (0, 0, 0))
    album = font32.render(f"album: {playlist[current]['album']}", True, (0, 0, 0))
    volume_text = font32.render(f"volume: {round(volume * 10, 1)}", True, (0, 0, 0))
    paused_text = font32.render("paused", True, (0, 0, 0))
    playing_text = font32.render("playing...", True, (0, 0, 0))
    cover = pygame.image.load(playlist[current]['art'])
    cover = pygame.transform.scale(cover, (300, 300))
    screen.blit(queue, (50, 185))
    screen.blit(name, (50, 220))
    screen.blit(artist, (50, 290))
    screen.blit(album, (50, 325))
    screen.blit(volume_text, (50, 360))
    screen.blit(cover, (870, 150))
    if not playing:
        screen.blit(paused_text, (50, 395))
    elif playing:
        screen.blit(playing_text, (50, 395))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()