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

DEVICE = 0
CARD   = 0
VOLUME = 50

aiy_lang      = ['en-US', 'en-GB', 'de-DE', 'es-ES', 'fr-FR', 'it-IT']
default_speech= "ja-JP"

def make_minutes(convs):
        conv_title= "打ち合わせ"
        conv_cont = ""

        minutes_temp={
             "title":"議題：",
             "date":"日付：",
             "written":"作成者：",
             "contents":"議事内容："
        }

        dateStr = datetime.now().strftime('%Y-%m-%d')
        for con in convs:
            convTimeStr = con["convDateTime"].strftime('%H:%M:%S')
            if con["keyw"] in ["minutes"]:
                conv_title = con["convt"]
            conv_cont += '(' + str(con["number"]) +') ' + con["convt"] + ' (' + convTimeStr + ')\n'
        minutes = minutes_temp["title"] + conv_title + '\n'
        minutes+= minutes_temp["date"] + dateStr + '\n'
        minutes+= minutes_temp["written"] + mail + '\n'
        minutes+= minutes_temp["contents"] + '\n'
        minutes+= conv_cont #+ '\n'
        subject = conv_title + '(' + dateStr + ')'
        print(subject + '\n\n' + minutes)
        return subject, minutes

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

    import RPi.GPIO as GPIO
    BUTTON = 16
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON, GPIO.IN)

    i = 0
    convs=[]

    while True:
      print('Press the button and speak')

      state=GPIO.input(BUTTON)
      if state:
          print("Not started!")
      else:
          print("Started!")

      #button.wait_for_press()
      #while True:

          print('Listening...')
          text = recognizer.recognize()
          if not text:
            print('Sorry but please say again in ' + speech_lang)
          else:

            convDateTime= datetime.now()
            convDateStr = convDateTime.strftime('%Y-%m-%d %H:%M:%S')
            i += 1
            print(str(i) + text + convDateStr)
            bye_words    = ['終わりです', '終了', 'おわり', 'さようなら', 'さよなら', 'バイバイ']
            minutes_words= ['議事録', '打合せ', 'ミーティング']
            keyw = ""
            text.lower()
            for m in minutes_words:
              if text.find(m) > -1:
                keyw = "minutes"
                break
            conv = {"number": i,
                "convDateTime": convDateTime,
                "convt": text,
                "keyw": keyw}
            convs.append(conv)
            print(convs)

            if repeat != "no":
              if speech_lang in aiy_lang:
                aiy.audio.say(text, speech_lang)
              elif speech_lang == "ja-JP":
                os.system('~/AIY-projects-python/src/aquestalkpi/AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, text, CARD, DEVICE))
              else:
                aiy.audio.say("No "+speech_lang+" to speak!", "en-US")

            if text in bye_words:
              subject, minutes = make_minutes(convs)
              if mail:
                os.system('echo "' + minutes + '" | mail -s "' + subject + '" ' + mail)
              break
            time.sleep(0.2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--speech', dest='speech_lang', type=str, default='', help='Base speech language')
    parser.add_argument('--repeat', dest='repeat', type=str, default='speech', help='Repeat the speech or not')
    parser.add_argument('--mail', dest='mail', type=str, default='', help='send to email')
    args   = parser.parse_args()
    speech_lang= args.speech_lang if args.speech_lang else default_speech
    repeat = args.repeat if args.repeat else "speech"
    mail   = args.mail if args.mail else ""
    main()
