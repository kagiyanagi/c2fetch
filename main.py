from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
import psutil

console = Console()
total_cpu_cores = psutil.cpu_count(logical=False)

def locate_temp():
    temps = psutil.sensors_temperatures().get('coretemp', [])
    core_temp_list = []
    for i in range(0, total_cpu_cores+1):
        core_temp = int(temps[i].current)
        core_temp_list.append(Text(f"Your Core{i} temp is : {core_temp}°C"))
    return core_temp_list

with Live(console=console, refresh_per_second=1) as live:
    while True:
        lines = locate_temp()
        live.update(Group(*lines))