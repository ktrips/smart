# Raspberry Pi Smart devices with Google APIs

## How to setup the smart app and hardware

1. Install Google AIY to your Raspberry Pi

2. Make smart folder and copy examples from AIY python
```mkdir ~/AIY-projects-python/src/smart
sudo cp ~/AIY-projects-python/src/examples/voice/* ~/AIY-projects-python/src/smart/
 
3. Place each files to the smart folder

4. Setup required software

### Downlaod and install Seeed software

```git clone
 
### Download [AquesTalk](https://www.a-quest.com/products/aquestalkpi.html)
```wget https://www.a-quest.com/archive/package/aquestalkpi-20130827.tgz
tar xzvf aquestalkpi-*.tgz

5. Setup Google SDK
### Setup Google Vision
```sudo nano ~/.bashrc

```GOOGLE_APPLICATION_CREDENTIALS="/home/pi/visionxxx.json

```echo $GOOGLE_APPLICATION_CREDENTIALS

### Setup Google Translate
```pip install --upgrade google-cloud-translate
