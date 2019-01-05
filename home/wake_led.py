# -*- coding: utf-8 -*-

import snowboydecoder
import sys
import signal

interrupted = False

from light import Light
interrupted = False
LED=17

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) == 1:
    print("エラーです。モデル名を指定して下さい。")
    sys.exit(-1)

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
print("ウェイクワードを発話して下さい。Ctrl+Cで終了します。")

# main loop
led = Light(LED)
detector.start(detected_callback=led.blink, #snowboydecoder.play_audio_file,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

