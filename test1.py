import psutil
x = psutil.disk_usage('C:\\')
print(psutil.disk_partitions())             # 所有硬碟資訊
print(psutil.disk_usage('C:\\'))  # 指定硬碟資訊
