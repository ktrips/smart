#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess

from pixels import pixels

BUTTON = 17
#LED    = 16
hold_time=1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(LED, GPIO.OUT)

"""actions = ['arecord -t wav -f dat -d 5 rec.wav', #ボタン長押しで録音
           'sudo raspistill -o '+fdir+fname+'.jpg', #ワンプッシュで写真撮影
           'aplay rec.wav'] #ダブルプッシュで再生
for i in range(3):
      GPIO.output(LED, GPIO.HIGH)
      time.sleep(0.5)
      GPIO.output(LED, GPIO.LOW)
      time.sleep(0.5)"""

actions = ['python3 visiontrans.py --trans ja-JP', #ボタン長押しで顔、ラベル、ロゴ全部読み取り、日本語発話
           'python3 visiontrans.py --detect text --trans ja-JP', #ワンプッシュで文字読み取り、日本語翻訳発話
           'python3 visiontrans.py --detect face'] #ダブルプッシュで顔読み取り
pixcels.listen()
time.sleep(hold_time)
pixcels.off()

GPIO.add_event_detect(BUTTON,GPIO.FALLING)
while True:
     if GPIO.event_detected(BUTTON):
      GPIO.remove_event_detect(BUTTON)
      now = time.time()
      count = 0
      GPIO.add_event_detect(BUTTON,GPIO.RISING)
      while time.time() < now + hold_time:
        if GPIO.event_detected(BUTTON):
          count +=1
          time.sleep(.3) # debounce time

      print count
      if count == 0:
        #GPIO.output(LED, GPIO.HIGH)
        pixels.listen()
        time.sleep(hold_time)
        #GPIO.output(LED, GPIO.LOW)
        pixels.off()

      for i in range(count):
        time.sleep(0.5)
        #GPIO.output(LED, GPIO.HIGH)
        pixels.listemn()
        time.sleep(0.5)
        #GPIO.output(LED, GPIO.LOW)
        pixels.off()

      cmd = actions[count]
      print cmd
      if cmd:
        subprocess.call(actions[count], shell=True)

      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)
      pixels.off()
