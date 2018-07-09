#!/bin/bash --rcfile

source /etc/bash.bashrc
source ~/.bashrc

export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/vision.json
echo $GOOGLE_APPLICATION_CREDENTIALS

cd ~/AIY-projects-python/src/smart/
echo "Running VisionTalk.py!"
python3 visiontalk.py
echo "VisionTalk is done!"
