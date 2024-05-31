import psutil

def main():
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_percent}%")
    if cpu_percent > 3:
        print("High CPU Usage detected. Listing processes with CPU usage above 0.1%:")
        for process in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            try:
                process_cpu_percent = process.info['cpu_percent']
                if process_cpu_percent > 0.1:
                    pid = process.info['pid']
                    name = process.info['name']
                    print(f"PID: {pid}, NAME: {name}, CPU Usage: {process_cpu_percent}%")
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    else:
        print("CPU usage is normal.")

if __name__ == "__main__":
    main()
