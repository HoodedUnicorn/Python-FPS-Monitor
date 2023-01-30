import pygame
import sys
import psutil

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Century Gothic", 16)

# Create a transparent surface to display the info on
info_surface = pygame.Surface((200, 200), pygame.SRCALPHA)

start_time = pygame.time.get_ticks()
frame_count = 0
fps = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))
    info_surface.fill((0, 0, 0, 0))  # Clear the surface to make it transparent

    # Display CPU usage
    cpu_usage = psutil.cpu_percent()
    cpu_text = font.render("CPU: {:.2f}%".format(cpu_usage), 1, (255, 255, 255))
    info_surface.blit(cpu_text, (20, 20))

    # Display GPU usage
    try:
        import GPUtil
        gpu_devices = GPUtil.getGPUs()
        gpu_usage = gpu_devices[0].load * 100
        gpu_text = font.render("GPU: {:.2f}%".format(gpu_usage), 1, (255, 255, 255))
        info_surface.blit(gpu_text, (20, 50))
    except ImportError:
        pass

    # Display RAM usage
    ram_usage = psutil.virtual_memory().percent
    ram_text = font.render("RAM: {:.2f}%".format(ram_usage), 1, (255, 255, 255))
    info_surface.blit(ram_text, (20, 80))

    # Display FPS
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    frame_count += 1

    if elapsed_time > 1000:
        fps = frame_count / (elapsed_time / 1000.0)
        start_time = current_time
        frame_count = 0

    fps_text = font.render("FPS: {:.2f}".format(fps), 1, (255, 255, 255))
    info_surface.blit(fps_text, (20, 110))

    # Blit the info surface onto the main screen
    screen.blit(info_surface, (20, 20))
    pygame.display.update()
    clock.tick(60)
