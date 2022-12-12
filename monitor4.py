import psutil

# get system-wide information
info = psutil.info()

# print current storage usage
print('Storage:', info.memory_percent, '%')

# print current RAM usage
print('RAM:', info.memory_percent, '%')

# print current CPU usage
print('CPU:', info.cpu_percent, '%')
