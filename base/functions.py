import psutil


class CPU(object):
    _func_name = "CPU"

    def info(self):
        _info = {}
        _info["cpu_count"] = psutil.cpu_count()
        _info["logical_cpu_count"] = psutil.cpu_count(logical=False)
        _info["cpu_percent"] = psutil.cpu_percent(interval=0.5, percpu=True)
        return self._func_name, _info


class Disk(object):
    _func_name = "DISK"

    def info(self):
        _info = []
        disks = psutil.disk_partitions()
        for disk in disks:
            if disk.fstype=='NTFS':
                disk_info = {}
                disk_info["device"] = disk.device
                disk_info["usage_percent"] = psutil.disk_usage(disk.device).percent
                _info.append(disk_info)
        return self._func_name, _info


class Memory(object):
    _func_name = "MEMORY"

    def info(self):
        _info = psutil.virtual_memory().percent
        return self._func_name, _info

