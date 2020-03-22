#!/usr/bin/python
import sys
import socket
import telnetlib
import time
from struct import pack


def recvuntil(sock, txt):
    d = ""
    while d.find(txt) == -1:
        try:
            dnow = sock.recv(1)
            if len(dnow) == 0:
                print("-=(warning)=- recvuntil() failed at recv")
                print("Last received data:")
                print(d)
                return False
        except socket.error as msg:
            print("-=(warning)=- recvuntil() failed at recv")
            print("Last received data:")
            print(d)
            return False
        d += dnow
    return d


def recvall(sock, n):
    d = ""
    while len(d) != n:
        try:
            dnow = sock.recv(n - len(d))
            if len(dnow) == 0:
                print("-=(warning)=- recvuntil() failed at recv")
                print("Last received data:")
                print(d)
                return False
        except socket.error as msg:
            print("-=(warning)=- recvuntil() failed at recv")
            print("Last received data:")
            print(d)
            return False
        d += dnow
    return d


# Proxy object for sockets.
class gsocket(object):
    def __init__(self, *p):
        self._sock = socket.socket(*p)

    def __getattr__(self, name):
        return getattr(self._sock, name)

    def recvall(self, n):
        return recvall(self._sock, n)

    def recvuntil(self, txt):
        return recvuntil(self._sock, txt)

    # Base for any of my ROPs.


def db(v):
    return pack("<B", v)


def dw(v):
    return pack("<H", v)


def dd(v):
    return pack("<I", v)


def dq(v):
    return pack("<Q", v)


def find_op(op, val1, val2):
    if op == "+":
        result = val1 + val2
    elif op == "-":
        result = val1 - val2
    elif op == "*":
        result = val1 * val2
    else:
        result = val1 / val2

    return str(result)


def go():
    global HOST
    global PORT
    s = gsocket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print("start")
    # Put your code here!
    value = s.recvall(441)
    new_val = value[-11:].replace("(", "").replace(")", "").replace(" ", "").replace("'", "").split(",")
    res = find_op(new_val[1],int(new_val[0]),int(new_val[2]))
    print(res)
    s.sendall(res+"\n")

    for i in range(0,1000):
        value = s.recvuntil(")")
        new_val = value.replace("\n>","").replace("(", "").replace(")", "").replace(" ", "").replace("'", "").split(",")
        res = find_op(new_val[1],int(new_val[0]),int(new_val[2]))
        s.sendall(res + "\n")
        print(i)
    # Interactive sockets.
    t = telnetlib.Telnet()
    t.sock = s
    t.interact()

    # Python console.
    # Note: you might need to modify ReceiverClass if you want
    #       to parse incoming packets.
    # ReceiverClass(s).start()
    # dct = locals()
    # for k in globals().keys():
    #  if k not in dct:
    #    dct[k] = globals()[k]
    # code.InteractiveConsole(dct).interact()

    s.close()


HOST = '192.168.1.66'
PORT = 1337
go()

