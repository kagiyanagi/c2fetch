import time
import os
import psutil

total_core = os.cpu_count() #total cpu core count

#get a cpu core temp with lm_sensors
        
def locate_temp():
    temps = psutil.sensors_temperatures()
    cpu_pkg = temps['coretemp'][0].current
    return int(cpu_pkg)

terminal_size = os.get_terminal_size() # get term size

for i in range(0, 999999999):
    os.system('cls' if os.name == 'nt' else 'clear') #clear the terminal

    cpu_temp = locate_temp()

    base_str = f'Your CPU\'s temp is {cpu_temp}°C'
    print(base_str.center(int(terminal_size.columns),), end="")

    time.sleep(1)