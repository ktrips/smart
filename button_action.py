#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import RPi.GPIO as GPIO
import subprocess

BUTTON = 17
hold_time=1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

actions = ['raspistill -o image.jpg', #ボタン長押しで、写真撮影
           'arecord -t wav -f dat -d 5 rec.wav', #ワンプッシュで音声5秒聞き取り
           'aplay rec.wav'] #ダブルプッシュで聞き取り音声の出力

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
      cmd = actions[count]
      print cmd
      if cmd:
        subprocess.call(actions[count], shell=True)

      GPIO.remove_event_detect(BUTTON)
      GPIO.add_event_detect(BUTTON, GPIO.FALLING)
