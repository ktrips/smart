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

#aiy.i18n.set_language_code('ja-JP')
default_speech = 'ja-JP'
default_detect = ["FACE", "LABEL", "LOGO"]
default_max    = 3

dir_image = '/home/pi/AIY-projects-python/src/robot/image/'

DISCOVERY_URL="https://{api}.googleapis.com/$discovery/rest?version={apiVersion}"

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

def main(detection, photo_file):
    if photo_file == "":
        photo_file = camera()
    credentials = GoogleCredentials.get_application_default()
    service = discovery.build('vision', 'v1', credentials=credentials,
            discoveryServiceUrl=DISCOVERY_URL)

    with open(photo_file, 'rb') as image:
        image_content = base64.b64encode(image.read())
        if detection == "": #No parameter
          DETECT = default_detect
        else: #Paremater specified
          DETECT = [detection.upper()]

        result   = ""
        result_ja= ""
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
                  result += res["description"]+","
                
              elif DET in ["TEXT"]:
                tlocale = res["locale"]
                result += res["description"]+","
                bounds += res["boundingPoly"]["vertices"]

              elif DET in ["FACE"]:
                if res["joyLikelihood"] == "VERY_LIKELY":
                  result += "Smile "
                  result_ja += "笑っている"
                if res["angerLikelihood"] == "VERY_LIKELY":
                  result += "Angry "
                  result_ja += "怒っている"
                if res["headwearLikelihood"] == "VERY_LIKELY":
                  rsult += "Cap "
                  result_ja += "帽子かぶってる"
                result += "Face! "
                result_ja += "人を見つけました！"

          except:
            result += "No "+DET
            result_ja += "いませんでした！"

        return result

if __name__ == '__main__':
     parser = argparse.ArgumentParser()
     parser.add_argument('detection', nargs='?', default='', help='LABEL, FACE, LOGO_DETECTION')
     parser.add_argument('image', nargs='?', default='', help='Image file name')
     parser.add_argument('speech', nargs='?', default='ja-JP', help='')
     args = parser.parse_args()
     result = main(args.detection, args.image)
     print(result)
     aiy.audio.say(result, args.speech)
