# -*- coding: utf-8 -*-
import socket
from io import StringIO
import re
import subprocess

import os
import time
import RPi.GPIO as GPIO

from light import Light
interrupted = False
GPIO.setwarnings(False)

aquest_dir = "/home/pi/smart/aquestalkpi/"

def led_blink(color, count):
        if color == "red":
            led = Light(17)
        elif color == "green":
            led = Light(18)
        else:
            led = Light(17)
        for i in range(count):
            led.blink()
            time.sleep(1)
"""
try:
    unicode # python2
    def u(str): return str.decode('utf-8')
    pass
except: # python3
    def u(str): return str
    pass
"""

host = '127.0.0.1'
port = 10500
bufsize = 1024

buff = StringIO(u'')
pattern = r'WHYPO WORD=\"(.*)\" CLASSID'
aquest_word = aquest_dir + 'AquesTalkPi "声でリモコン操作しましょう！"' + ' | aplay'
os.system(aquest_word)
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        data = sock.recv(bufsize)
        buff.write(data.decode('utf-8'))
        data = buff.getvalue().replace('> ', '>\n ')
        if '\n' in data:
            lines = data.splitlines()
            for i in range(len(lines)-1):
                if lines[i] != '.':
                    #print(lines[i])
                    m = re.search(pattern, lines[i])
                    if m:
                        word = m.group(1)
                        if u'テレビオン' in word:
                            command = 'on'
                        elif u'音量ダウン' in word:
                            command = 'down'
                        elif u'音量アップ' in word:
                            command = 'up'

                        print(word)
                        if command:
                          args = ['irsend', '-#', '1', 'SEND_ONCE', 'remotetv', command]
                          try:
                                led_blink("red",1)
                                subprocess.Popen(args)
                                led_blink("green",3)
                          except OSError:
                                print('command not found.')

            buff.close()
            buff = StringIO(u'')
            if lines[len(lines)-1] != '.':
                buff.write(lines[len(lines)-1])

except socket.error:
    print('socket error')
except KeyboardInterrupt:
    pass

sock.close()
