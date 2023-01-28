import platform

import pygame
import sys
import psutil
import gpustat
from GPUtil import GPUtil


def fpsrun():
    fps = str(int(clock.get_fps()))
    fps_text = font.render(fps, 1, pygame.Color("white"))
    return fps_text


class SystemInfo:
    def __init__(self):
        self.gpu_usage = None
        self.gpu_name = None
        self.cpu_usage = None
        self.cpu_name = None


sys_info = SystemInfo()

# Get GPU usage and name
gpu_percent = GPUtil.getGPUs()[0].load
sys_info.gpu_usage = gpu_percent
sys_info.gpu_name = GPUtil.getGPUs()[0].name

# Get CPU usage and name
sys_info.cpu_usage = psutil.cpu_percent()
sys_info.cpu_name = platform.processor()

# Print the information
print("GPU: ", sys_info.gpu_name, " Usage: ", sys_info.gpu_usage, "%")
print("CPU: ", sys_info.cpu_name, " Usage: ", sys_info.cpu_usage, "%")


def get_cpu_usage():
    cpu_usage = psutil.cpu_percent()
    return str(cpu_usage) + "%"


def get_cpu_name():
    # Get CPU information
    cpu_percent = psutil.cpu_percent()
    cpu_name = psutil.cpu_freq().name
    logical_cpus = psutil.cpu_count()
    physical_cpus = psutil.cpu_count(logical=False)


def get_gpu_usage():
    gpu_stats = gpustat.GPUStatCollection.new_query()
    gpu_usage = gpu_stats.gpus[0].utilization
    return str(gpu_usage) + "%"


pygame.init()
height = 700
width = 150
screen = pygame.display.set_mode((height, width))
# screen = pygame.display.set_mode((height,width),pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.SysFont("Century Gothic", 16)

gpu_usage_text = font.render(get_gpu_usage(), 1, pygame.Color("white"))
screen.blit(gpu_usage_text, (60, 50))
cpu_usage_text = font.render(get_cpu_usage(), 1, pygame.Color("white"))
screen.blit(cpu_usage_text, (60, 100))

i = 0
while i <= 10:
    screen.fill((0, 0, 0))
    gpu_usage_text = font.render("GPU: " + sys_info.gpu_name + " Usage: " + str(sys_info.gpu_usage) + "%", True, (255, 255, 255))
    cpu_usage_text = font.render("CPU: " + sys_info.cpu_name + " Usage: " + str(sys_info.cpu_usage) + "%", True, (255, 255, 255))
    screen.blit(fpsrun(), (60, 50))
    screen.blit(gpu_usage_text, (60, 80))
    screen.blit(cpu_usage_text, (60, 110))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    clock.tick(60)
    pygame.display.update()
