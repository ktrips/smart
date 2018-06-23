#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat

import os
import time
from datetime import datetime
import argparse
import re

from pixels import pixels

default_speech= 'en-US'
default_trans = 'ja-JP'
aiy_lang = ['en-US', 'en-GB', 'de-DE', 'es-ES', 'fr-FR', 'it-IT']

import urllib.request, urllib.parse, urllib.error
DEVICE = 0
CARD   = 0
VOLUME = 50

from google.cloud import translate

def translate_text(text, trans_lang):
    if trans_lang == '':
        return text
    else:
      target_lang = trans_lang.split("-")[0]
      translate_client = translate.Client()
      result = translate_client.translate(text, target_language=target_lang)
      return result['translatedText']

def main():
    recognizer = aiy.cloudspeech.get_recognizer()
    recognizer.expect_phrase('turn off the light')
    recognizer.expect_phrase('turn on the light')
    recognizer.expect_phrase('blink')
    recognizer.expect_phrase('repeat after me')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    aiy.i18n.set_language_code(speech_lang)

    for i in range(3):
      pixels.wakeup()
      time.sleep(1)
      pixels.off()

    while True:
     print('Press the button and speak')
     pixels.wakeup()
     button.wait_for_press()

     while True:
        print('Listening...')
        
        bye_words    = ['goodbye', 'good bye', 'see you', 'bye bye']
        pixels.think()
        text = recognizer.recognize()
        if not text:
            print('Sorry but please say again in ' + speech_lang)
        else:
            pixels.listen()
            print('Speech: ' + text)
            trans_text = translate_text(text, trans_lang)
            trans_text = trans_text.replace("&#39;","")
            print('Trans: ' + trans_text)
            pixels.off()
            pixels.listen()
            if trans_lang in aiy_lang:
                aiy.audio.say(trans_text, trans_lang)
            elif trans_lang == "ja-JP":
                os.system('~/AIY-projects-python/src/aquestalkpi/AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, trans_text, CARD, DEVICE))
            else:
                print("No lang to say")

            if 'turn on the light' in text:
                led.set_state(aiy.voicehat.LED.ON)
            elif 'turn off the light' in text:
                led.set_state(aiy.voicehat.LED.OFF)
            elif 'blink' in text:
                led.set_state(aiy.voicehat.LED.BLINK)
            elif 'repeat after me' in text:
                to_repeat = text.replace('repeat after me', '', 1)
                aiy.audio.say(to_repeat)

            for b in bye_words:
              if text.find(b) > -1:
                keyw = "bye"
                break
            if text in bye_words:
                pixels.off()
                break
            time.sleep(0.2)
            pixels.off()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--speech', dest='speech_lang', type=str, default='', help='Base speech language')
    parser.add_argument('--trans', dest='trans_lang', type=str, default='', help='Language translated to ')
    args   = parser.parse_args()
    speech_lang= args.speech_lang if args.speech_lang else default_speech
    trans_lang = args.trans_lang if args.trans_lang else default_trans
    main()
