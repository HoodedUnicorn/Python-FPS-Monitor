import pygame
import sys
import psutil
import gpustat


def get_gpu_usage():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_usage = gpu_stats.gpus[0].utilization
    return str(gpu_usage) + "%"


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return str(cpu_usage) + "%"


pygame.init()
height = 150
width = 150
screen = pygame.display.set_mode((height, width))
# screen = pygame.display.set_mode((height,width),pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Century Gothic", 30)

gpu_usage_text = font.render(get_gpu_usage(), 1, pygame.Color("white"))
screen.blit(gpu_usage_text, (60, 50))
cpu_usage_text = font.render(get_cpu_usage(), 1, pygame.Color("white"))
screen.blit(cpu_usage_text, (60, 100))


def fpsrun():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("white"))
    return fps_text


def get_gpu_usage():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_usage = gpu_stats.gpus[0].utilization
    return str(gpu_usage) + "%"


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return str(cpu_usage) + "%"


i = 0
while i <= 10:
    screen.fill((0, 0, 0))
    gpu_usage_text = font.render(get_gpu_usage(), 1, pygame.Color("white"))
    cpu_usage_text = font.render(get_cpu_usage(), 1, pygame.Color("white"))
    screen.blit(fpsrun(), (60, 50))
    screen.blit(gpu_usage_text, (60, 80))
    screen.blit(cpu_usage_text, (60, 110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    pygame.display.update()

