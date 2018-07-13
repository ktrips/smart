#! /usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, os, sys, re
import cv2
import json
import time
from datetime import datetime
import urllib2
import urllib
import dateutil.parser
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import argparse
import RPi.GPIO as GPIO
import requests
import blinkt
import colorsys

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

rec_time   = 4
rec_path   = 'tmp.wav'
flash      = 0

speech_path= '/home/pi/web/cgi-bin/speech.wav'
accuracy   = 70
hold_time  = 1.2

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)

models = {1: {"name": "カテゴリ認識",
            "url": "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/concept/classify/?APIKEY=",
            "model":{'scene': u"['風景','シーン','背景','写り']",
                    'fashion_style': u"['ファッション','スタイル']",
                    'fashion_color': u"['カラー','色']",
                    'food': u"['料理','食べ物','食事','フード']",
                    'flower': u"['花','フラワー','植物']",
                    'kinoko': u"['キノコ','きのこ','マッシュルーム']"}
            },
        2: {"name": "物体認識",
            "url": "https://api.apigw.smt.docomo.ne.jp/imageRecognition/v1/objectDetection/detect/?APIKEY=",
            "model":{'currency': u"['お札','金','カネ','マネー','円']",
                    'bodyPart': u"['人','体','顔','自撮り','ボディ','部位','体形']"}
            },
        3: {"name": "文字認識",
            "url": "https://api.apigw.smt.docomo.ne.jp/characterRecognition/v1/scene",
            "model":{'word': u"['文字','言葉','読取','テキスト']"}
            }
        }

docomo_key= 'xxx'
URL_SPEECH= 'https://api.apigw.smt.docomo.ne.jp/voiceText/v1/textToSpeech?APIKEY='
URL_RECOG = 'https://api.apigw.smt.docomo.ne.jp/amiVoice/v1/recognize?APIKEY='

def blinkt_pulse(r,g,b):
    for i in range(blinkt.NUM_PIXELS):
        blinkt.clear()
        blinkt.set_pixel(i, r, g, b)
        blinkt.show()
        time.sleep(0.1)
    blinkt.clear()
    blinkt.show()

def blinkt_all(r, g, b):
    blinkt.clear()
    blinkt.set_all(r, g, b)
    blinkt.show()

blinkt.set_clear_on_exit()
blinkt.set_brightness(0.1)

GPIO.output(LED, GPIO.HIGH)
blinkt_pulse(0, 255, 0)
GPIO.output(LED, GPIO.LOW)

def camera():
    GPIO.output(LED, GPIO.HIGH)
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = '/home/pi/web/image/' + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
        os.mkdir(dir_path)
    except OSError:
        print 'Date dir already exists'
    c1 = 'fswebcam -r 640x480 --no-banner '
    os.system(c1 + fname)
    GPIO.output(LED, GPIO.LOW)
    return fname

def getImage(fname, modelName, lang, url):
    register_openers()
    f = open(fname, 'r')

    if modelName in models[1]['model'].keys() + models[2]['model'].keys():
        datagen, headers = multipart_encode({'image': f, 'modelName': modelName})
    else:
        url = url + '?APIKEY='
        datagen, headers = multipart_encode({'image': f, 'lang': lang})

    url = url + docomo_key
    request = urllib2.Request(url, datagen, headers)
    response= urllib2.urlopen(request)
    res_dat = response.read()

    if modelName in models[1]['model'].keys() + models[2]['model'].keys():
        res_json = json.loads(res_dat)['candidates']
    else:
        res_json = json.loads(res_dat)['job']['@id']

    print res_json
    return res_json


def makeWordList(result):
    word_list= []
    count    = int(result['words']['@count'])
    for i in range(count):
        word = result['words']['word'][i]
        word_list.append(word)
    return word_list


def getWordList(img_id):
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
        time.sleep(3)


def speech(message, speaker, VOLUME):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'text': message,
        'speaker': speaker,
        'volume': VOLUME,
        'emotion': 'happiness', #'sadness',
        'emotion_level': 2,
        'pitch': 100,
        'speed': 100,
    }

    try:
        values = urllib.urlencode(data)
        url = URL_SPEECH + docomo_key
        req = urllib2.Request(url, values, headers)
        res = urllib2.urlopen(req)
        header = res.info()
        data   = res.read()
        code   = res.getcode()
    except Exception as e:
        print e
        exit()
    print code, header
    return code,data

def talk(message='しゃべります！'):
    GPIO.output(LED, GPIO.HIGH)
    code, data = speech(message, speaker, VOLUME)
    if code == 200:
        f=open(speech_path, 'w')
        f.write(data)
        f.close()
        os.system('aplay -D plughw:{},{} '.format(CARD, DEVICE) + speech_path)
    else:
        print "Speech response is not 200"
    GPIO.output(LED, GPIO.LOW)


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
    parser.add_argument('--speaker',dest='speaker', type=str, default='', help='speaker name')
    parser.add_argument('--mail',   dest='mail', type=str, default='', help='send to email')

    args   = parser.parse_args()
    lang   = args.lang if args.lang else lang_def
    speaker= args.speaker if args.speaker else speaker_def
    tomail = args.mail if args.mail else ''
    print lang, speaker, tomail

    GPIO.add_event_detect(BUTTON,GPIO.FALLING)
    while True:
        print "Press 1 (scene, food), 2 (body, ccy), 3 (word) times, or hold to listen!"
        if GPIO.event_detected(BUTTON):
            message   = ""
            fname     = ""
            model_name= ""
            count     = 0

            GPIO.remove_event_detect(BUTTON)
            now = time.time()
            GPIO.add_event_detect(BUTTON,GPIO.RISING)
            while time.time() < now + hold_time:
                if GPIO.event_detected(BUTTON):
                    count +=1
                    time.sleep(.3) # debounce time

            print count
            if count == 0:
                blinkt_pulse(255, 255, 0)
                talk('何を撮りますか？')
                rec = recognize(rec_time)
                print rec
                talk(rec.encode('utf-8') + '、と言ったのですか？')

                for i in range(1,4):
                    for k,v in models[i]['model'].items():
                        print k, v
                        if re.match(v, rec):
                            model_name = k
                            count= i
                            break

            if count > 0:
                if count > 3: count = 3
                model_desc = models[count]['name']
                url = models[count]['url']
                print url, model_desc

                talk('では、' + model_desc + '写真を撮ります！')
                blinkt_all(flash, flash, flash)
                talk('かしゃ！！')
                fname = camera()
                img = cv2.imread(fname)
                oname = fname.replace('.jpg', '_o.jpg')
                blinkt_all(0, 0, 0)
                blinkt.clear()
                blinkt.show()

                candidate_list = []
                obj    = 0
                objects= ''
                if count in [1, 2]:
                    blinkt_pulse(0, 0, 255)
                    if model_name == '':
                      for model in models[count]['model'].keys():
                        print model
                        candidate_list += getImage(fname, model, lang, url)
                    else:
                      candidate_list = getImage(fname, model_name, lang, url)
                    for can in candidate_list:
                        score    = round(can['score']*100, 1)
                        object   = can['tag']
                        obj_model= model_name
                        if count == 2:
                            x = int(can['xMin'])
                            y = int(can['yMin'])
                            x2= int(can['xMax'])
                            y2= int(can['yMax'])
                        if score > accuracy:
                            obj +=1
                            obj_score = object + "(" + str(score) + "%)"
                            print obj_score
                            if object: objects += object + ', '
                            if count == 2:
                                cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), thickness=2)
                                cv2.putText(img, obj_score.encode('utf-8'), (x-10, y2+20), cv2.CV_AA, 0.6, (0, 0, 255), 1, cv2.CV_AA)

                elif count == 3:
                        blinkt_pulse(0, 255, 255)
                        model_name = "word"
                        image_list = getImage(fname, model_name, lang, url)
                        candidate_list = getWordList(image_list)
                        for can in candidate_list:
                            score    = float(can['@score'])
                            object   = can['@text']
                            obj_model= can['@category']
                            x  = int(can['shape']['point'][0]['@x'])
                            y  = int(can['shape']['point'][0]['@y'])
                            x2= int(can['shape']['point'][2]['@x'])
                            y2= int(can['shape']['point'][2]['@y'])
                            if score > accuracy:
                                obj +=1
                                cv2.rectangle(img, (x, y), (x2, y2), (0, 0, 255), thickness=2)
                                obj_score = object + "(" + str(score) + "%)"
                                print obj_score
                                if object: objects += object + ', '

                message = str(obj) + " object detected: "
                cv2.putText(img, message.encode('utf-8'), (10, 20), cv2.CV_AA, 0.8, (255, 0, 0), 1, cv2.CV_AA)
                cv2.imwrite(oname, img)

                if objects: message += objects.encode('utf-8') + "が写っているかもしれません！"

                blinkt_pulse(0, 255, 0)
                print message
                talk(message)

                msgname = fname.replace('.jpg', '_msg.txt')
                f = open(msgname, 'w')
                f.write(message)
                f.close()
                if tomail and obj > 0:
                    os.system("mutt -s " + model_desc + " " + tomail + " -a " + oname + " < " + msgname)
                    mailmsg = "メールが、" + tomail + "に送られました。"
                    talk(mailmsg)

            else:
                talk("わかりませんでした！また、撮ってくださいね！")

            GPIO.remove_event_detect(BUTTON)
            GPIO.add_event_detect(BUTTON, GPIO.FALLING)
            
