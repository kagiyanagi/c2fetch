from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
from rich.align import Align
import psutil

console = Console()  # output console for rich

def locate_temp():
    temps = psutil.sensors_temperatures().get('coretemp', [])  # may vary by CPU
    core_temp_list = []
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
