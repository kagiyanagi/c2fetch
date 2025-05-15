import time
import subprocess

def core_temp(core):
    pattern = "\'\\d+\\.\\d+°C\'"
    cmd = f"sensors | grep \'Core {core}\' | grep -oP {pattern} | head -n 1"
    return subprocess.getoutput(cmd)

i = 1
a = 0

while a <= i :
    print(f'\r{core_temp(0)}', end="", flush=True)
    time.sleep(1)