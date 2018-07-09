#!/bin/bash --rcfile

source /etc/bash.bashrc
source ~/.bashrc

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/vision.json
echo $GOOGLE_APPLICATION_CREDENTIALS
amixer --card 0 cset numid=11 100%

cd ~/AIY-projects-python/src/smart/
echo "Running VisionTalk.py!"
python3 visiontrans.py --detect text --trans ja-JP
echo "VisionTalk is done!"
