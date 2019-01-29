-*- coding: utf-8 -*-
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

aquest_dir   = "/home/pi/smart/aquestalkpi/AquesTalkPi "
bme_command  = "/home/pi/smart/snowboy/bme.py"
ifttt_command= ""

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

host = '127.0.0.1'
port = 10500
bufsize = 1024

buff = StringIO(u'')
pattern = r'WHYPO WORD=\"(.*)\" CLASSID'

os.system(aquest_dir + ' "御用は何でしょうか？" | aplay')

#def main():
p = subprocess.Popen(["bash julius_greeting.sh"], stdout=subprocess.PIPE, shell=True)
pid = p.stdout.read() # juliusのプロセスIDを取得
print('Julius runs with '+str(pid))
time.sleep(1)

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
                       device = "tv"
                       command= "tvon"

                       if u'おはよう' in word:
                           msg = 'おはようございます！今日もいい朝ですね！'
                       elif u'いってきます' in word:
                           msg = 'いってらっしゃい！今日の天気は晴れですよ！'
                       elif u'ただいま' in word:
                           msg = 'おかえりなさい！おつかれさまでした！'
                       elif u'おやすみ' in word:
                           msg = 'おやすみなさい！良い夢を！'
                       elif u'音量アップ' in word:
                           msg = 'また話しかけてね！'
                           print(msg)
                           p.kill()
                           subprocess.call(["kill " + pid], shell=True) # juliusのプロセスを終了
                           time.sleep(1)
                           sock.close()
                           break
                       else:
                           msg = ""

                       print(word)
                       if msg:
                         args = ['irsend', '-#', '1', 'SEND_ONCE', device, command]
                         try:
                               led_blink("red",1)
                               print(msg)
                               os.system(aquest_dir + msg + ' | aplay')
                               os.system('python ' + bme_command)
                               os.system('raspistill -o image.jpg')
                               cam_msg = "今日のスナップを保存しました！"
                               print(cam_msg)
                               subprocess.Popen(args)
                               print(device, command)
                               led_blink("green",3)
                         except OSError:
                               print('command not found.')
                       else:
                         print('No word detected')

           buff.close()
           buff = StringIO(u'')
           if lines[len(lines)-1] != '.':
               buff.write(lines[len(lines)-1])

except socket.error:
   print('socket error')
except KeyboardInterrupt:
   pass

p.kill()
subprocess.call(["kill " + pid], shell=True) # juliusのプロセスを終了
sock.close()

#if __name__ == "__main__":
#  main()
