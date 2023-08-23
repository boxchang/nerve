import psutil


class CPU(object):
    _func_name = "CPU"

    def info(self):
        _info = []
        _info.append(psutil.cpu_count())
        _info.append(psutil.cpu_count(logical=False))
        _info.append(psutil.cpu_percent(interval=0.5, percpu=True))
        return self._func_name, _info


class Disk(object):
    _func_name = "DISK"

    def info(self):
        _info = []
        disks = psutil.disk_partitions()
        for disk in disks:
            _info.append(psutil.disk_usage(disk.device))
        return self._func_name, _info


class Memory(object):
    _func_name = "MEMORY"

    def info(self):
        _info = []
        _info.append(psutil.virtual_memory())
        return self._func_name, _info

