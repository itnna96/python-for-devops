

import subprocess,os,re
from prometheus_client import Gauge,start_http_server
from time import sleep

CPU_PERCENT = Gauge(
    'cpu_percent',
    'CPU Percentage',
    []
)
#Load Avg: 4.40,3.55,3.49
#          1min,5min,15mins
#top Get CPU Usage by load avg
def cpu_load():
    host = os.environ.get('HOST')
    load_avg = os.getloadavg()[1]
    cpu_count = os.cpu_count()
    cpu_percentage = round((load_avg / cpu_count) * 100,2)
    CPU_PERCENT.set(cpu_percentage)
    # print(f"CPU percent: {cpu_percentage}%")

if __name__ == '__main__':
    start_http_server(8080)
    while True:
        cpu_load()
        sleep(5)
#sysctl hw.memsize 
#Virtual memory
# vm_stats = subprocess.run(['vm_stat'],capture_output=True,text=True).stdout
# vm_free = int(re.search(r'Pages\sfree:\s+(\d+)\.',vm_stats).group(1)) * 4096 #real free
# vm_active = int(re.search(r'Pages\sactive:\s+(\d+)\.',vm_stats).group(1)) * 4096
# vm_inactive = int(re.search(r'Pages\sinactive:\s+(\d+)\.',vm_stats).group(1)) * 4096
# vm_wired = int(re.search(r'Pages\swired:\s+(\d+)\.',vm_stats).group(1)) * 4096

# memory_total = int(subprocess.run(['sysctl','hw.memsize'],capture_output=True,text=True).stdout.split('\n')[0].split()[1])
# memory_percentage = round ((vm_active + vm_inactive + vm_wired ) / memory_total *100,2)
# mem_free = round(vm_free/memory_total*100,2)
# print(f"Memory percent:{memory_percentage}%. Memory free: {mem_free}%.")

# Disk Size
# disks = subprocess.run(['df','-h','/'],capture_output=True,text=True).stdout.split('\n')[1]
# avail_disk = disks.split()[3]
# total_disk = disks.split()[1]
# print (f"Disk total: {total_disk}. Disk usage: {avail_disk}.")

# # Disk IO
# # example: 500MB/s
# disks_io = subprocess.run(['iostat'],capture_output=True,text=True).stdout.split('\n')[3].split()[0]
# print(f"Disk IO: {disks_io} MB/s.")

# # Network
# networks = subprocess.run(['ping','-i 1','-c 5','google.com'],capture_output=True,text=True).stdout.split('\n')[-2]
# if '100.0% packet loss' in networks:
#     print('Cannot connect to internet.')
# else:
#     latency_min, latency_avg, latency_max,_ = networks.split()[3].split('/')
# print(f"Network Latency: {latency_avg} ms.")

#Có thể dùng cron để chạy check liên tục hoặc gửi mail về cho mình nếu hệ thống quá tải