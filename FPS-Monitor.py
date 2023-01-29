import pygame
import sys
import psutil
import gpustat
import cpuinfo


pygame.init()
height = 700
width = 300
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Century Gothic", 16)


def fpsrun():
    fps = str(int(clock.get_fps()))
    fps_text = font.render("FPS: " + fps, 1, pygame.Color("white"))
    return fps_text


def get_cpu_usage():
    cpu_info = cpuinfo.get_cpu_info()['brand_raw']
    cpu_usage = psutil.cpu_percent()

    if 'AMD' in cpu_info:
        color = pygame.Color("red")
    elif 'Intel' in cpu_info:
        color = pygame.Color("blue")
    else:
        color = pygame.Color("white")

    cpu_usage_text = font.render("CPU Usage: " + str(cpu_usage) + "%", 1, color)
    return cpu_usage_text

def get_cpu_name():
    cpu_name = cpuinfo.get_cpu_info()['brand_raw']
    if 'AMD' in cpu_name:
        cpu_name_text = font.render("CPU Name: " + cpu_name, 1, pygame.Color("red"))
    elif 'Intel' in cpu_name:
        cpu_name_text = font.render("CPU Name: " + cpu_name, 1, pygame.Color("blue"))
    else:
        cpu_name_text = font.render("CPU Name: " + cpu_name, 1, pygame.Color("white"))
    return cpu_name_text


def get_gpu_usage():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_usage = gpu_stats.gpus[0].utilization
    gpu_usage_text = font.render("GPU Usage: " + str(gpu_usage) + "%", 1, pygame.Color("green"))
    return gpu_usage_text


def get_gpu_name():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_name = gpu_stats.gpus[0].name
    gpu_name_text = font.render("GPU Name: " + gpu_name, 1, pygame.Color("green"))
    return gpu_name_text


def get_ram_info():
    ram_info = psutil.virtual_memory()
    return "Total RAM: " + str(ram_info.total // (1024**2)) + "MB"


def get_ram_usage():
    ram_usage = psutil.virtual_memory().percent
    return str(ram_usage) + "%"


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill(pygame.Color("black"))
    screen.blit(fpsrun(), (20, 20))
    screen.blit(get_cpu_name(), (20, 50))
    screen.blit(get_cpu_usage(), (20, 70))
    screen.blit(get_gpu_name(), (20, 100))
    screen.blit(get_gpu_usage(), (20, 120))
    screen.blit(font.render("RAM Info: " + get_ram_info(), 1, pygame.Color("orange")), (20, 150))
    screen.blit(font.render("RAM Usage: " + get_ram_usage(), 1, pygame.Color("orange")), (20, 170))

    pygame.display.update()
    clock.tick(60)
