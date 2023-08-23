#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
from base.command import Command

info_list = {}
for arg in sys.argv[1:]:
    print(arg)
    cmd = Command(arg)
    func_name, info = cmd.info()
    info_list[func_name] = info
    print(info_list)
