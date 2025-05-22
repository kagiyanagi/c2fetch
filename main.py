from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
from rich.align import Align
import os
import psutil
import time
import argparse

console = Console()  # output console for rich

# Sensor keys: try common CPU sensors in order
try_keys = ['coretemp', 'k10temp', 'amdgpu', 'acpitz']

def create_gif_art(color = "magenta"):
    return Text("""
  (\_/)
 ( •_•)
/ >❤ ​  CPU Temp Monitor
""", style=f"bold {color}")

def temp_style(temp):
    if temp >= 80:
        return "bold red"
    elif temp >= 65:
        return "yellow"
    return "white"

def locate_temp(gif_art):
    temps_dict = psutil.sensors_temperatures()
    for key in try_keys:
        if key in temps_dict:
            temps = temps_dict[key]
            break
    else:
        return [Text("No temperature sensors found", style="bold red")]

    seen_labels = set()
    core_temp_list = [gif_art, Text("")]  # start with gif and a blank line for spacing
    for i, entry in enumerate(temps):
        label = entry.label or f"Core {i}"
        if label in seen_labels:
            continue
        seen_labels.add(label)
        temp = int(entry.current)
        style = temp_style(temp)
        if i == 0:
            temp_text = Text.assemble(("Highest temp: ", ""), (f"{temp}°C", style))
        else:
            temp_text = Text.assemble((f"{label}: ", ""), (f"{temp}°C", style))
        core_temp_list.append(temp_text)
    return core_temp_list

# live view updates every second, showing centered temps
def main():
    parser = argparse.ArgumentParser(description="CPU Temperature Monitor")
    parser.add_argument("--color", default="magenta", help="Set the color of the ASCII art")
    args = parser.parse_args()

    gif_art = create_gif_art(args.color)

    try:
        with Live(console=console, refresh_per_second=1, screen=True) as live:
            while True:
                lines = locate_temp(gif_art)
                w, h = console.size  # current terminal dimensions
                view = Align(Group(*lines), align="center", vertical="middle", width=w, height=h)
                live.update(view)
                time.sleep(1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
