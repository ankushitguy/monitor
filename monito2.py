import os
import time
import psutil

def monitor_server():
    # Set the interval for checking the server stats (in seconds)
    interval = 60

    while True:
        # Check the storage usage
        storage = get_storage_usage()

        # Check the RAM usage
        ram = get_ram_usage()

        # Check the CPU usage
        cpu = get_cpu_usage()

        if storage > 90 or ram > 90 or cpu > 90:
            # One of the server stats is over 90%, send an alert email to the administrator
            send_alert_email(storage, ram, cpu)
        else:
            # The server stats are within acceptable limits, check again after the specified interval
            time.sleep(interval)

def get_storage_usage():
    # Set the path to the storage device
    storage_device = '/dev/sda1'

    # Get the filesystem stats for the storage device
    stats = os.statvfs(storage_device)

    # Get the total storage space (in bytes)
    total_storage = stats.f_frsize * stats.f_blocks

    # Get the used storage space (in bytes)
    used_storage = stats.f_frsize * (stats.f_blocks - stats.f_bfree)

    # Calculate the percentage of used storage space
    used_percent = (used_storage / total_storage) * 100

    # Return the percentage of used storage space
    return used_percent

def get_ram_usage():
    # Get the total RAM (in bytes)
    total_ram = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')

    # Get the used RAM (in bytes)
    with open('/proc/meminfo', 'r') as meminfo:
        lines = meminfo.readlines()
        for line in lines:
            if line.startswith('MemTotal:'):
                total_ram_str = line.split()[1]
                total_ram = int(total_ram_str) * 1024
            elif line.startswith('MemFree:'):
                free_ram_str = line.split()[1]
                free_ram = int(free_ram_str) * 1024
            elif line.startswith('Buffers:'):
                buffers_ram_str = line.split()[1]
                buffers_ram = int(buffers_ram_str) * 1024
            elif line.startswith('Cached:'):
                cached_ram_str = line.split()[1]
                cached_ram = int(cached_ram_str) * 1024

    used_ram = total_ram - free_ram - buffers_ram - cached_ram

    # Calculate the percentage of used RAM
    used_percent = (used_ram / total_ram) * 100

    # Return the percentage of used RAM
    return used_percent

def get_cpu_usage():
    loadavg = os.getloadavg()
    used_cpu = (loadavg[0] / os.cpu_count()) * 100
    return used_cpu

def send_alert_email(storage, ram, cpu):
    # Use the smtplib library to send an email alert to the administrator
    # Include the current storage, RAM, and CPU usage in the email body
    print(get_storage_usage())
    print(get_ram_usage())
    print(get_cpu_usage())


# Start the monitoring process
monitor_server()
