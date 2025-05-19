from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
from rich.align import Align
import psutil

console = Console()
total_cpu_cores = psutil.cpu_count(logical=False)

def locate_temp():
    temps = psutil.sensors_temperatures().get('coretemp', [])[1:]
    core_temp_list = []
    for i, entry in enumerate(temps):
        core_temp_list.append(Text(f"Your Core {i} temp is: {int(entry.current)}°C"))
    return core_temp_list

with Live(console=console, refresh_per_second=1, screen=True) as live:
    while True:
        lines = locate_temp()
        term_width, term_height = console.size
        aligned = Align(
            Group(*lines),
            align="center",
            vertical="middle",
            width=term_width,
            height=term_height
            )
        live.update(aligned)