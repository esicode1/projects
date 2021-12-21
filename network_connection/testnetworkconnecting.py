#!/usr/bin/env python3

__author__ = 'ehsangb180@gmail.com'


'''

    in windows os replace 'clear' to 'cls' in cmd.

'''
import os
import sys
import time
import socket
import itertools
import threading

done = False

def animate():
    os.system('clear')
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rConnecting ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect(("8.8.8.8", 53))
        os.system('clear')
        sys.stdout.write('\rConnected!  :)  \n')

    except socket.error:
        sys.stdout.write('\rDisconnected!  :(    \n')

    finally:
        time.sleep(2)
        os.system('clear')

t = threading.Thread(target=animate)
t.start()

time.sleep(3)
done = True
