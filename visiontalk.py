# -*- coding: utf-8 -*-

import argparse
import base64
import httplib2
import picamera
import os
import re
from datetime import datetime

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

from PIL import Image, ImageDraw

import aiy.audio
import aiy.voicehat

from pixels import pixels
#aiy.i18n.set_language_code('ja-JP')
#default_speech= 'en-US'
default_trans = 'ja-JP'
aiy_lang = ['en-US', 'en-GB', 'de-DE', 'es-ES', 'fr-FR', 'it-IT']

import urllib.request, urllib.parse, urllib.error
DEVICE = 0
CARD   = 0
VOLUME = 50
aquest_dir = '/home/pi/AIY-projects-python/src/aquestalkpi/AquesTalkPi'

from google.cloud import translate
def translate_text(text, trans_lang):
    if trans_lang == '':
        return text
    else:
      target_lang = trans_lang.split("-")[0]
      translate_client = translate.Client()
      result = translate_client.translate(text, target_language=target_lang)
      return result['translatedText']
    
default_detect= ["FACE", "LABEL", "LOGO"]
default_max   = 3
dir_image     = '/home/pi/AIY-projects-python/src/smart/image/'
DISCOVERY_URL = "https://{api}.googleapis.com/$discovery/rest?version={apiVersion}"
def camera():
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = dir_image + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
      os.mkdir(dir_path)
    except OSError:
      print('Date dir already exists')
    #os.system('raspistill -o ' + fname)
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)
    camera.capture(fname)
    return fname

def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)
    for bound in bounds:
        draw.polygon([
            bound.vertices[0].x, bound.vertices[0].y,
            bound.vertices[1].x, bound.vertices[1].y,
            bound.vertices[2].x, bound.vertices[2].y,
            bound.vertices[3].x, bound.vertices[3].y], None, color)
    return image

def main(detect="", photo_file="", trans_lang=""):
    pixels.wakeup()
    if photo_file == "":
        photo_file = camera()
    pixels.off()
    
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials,
            discoveryServiceUrl=DISCOVERY_URL)

    pixels.listen()
    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        if detect == "": #No parameter
          DETECT = default_detect
        else: #Paremater specified
          DETECT = [detect.upper()]

        result   = ""
        bounds   = []
        tlocale  = ""
        for DET in DETECT:
          service_request = service.images().annotate(body={
            'requests': [{
                'image': {
                    'content': image_content.decode('UTF-8')
                    },
                'features': [{
                    'type': DET+'_DETECTION',
                    'maxResults': default_max
                    }]
                }]
            })
          response = service_request.execute()
          annotation = DET.lower()+'Annotations'
          try:
            results = response['responses'][0][annotation]
            for res in results:
              if DET in ["LABEL", "LOGO"]:
                if res["score"] > 0.7:
                  result += res["description"]+", "
                
              elif DET in ["TEXT"]:
                tlocale = res["locale"]
                result += res["description"]+", "
                bounds += res["boundingPoly"]["vertices"]

              elif DET in ["FACE"]:
                if res["joyLikelihood"] == "VERY_LIKELY" or res["joyLikelihood"] == "LIKELY":
                  result += "Smile "
                if res["angerLikelihood"] == "VERY_LIKELY" or res["angerLikelihood"] == "LIKELY":
                  result += "Angry "
                if res["headwearLikelihood"] == "VERY_LIKELY" or res["headwearLikelihood"] == "LIKELY":
                  rsult += "Capped "
                
              result += DET + ", "            
          except:
            result += "No " + DET + ", "
          pixels.off()
          print('Result: ' + result)
            
          pixels.listen()    
          if trans_lang:
            trans_text = translate_text(result, trans_lang)
            trans_text = trans_text.replace("&#39;","")
            print('Trans: ' + trans_text)
            if trans_lang in aiy_lang:
              aiy.audio.say(trans_text, trans_lang)
            elif trans_lang == "ja-JP":
              os.system(aquest_dir + ' -g {} {} | aplay -D plughw:{},{}'.format(VOLUME, trans_text, CARD, DEVICE))
            else:
              aiy.audio.say('Nothing to trans!', 'en-US')
            
          else: #trans_lang = null then default en-US
            aiy.audio.say(result, 'en-US')
            
          pixels.off()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--detect', nargs='?', default='', help='LABEL, FACE, LOGO and TEXT_DETECTION')
    parser.add_argument('--image', nargs='?', default='', help='Image file name')
    parser.add_argument('--trans', nargs='?', default='', help='If null no trans (en-US) or trans lang like ja-JP')
    args = parser.parse_args()
    main(args.detect, args.image, args.trans)
    
