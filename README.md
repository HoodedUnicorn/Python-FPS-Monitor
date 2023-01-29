[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/HoodedUnicorn/Python-FPS-Monitor?color=gree&label=Github)](https://github.com/HoodedUnicorn/Python-FPS-Monitor/releases)
[![npm (scoped)](https://img.shields.io/npm/v/@hoodedunicorn/python-fps-monitor?color=red)](https://www.npmjs.com/package/@hoodedunicorn/python-fps-monitor)


# Python FPS and System Monitor :video_game:

This is a Python script that uses the Pygame library to display the current FPS (frames per second) and system information such as GPU usage and CPU usage in a resizable window.
<br>
<h2>Dependencies :bookmark_tabs: </h2>

* Pygame
* Psutil
* Gpustat
* cpuinfo
* sys

<h2>Installation :computer: </h2>


<h3>Install via NPM packages :factory:</h3>

 * Install the dependencies by running `pip install pygame psutil gpustat cpuinfo` in the command line. <br>
 * Install package via NPM package manager `npm i @hoodedunicorn/python-fps-monitor` <br>
 * Run the script using `python FPS-Monitor.py`


<h2>Limitations :warning: </h2>

This script is only compatible with NVidia GPUs. It will not work with other types of GPUs such as AMD or Intel. Additionally, it will only display information for the first GPU it detects. If you have multiple GPUs installed, you will need to modify the script to display information for all of them.


<h2>Features :space_invader: </h2>
This code is a Python script that uses Pygame, sys, psutil, gpustat, and cpuinfo libraries to display system information in a graphical interface. The code initializes the Pygame library, sets the height and width of the window, and sets up a font for text display. <br>
<br>
The script has several functions that are responsible for getting specific system information and returning text in the form of a Pygame surface. The fpsrun() function returns the current FPS value as text. <br>
<br> The get_cpu_usage() function returns the CPU usage percentage, along with the CPU name, in text format with different colors depending on whether the CPU is from AMD, Intel, or any other brand. <br>
<br> The get_gpu_usage() and get_gpu_name() functions return the GPU usage percentage and name in text format with green color. The get_ram_info() and get_ram_usage() functions return the total RAM and the RAM usage percentage in text format with orange color.

<br> In the main loop, the script listens for Pygame quit events, updates the screen with the system information, and updates the display 60 times per second. The script displays the FPS value, CPU name, CPU usage, GPU name, GPU usage, total RAM, and RAM usage on the screen.

<h2>Roadmap :calendar: (subject to change)</h2>

:heavy_check_mark: = Implemented
:recycle: = In testing
:memo: = Working on it
:x: = Not yet available

| Feature | :heavy_check_mark:/:recycle:/:memo:/:x:|
| ---- | ---- | 
| RAM stats & usage | :heavy_check_mark: |
| CPU stats color AMD or Intel | :recycle: |  
| CPU temps and GPU Memory usage | :memo: |
| Accessible for all GPU's | :x: |
| Be an Overlay | :x: |


<h2>Conclusion :rocket:</h2>

This script is a useful tool for monitoring the performance of your system while running resource-intensive applications such as games or video editing software. It is easy to install and customize, making it a valuable addition to any developer or gamer's toolbox.


<h2>Versions :pizza:</h2>

To see versions [click me](Versions.md), 

to download a previous release [click here](releases)

<h2>Bugs :bug:</h2>

| Issue | Resolved? |
| ---- | ---- |
| Window is very slow to change position | :x: |
| FPS is not shown correctly | :x: |
