# -*- coding: utf-8 -*-
import subprocess, os, sys, re
from datetime import datetime
import time
import requests

def camera():
    now = datetime.now()
    dir_name = now.strftime('%Y%m%d')
    dir_path = '/home/pi/smart/image/' + dir_name + '/'
    file_name= now.strftime('%H%M%S') + '.jpg'
    fname    = dir_path + file_name
    try:
        os.mkdir(dir_path)
    except OSError:
        print('Date dir already exists')
    os.system('raspistill -w 480 -h 360 -o ' + fname)
    return fname


def line(fname):
    url = "https://notify-api.line.me/api/notify"
    token = "4FJ9nlw1i7P95ncAfmy2DoXmc4GUlDxHh8tXHc5gdbn"
    headers = {"Authorization" : "Bearer "+ token}

    message =  "写真を撮りました！"
    payload = {"message" :  message}
    files = {"imageFile": open(fname, "rb")}
    print(fname)
    r = requests.post(url, headers = headers, params=payload, files=files)
    print(r.text)


def main(image=""):
    if image == "":
        fname = camera()
    else:
        fname = image
    if fname:
      line(fname)


if __name__ == '__main__':
    main()
