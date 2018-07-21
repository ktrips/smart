#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import time
import RPi.GPIO as GPIO
import subprocess

BUTTON = 17
hold_time=1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTON,GPIO.FALLING)

def main(speech=”en-US”, trans="ja-JP"):
actions = ['python3 visiontrans.py --detect text --trans {}'.format(trans), #ボタン長押しで、写真撮影、外国語読み取り、変換
           'python3 cloudspeech_trans.py –speech {} --trans {}'.format(speech, trans), #ワンプッシュで外国語聞き取り、変換
           'python3 cloudspeech_trans.py –speech {} --trans {}'.format(trans, speech)] #ダブルプッシュで発話日本語などを外国語変換
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

if __name__ == '__main__':
   parser = argparse.ArgumentParser()
    parser.add_argument('--speech', nargs='?', default='en-US', help='If null speech is en-US')
    parser.add_argument('--trans', nargs='?', default='ja-JP', help='If null trans to ja-JP')
    args = parser.parse_args()
    main(args.speech, args.trans)
