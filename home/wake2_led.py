# -*- coding: utf-8 -*-

import snowboydecoder
import sys
import signal

import RPi.GPIO as GPIO

from light import Light
interrupted = False
LED=17
GPIO.setwarnings(False)

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("エラーです。モデル名を指定して下さい。")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)
    
led = Light(LED)
sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING),
             lambda: led.blink()] #snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]
print("ウェイクワードを発話して下さい。Ctrl+Cで終了します。")

# main loop
detector.start(detected_callback=callbacks, #led.blink, #snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
