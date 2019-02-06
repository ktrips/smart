# -*- coding: utf-8 -*-
import subprocess, os, sys, re
from datetime import datetime
import time

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

def main(image=""):
    if image == "":
        fname = camera()
    else:
        fname = image
　　print(fname)

if __name__ == '__main__':
    main()
