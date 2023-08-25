#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket
from base.command import Command

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    indata, addr = s.recvfrom(1024)
    print('recvfrom ' + str(addr) + ': ' + indata.decode())
    info_list = {}
    args = str(indata.decode()).split(' ')
    for arg in args:
        cmd = Command(arg)
        func_name, info = cmd.info()
        info_list[func_name] = info

    outdata = str(info_list)
    s.sendto(outdata.encode(), addr)
s.close()