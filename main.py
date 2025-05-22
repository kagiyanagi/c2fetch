from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
from rich.align import Align
from rich.panel import Panel
from rich.markdown import Markdown
from rich import box
import psutil

console = Console()  # output console for rich

# Sensor keys: try common CPU sensors in order
try_keys = ['coretemp', 'k10temp', 'amdgpu', 'acpitz']

# Add your ASCII or GIF
gif_art = Text("""
       (\_/)
      ( •_•)
     / >❤ ​  CPU Temp Monitor
""", style="bold magenta")

def locate_temp():
    temps_dict = psutil.sensors_temperatures()
    for key in try_keys:
        if key in temps_dict:
            temps = temps_dict[key]
            break
    else:
        return [Text("No temperature sensors found", style="bold red")]

    core_temp_list = [gif_art, Text("")]  # start with gif and a blank line for spacing
    for i, entry in enumerate(temps):
        if i == 0:
            # first entry is treated as overall highest
            core_temp_list.append(Text(f"Highest temp: {int(entry.current)}°C", style="bold"))
        else:
            # individual core temperatures
            core_temp_list.append(Text(f"Core {i-1}: {int(entry.current)}°C"))
    return core_temp_list

# live view updates every second, showing centered temps
def main():
    with Live(console=console, refresh_per_second=1, screen=True) as live:
        while True:
            lines = locate_temp()
            w, h = console.size  # current terminal dimensions
            view = Align(Group(*lines), align="center", vertical="middle", width=w, height=h)
            live.update(view)

if __name__ == "__main__":
    main()