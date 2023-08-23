from base.functions import Disk, Memory, CPU


class Command(object):
    func_list = {'/D': Disk, '/M': Memory, '/C': CPU}

    def __init__(self, arg):
        if not arg.find('=') > -1:
            self.process = self.func_list[arg]

    def info(self):
        return self.process().info()
