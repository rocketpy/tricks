# psutil  - Cross-platform lib for process and system monitoring in Python.

# https://github.com/giampaolo/psutil
# https://pypi.org/project/psutil/


# pip install psutil


import psutil

psutil.cpu_times()
scputimes(user=3961.46, nice=169.729, system=2150.659, idle=16900.540, iowait=629.59, irq=0.0, softirq=19.42, steal=0.0, guest=0, nice=0.0)

for x in range(3):
    psutil.cpu_percent(interval=1)
