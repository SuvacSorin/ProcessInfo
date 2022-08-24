import json
import subprocess
import sys
import time

import psutil

path_to_executable = None
interval = 0

if len(sys.argv) == 3:
    path_to_executable = sys.argv[1]
    interval = float(sys.argv[2])
else:
    print(f"Expected 3 arguments. Got {len(sys.argv)}.")
    sys.exit()

process = subprocess.Popen([path_to_executable])
ps = psutil.Process(process.pid)

while ps.is_running():
    with ps.oneshot():
        cpu_usage = ps.cpu_percent()
        memory_rss = ps.memory_info()[0]
        memory_vms = ps.memory_info()[1]
        file_descriptors = ps.num_fds()

        json_data = json.dumps({
            "cpu_usage": cpu_usage,
            "memory_consumption": {
                "memory_rss": memory_rss,
                "memory_vms": memory_vms
            },
            "file_descriptors": file_descriptors
        })
        with open('data.txt', 'a') as f:
            f.write(json_data + '\n')

        time.sleep(interval)
