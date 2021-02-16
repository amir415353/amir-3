import time
import os
import subprocess

for a in range(0, 9999):
    os.system('pkill tor')
    proc = subprocess.Popen(["tor"])
    time.sleep(12)
    proc.terminate()
