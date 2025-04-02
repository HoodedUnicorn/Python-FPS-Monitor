import pygame
import sys
import psutil
import win32api
import win32gui
import win32con
import time


# To run PresentMon or any FPS capture tool

# Try importing GPUtil, set to None if unavailable
try:
    import GPUtil
except ImportError:
    GPUtil = None  # Prevent errors if GPUtil is missing

pygame.init()

# Set overlay window properties
WIDTH, HEIGHT = 300, 300  # Increased height to fit more information
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.NOFRAME)  # No border window
pygame.display.set_caption("Performance Overlay")

# Get window handle
hwnd = pygame.display.get_wm_info()["window"]

# Get screen width
screen_width = win32api.GetSystemMetrics(0)

# Move 10 cm (≈ 378 pixels) to the left
shift_left = 378

# Set window position safely
default_x, default_y = (screen_width - WIDTH) // 2, 20  # Centered by default
x = max(0, default_x - shift_left)  # Ensures it stays on-screen
y = 20  # Fixed top position

# Move window to the new position
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x, y, WIDTH, HEIGHT, win32con.SWP_SHOWWINDOW)

# Make window always on top and transparent
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd,
                                              win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0, 0, 0), 0, win32con.LWA_COLORKEY)

# Create clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont("Century Gothic", 20, bold=True)  # Reduced font size to fit more text

# Initialize variables
last_fps_update_time = time.time()
fps = 0


# Function to get FPS using PresentMon
import subprocess
import os
import time

def get_fps_from_presentmon():
    try:
        # Ensure PresentMon path is correctly escaped or use raw string
        presentmon_path = r'C:\Users\HoodedUnicorn\Downloads\PresentMon-2.3.0-x64.exe'

        # Run PresentMon and capture FPS data directly to stdout
        subprocess.run(
            [presentmon_path, '--stop_existing_session', '--process_name', 'FortniteClient-Win64-Shipping_BE.exe', '--output_stdout'],
            check=True)

        # Wait a moment to allow PresentMon to capture some FPS data
        time.sleep(5)

        # This will print the FPS data to your terminal
        print("FPS data captured successfully.")
        return None
    except Exception as e:
        print(f"Error getting FPS: {e}")
        return None

# Wrap text to fit within the width of the window
def wrap_text(text, max_width):
    """Wrap the text to fit within the max_width."""
    lines = []
    words = text.split(" ")
    current_line = ""

    for word in words:
        # Try adding the word to the current line
        test_line = current_line + ((" " if current_line else "") + word)
        if font.size(test_line)[0] <= max_width:
            current_line = test_line  # If it fits, continue adding words
        else:
            lines.append(current_line)  # Add the current line to lines
            current_line = word  # Start a new line with the word
    if current_line:
        lines.append(current_line)  # Add the last line
    return lines


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get FPS using PresentMon once every second (or desired interval)
    current_time = time.time()
    if current_time - last_fps_update_time >= 1:  # Update FPS every 1 second
        fps_value = get_fps_from_presentmon()
        if fps_value:
            fps = fps_value
        last_fps_update_time = current_time

    screen.fill((0, 0, 0))  # Transparent background (black colorkey)

    # CPU Usage
    cpu_usage = psutil.cpu_percent()
    cpu_text = font.render(f"CPU: {cpu_usage:.2f}%", True, (255, 255, 255))
    screen.blit(cpu_text, (20, 20))

    # RAM Usage
    ram_usage = psutil.virtual_memory().percent
    total_ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
    ram_text = font.render(f"RAM: {ram_usage:.2f}% / {total_ram:.2f}GB", True, (255, 255, 255))
    screen.blit(ram_text, (20, 50))

    # GPU Usage & Name (if GPUtil is available)
    if GPUtil:
        try:
            gpu = GPUtil.getGPUs()[0]  # Get first GPU
            gpu_name = gpu.name  # Get GPU name
            gpu_usage = gpu.load * 100  # Get GPU usage
            gpu_memory = gpu.memoryUsed  # Get GPU memory used
            gpu_max_memory = gpu.memoryTotal / 1024  # Max GPU memory in GB (convert from MB)

            # Detect GPU type (NVIDIA, Intel, or AMD)
            if "NVIDIA" in gpu_name:
                gpu_color = (0, 255, 0)  # Green for NVIDIA
            elif "Intel" in gpu_name:
                gpu_color = (0, 0, 255)  # Blue for Intel
            elif "AMD" in gpu_name:
                gpu_color = (255, 0, 0)  # Red for AMD
            else:
                gpu_color = (255, 255, 255)  # White if no match

            # GPU Text including max GPU memory in GB
            gpu_text = f"GPU: {gpu_usage:.2f}% ({gpu_name}) - {gpu_memory}MB / {gpu_max_memory:.2f}GB"
        except Exception:
            gpu_text = "GPU: Error"
            gpu_color = (255, 255, 255)  # Default to white if error
    else:
        gpu_text = "GPU: N/A"  # Show 'N/A' if GPUtil is missing
        gpu_color = (255, 255, 255)  # Default to white

    # Wrap text to fit within the width of the window
    wrapped_gpu_text = wrap_text(gpu_text, WIDTH - 40)  # 40 for padding from edges
    y_offset = 80  # Starting Y position for GPU info

    for line in wrapped_gpu_text:
        gpu_line = font.render(line, True, gpu_color)  # Use the detected GPU color
        screen.blit(gpu_line, (20, y_offset))
        y_offset += 20  # Adjust for next line

    # Display FPS once every second
    if fps:
        fps_text = font.render(f"FPS: {fps}", True, (255, 255, 255))
        screen.blit(fps_text, (20, y_offset))

    pygame.display.update()
    clock.tick(60)  # Limit to 60 FPS