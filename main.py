from rich.live import Live
from rich.text import Text
from rich.console import Console, Group
from rich.align import Align
import psutil

# Create a Console instance for rich output
console = Console()

# Get the number of physical CPU cores (not counting hyper‑threaded logical cores)
total_cpu_cores = psutil.cpu_count(logical=False)

def locate_temp():
    """
    Read CPU temperature sensors and build a list of Text objects:
    - The first entry shows the highest temperature.
    - Subsequent entries show each individual core's temperature.
    """
    # Retrieve all temperature entries under the 'coretemp' sensor (Intel CPUs)
    temps = psutil.sensors_temperatures().get('coretemp', [])
    core_temp_list = []

    # Loop through each sensor reading
    for i, entry in enumerate(temps):
        # The first entry: label it as the highest temperature
        if i == 0:
            core_temp_list.append(
                Text(f"Highest temperature : {int(entry.current)}°C", style="bold")
            )
        # Further entries: individual core temps, index shifted by -1 for readability
        else:
            core_temp_list.append(
                Text(f"Your Core{i-1}'s temp is: {int(entry.current)}°C")
            )

    return core_temp_list

# Live display context: refresh the console output once per second
with Live(console=console, refresh_per_second=1, screen=True) as live:
    while True:
        # Fetch updated temperature lines
        lines = locate_temp()

        # Determine current terminal size to center the output
        term_width, term_height = console.size

        # Group the Text lines and center them both horizontally and vertically
        aligned = Align(
            Group(*lines),
            align="center",
            vertical="middle",
            width=term_width,
            height=term_height
        )

        # Update the live view with the newly aligned Group
        live.update(aligned)
