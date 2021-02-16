import time
import os
import subprocess
import sys
for a in range(0, 9999):
    os.system('pkill tor')
    subprocess.Popen(["tor"])
    time.sleep(12)
    sys.exit(0)
