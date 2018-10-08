
#! /usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, os, sys, re
import cv2
import json
import time
from datetime import datetime
#import urllib2
import urllib.request, urllib.error
import urllib
import urllib.parse
import dateutil.parser
#from poster.encode import multipart_encode
#from poster.streaminghttp import register_openers
import argparse
import RPi.GPIO as GPIO
import requests
#import blinkt
import colorsys

import getTensor

BUTTON = 20
LED    = 16
DEVICE = 0
CARD   = 0
VOLUME = 50

RECDEV = 0
RECCD  = 1

lang_def   = 'jpn'
speaker_def= 'hikari' #'haruka' 'takeru' 'santa' 'bear'
mail_def   = ''

rec_lang   = 'ja'
rec_time   = 4
rec_path   = 'tmp.wav'

image_path = '/home/pi/tensor/webapps/image/'
speech_path= '/home/pi/tensor/webapps/speech.wav' #web/cgi-bin/speech.wav'
accuracy   = 70
hold_time  = 1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

models = {1: {"name": "ラズパイ受賞率分析",
            #"url": "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/concept/classify/?APIKEY=",
            "model": "_winner"
            },
        2: {"name": "アイオーティー診断",
            #"url": "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/objectDetection/detect/?APIKEY=",
            "model":"_aiotlt"
            },
        3: {"name": "ヨシダケ率診断",
            #"url": "https://api.apigw.smt.docomo.ne.jp/characterRecognition/v1/scene",
            "model":"_yoshidake"
            }
        }

docomo_key= '307745313362694e4e6f41786a766668674a45536461713445566b4e6e2e4769367959723846394f395143'
#'555248645546724838684e716c65775845386859535257646e52716b3650362e384f744c455a4b57544f44'
#URL_SPEECH= 'https://api.apigw.smt.docomo.ne.jp/voiceText/v1/textToSpeech?APIKEY='
URL_RECOG = 'https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY='

"""def blinkt_rgb(count, cl):
    blinkt.clear()
    if count == 0:
        blinkt.set_all(cl, cl, cl) #White
    elif count == 1:
        blinkt.set_all(cl, cl, 0) #Yellow
    elif count == 2:
        blinkt.set_all(0, cl, 0) #Green
    elif count == 3:
        blinkt.set_all(0, 0, cl) #Blue
    elif count == 9:
        blinkt.set_all(cl, 0, cl)
    else:
        blinkt.set_all(0, 0, 0)
    blinkt.show()
    time.sleep(.5)"""

"""def blinkt_pulse(r,g,b):
    for i in range(blinkt.NUM_PIXELS):
        blinkt.clear()
        blinkt.set_pixel(i, r, g, b)
        blinkt.show()
        time.sleep(.2)

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.05)"""


GPIO.output(LED, GPIO.HIGH)

"""
blinkt_pulse(255, 0, 0)
time.sleep(.5)
blinkt_pulse(0, 255, 0)
time.sleep(.5)
blinkt_pulse(0, 0, 255)
blinkt.clear()
blinkt.show()"""

GPIO.output(LED, GPIO.LOW)


def camera():
    GPIO.output(LED, GPIO.HIGH)
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = image_path + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
        os.mkdir(dir_path)
    except OSError:
        print('Date dir already exists')
    c1 = 'fswebcam -r 640x480 --no-banner '
    os.system(c1 + fname)
    GPIO.output(LED, GPIO.LOW)
    return fname

"""def makeWordList(result):
    word_list= []
    count    = int(result['words']['@count'])
    for i in range(count):
        word = result['words']['word'][i]
        word_list.append(word)
    return word_list"""


"""def getWordList(img_id):
    register_openers()
    print img_id
    url = models[3]['url'] + '/' + img_id + '?APIKEY=' + docomo_key

    request = urllib2.Request(url)
    recog_result = {}
    for i in range(5):
        response = urllib2.urlopen(request)
        res_dat  = response.read()

        recog_result = json.loads(res_dat)
        status = recog_result['job']['@status']
        print status
        if status == 'success':
            word_list = makeWordList(recog_result)
            print json.dumps(recog_result, indent=2)
            return word_list
        elif status == 'failure':
            return None
        time.sleep(3)"""

def talk(message):
    os.system('~/tensor/aquestalkpi/AquesTalkPi -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, message, CARD, DEVICE))


def recognize(rec_time=4):
    GPIO.output(LED, GPIO.HIGH)
    a1 = 'sudo arecord -r 16000 -f S16_LE -d ' + str(rec_time) + ' -D plughw:{},{} '.format(RECCD, RECDEV) + rec_path
    subprocess.call(a1, shell=True)
    GPIO.output(LED, GPIO.LOW)
    url = URL_RECOG + docomo_key
    files = {"a": open(rec_path, 'rb'), "v": "on"}
    r = requests.post(url, files=files)
    rec = r.json()['text']
    return rec


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--lang',   dest='lang', type=str, default='', help='language name')
    parser.add_argument('--image',dest='image', type=str, default='', help='image file name')
    parser.add_argument('--mail',   dest='mail', type=str, default='', help='send to email')

    args   = parser.parse_args()
    lang   = args.lang if args.lang else lang_def
    image  = args.image if args.image else ''
    tomail = args.mail if args.mail else ''
    print(lang, image, tomail)

    GPIO.add_event_detect(BUTTON,GPIO.FALLING)
    while True:
        print("Press 1 " + models[1]['name'] + ", 2 " + models[2]['name'] + ", 3 " + models[3]['name'] + " times!")
        if GPIO.event_detected(BUTTON):
