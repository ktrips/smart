Last login: Sat Dec 29 16:06:35 on ttys001
KMBP:~ ktrips$ ssh pi@raspberrypi.local
pi@raspberrypi.local's password: 
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec 29 18:38:53 2018 from 240f:3a:2015:1:fc22:a35e:7d27:d4dd
pi@raspberrypi:~ $ ls
Desktop    Downloads  Music     Public     Videos
Documents  MagPi      Pictures  Templates  smart
pi@raspberrypi:~ $ cd smart/
pi@raspberrypi:~/smart $ ls
BME280       blinka.py   parse_pulse.rb  raspi3               sony.lircd.conf
air          bme280.py   pixel.py        remotetv.lircd.conf  test.wav
aquestalkpi  bme_led.py  pixelfull.py    snowboy              tv
pi@raspberrypi:~/smart $ aplay test.wav 
再生中 WAVE 'test.wav' : Signed 16 bit Little Endian, レート 48000 Hz, ステレオ
aplay: pcm_write:2011: 書込エラー: 入力/出力エラーです
pi@raspberrypi:~/smart $ sudo reboot now
Connection to raspberrypi.local closed by remote host.
Connection to raspberrypi.local closed.
KMBP:~ ktrips$ ssh pi@raspberrypi.local
pi@raspberrypi.local's password: 
Permission denied, please try again.
pi@raspberrypi.local's password: 
Linux raspberrypi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec 29 19:11:53 2018
pi@raspberrypi:~ $ sudo raspi-config
Connection to raspberrypi.local closed by remote host.
Connection to raspberrypi.local closed.
KMBP:~ ktrips$ ssh pi@aipi.local
The authenticity of host 'aipi.local (240f:3a:2015:1:fa94:f402:c47b:e582)' can't be established.
ECDSA key fingerprint is SHA256:bz84ob4C47lRprS4mqYd3mmOiqMJLPy5ZiPnajtPmic.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'aipi.local' (ECDSA) to the list of known hosts.
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec 29 19:14:29 2018
pi@aipi:~ $ ls
Desktop    Downloads  Music     Public     Videos
Documents  MagPi      Pictures  Templates  smart
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ ls
BME280       blinka.py   parse_pulse.rb  raspi3               sony.lircd.conf
air          bme280.py   pixel.py        remotetv.lircd.conf  test.wav
aquestalkpi  bme_led.py  pixelfull.py    snowboy              tv
pi@aipi:~/smart $ aplay test.wav 
再生中 WAVE 'test.wav' : Signed 16 bit Little Endian, レート 48000 Hz, ステレオ
^Cシグナル 割り込み で中断...
pi@aipi:~/smart $ python bme_led.py 
temp : 23.19  ℃
pressure : 1014.29 hPa
hum :  34.13 ％
今の室温は、23.2度、湿度は、34.1パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
pi@aipi:~/smart $ aplay test.wav 
再生中 WAVE 'test.wav' : Signed 16 bit Little Endian, レート 48000 Hz, ステレオ


aplay: pcm_write:2011: 書込エラー: 入力/出力エラーです
pi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ sudo vi bme_led.py 
pi@aipi:~/smart $ python bme_led.py 
temp : 23.02  ℃
pressure : 1014.38 hPa
hum :  34.35 ％
今の室温は、23.0度、湿度は、34.4パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
aplay: pcm_write:2011: 書込エラー: 入力/出力エラーです
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart $ sudo reboot now
Connection to aipi.local closed by remote host.
Connection to aipi.local closed.
KMBP:~ ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Dec 29 19:18:09 2018
pi@aipi:~ $ ls
Desktop    Downloads  Music     Public     Videos
Documents  MagPi      Pictures  Templates  smart
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ ls
BME280       blinka.py   parse_pulse.rb  raspi3               sony.lircd.conf
air          bme280.py   pixel.py        remotetv.lircd.conf  test.wav
aquestalkpi  bme_led.py  pixelfull.py    snowboy              tv
pi@aipi:~/smart $ python bme_led.py 
temp : 23.22  ℃
pressure : 1014.33 hPa
hum :  34.04 ％
今の室温は、23.2度、湿度は、34.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart $ ls
BME280       blinka.py   parse_pulse.rb  raspi3               sony.lircd.conf
air          bme280.py   pixel.py        remotetv.lircd.conf  test.wav
aquestalkpi  bme_led.py  pixelfull.py    snowboy              tv
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          demo_arecord.py                     snowboydecoder.py
__pycache__        light.py                            snowboydecoder.pyc
_snowboydetect.so  requirements.txt                    snowboydetect.py
demo.py            resources                           snowboydetect.pyc
demo2.py           rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
pi@aipi:~/smart/snowboy $ ls
README.md          demo_arecord.py                     snowboydecoder.py
__pycache__        light.py                            snowboydecoder.pyc
_snowboydetect.so  requirements.txt                    snowboydetect.py
demo.py            resources                           snowboydetect.pyc
demo2.py           rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
  File "wake_led.py", line 19
    print(“エラーです。モデル名を指定して下さい。”)
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
Traceback (most recent call last):
  File "wake_led.py", line 24, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ ls
README.md          light.py                            snowboydecoder.pyc
__pycache__        light.pyc                           snowboydetect.py
_snowboydetect.so  requirements.txt                    snowboydetect.pyc
demo.py            resources                           version
demo2.py           rpi-arm-raspbian-8.0-1.1.1.tar.bz2  wake_led.py
demo_arecord.py    snowboydecoder.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/snowboy.umdl 
Traceback (most recent call last):
  File "wake_led.py", line 24, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ python
Python 2.7.13 (default, Sep 26 2018, 18:42:22) 
[GCC 6.3.0 20170516] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from light import Light
>>> interrupted = False
>>> LED=17
>>> led=LIGHT(LED)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'LIGHT' is not defined
>>> led=Light(LED)
>>> led.blink
<bound method Light.blink of <light.Light object at 0x76a75570>>
>>> Light.blink
<unbound method Light.blink>
>>> 
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> 
>>> l
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'l' is not defined
>>> 
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> 
pi@aipi:~/smart/snowboy $ ls
README.md          light.py                            snowboydecoder.pyc
__pycache__        light.pyc                           snowboydetect.py
_snowboydetect.so  requirements.txt                    snowboydetect.pyc
demo.py            resources                           version
demo2.py           rpi-arm-raspbian-8.0-1.1.1.tar.bz2  wake_led.py
demo_arecord.py    snowboydecoder.py
pi@aipi:~/smart/snowboy $ ls
README.md          light.py                            snowboydecoder.pyc
__pycache__        light.pyc                           snowboydetect.py
_snowboydetect.so  requirements.txt                    snowboydetect.pyc
demo.py            resources                           version
demo2.py           rpi-arm-raspbian-8.0-1.1.1.tar.bz2  wake_led.py
demo_arecord.py    snowboydecoder.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/snowboy.umdl 
Traceback (most recent call last):
  File "wake_led.py", line 24, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
^Cpi@aipi:~/smart/snowboy $ ls
README.md          demo2.py         requirements.txt                    snowboydecoder.pyc  wake_led.py
__pycache__        demo_arecord.py  resources                           snowboydetect.py
_snowboydetect.so  light.py         rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.pyc
demo.py            light.pyc        snowboydecoder.py                   version
pi@aipi:~/smart/snowboy $ python demo2.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
INFO:snowboy:Keyword 2 detected at time: 2018-12-29 22:37:31
INFO:snowboy:Keyword 1 detected at time: 2018-12-29 22:37:36
INFO:snowboy:Keyword 1 detected at time: 2018-12-29 22:37:39
INFO:snowboy:Keyword 2 detected at time: 2018-12-29 22:37:40
INFO:snowboy:Keyword 2 detected at time: 2018-12-29 22:37:41
INFO:snowboy:Keyword 2 detected at time: 2018-12-29 22:37:43
^Cpi@aipi:~/smart/snowboy $ sudo vi wake_led.py 
pi@aipi:~/smart/snowboy $ sudo vi demo.py 
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py 
pi@aipi:~/smart/snowboy $ python wake_led.py resources/snowboy.umdl 
Traceback (most recent call last):
  File "wake_led.py", line 22, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ cd ..
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ sudo vi bme_led.py 
pi@aipi:~/smart $ python bme_led.py 
Traceback (most recent call last):
  File "bme_led.py", line 20, in <module>
    from light import Light
ImportError: No module named light
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ sudo vi light.py
pi@aipi:~/smart $ python light.py 
light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
^CTraceback (most recent call last):
  File "light.py", line 40, in <module>
    time.sleep(0.7)
KeyboardInterrupt
pi@aipi:~/smart $ python bme_led.py 
/home/pi/smart/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
temp : 22.31  ℃
pressure : 1015.94 hPa
hum :  34.45 ％
今の室温は、22.3度、湿度は、34.5パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart $ sudo vi bme_led.py 
pi@aipi:~/smart $ python bme_led.py 
/home/pi/smart/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
temp : 22.41  ℃
pressure : 1015.85 hPa
hum :  35.19 ％
今の室温は、22.4度、湿度は、35.2パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart $ python bme_led.py 
/home/pi/smart/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
temp : 22.38  ℃
pressure : 1015.85 hPa
hum :  34.69 ％
今の室温は、22.4度、湿度は、34.7パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart $ ls
BME280       blinka.py   light.py        pixel.py      remotetv.lircd.conf  test.wav
air          bme280.py   light.pyc       pixelfull.py  snowboy              tv
aquestalkpi  bme_led.py  parse_pulse.rb  raspi3        sony.lircd.conf
pi@aipi:~/smart $ sudo cp bme_led.py light.py snowboy/
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.pyc                           snowboydecoder.py   version
__pycache__        demo2.py         requirements.txt                    snowboydecoder.pyc  wake_led.py
_snowboydetect.so  demo_arecord.py  resources                           snowboydetect.py
bme_led.py         light.py         rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.pyc
pi@aipi:~/smart/snowboy $ python bme_led.py 
/home/pi/smart/snowboy/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
temp : 22.52  ℃
pressure : 1015.88 hPa
hum :  34.55 ％
今の室温は、22.5度、湿度は、34.5パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Dry!
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
pi@aipi:~/smart/snowboy $ sudo shutdown now
Connection to aipi.local closed by remote host.
Connection to aipi.local closed.
KMBP:~ ktrips$ diskutil list
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         251.0 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         250.7 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +250.7 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            101.9 GB   disk1s1
   2:                APFS Volume Preboot                 44.2 MB    disk1s2
   3:                APFS Volume Recovery                517.0 MB   disk1s3
   4:                APFS Volume VM                      3.2 GB     disk1s4

/dev/disk3 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:     FDisk_partition_scheme                        *15.9 GB    disk3
   1:             Windows_FAT_32 boot                    43.8 MB    disk3s1
   2:                      Linux                         15.9 GB    disk3s2

KMBP:~ ktrips$ ls
Applications		Downloads		Library			Public
Creative Cloud Files	Dropbox			Movies
Desktop			GitHub			Music
Documents		Google ドライブ		Pictures
KMBP:~ ktrips$ cd Downloads/
KMBP:Downloads ktrips$ ls
1221_Arduino_eBook_1_rev.pdf		Install Spotify.app
2018-11-13-raspbian-stretch-full.img	InstallBackupAndSync.dmg
2018-11-13-raspbian-stretch-full.zip	Mac_OSX_VCP_Driver
AI-Transformation-Playbook.pdf		Mac_OSX_VCP_Driver (1).zip
Adafruit BME280 (1).fzpz		Mac_OSX_VCP_Driver (2).zip
Adafruit BME280.fzpz			Mac_OSX_VCP_Driver 2
Adafruit Breadboard NeoPixel.fzpz	Mac_OSX_VCP_Driver 3
Adafruit NeoPixel Stick.fzpz		Mac_OSX_VCP_Driver.zip
Arduino.app				ReceiverUpdaterCertMac.pkg
ArduinoWatchFiles.zip			SpotifyInstaller.zip
Atom.app				aquestalkpi-20130827.tgz
DevicePlus_RasPi1_121818.pdf		arduino-1.8.8-macosx.zip
DropboxInstaller.dmg			atom-1.33.0-full.nupkg
En_Kenichi_Yoshida_180301.docx		atom-mac.zip
Fritzing-Library-master			py-thermal-printer-master.zip
Fritzing-Library-master.zip		result.nnb
Fritzing0.9.3b.dmg			result.nnp
Fusion 360 Client Downloader.dmg	rpi-arm-raspbian-8.0-1.1.1.tar.bz2
IMG_7326.TRIM.MOV			spresense-binaries-v1.1.0
IMG_7327.TRIM.MOV			spresense-binaries-v1.1.0.zip
Illustrator_Installer.dmg
KMBP:Downloads ktrips$ diskutil unMountDisk /dev/disk3
Unmount of all volumes on disk3 was successful
KMBP:Downloads ktrips$ sudo dd if=/Users/ktrips/Downloads/2018-11-13-raspbian-stretch-full.img of=/dev/rdisk3 bs=1m
Password:
5052+0 records in
5052+0 records out
5297405952 bytes transferred in 486.472768 secs (10889419 bytes/sec)
KMBP:Downloads ktrips$ 
KMBP:Downloads ktrips$ 
KMBP:Downloads ktrips$ ssh pi@aipi.local
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@       WARNING: POSSIBLE DNS SPOOFING DETECTED!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
The ECDSA host key for aipi.local has changed,
and the key for the corresponding IP address 240f:3a:2015:1:d2bc:86d5:c441:cf02
is unknown. This could either mean that
DNS SPOOFING is happening or the IP address for the host
and its host key have changed at the same time.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the ECDSA key sent by the remote host is
SHA256:kvpvVx0nE3M3xgk7oRfjbRu7VycLSU2TQZWOGofK9ZU.
Please contact your system administrator.
Add correct host key in /Users/ktrips/.ssh/known_hosts to get rid of this message.
Offending ECDSA key in /Users/ktrips/.ssh/known_hosts:19
ECDSA host key for aipi.local has changed and you have requested strict checking.
Host key verification failed.
KMBP:Downloads ktrips$ vi /Users/ktrips/.ssh/known_hosts
KMBP:Downloads ktrips$ ssh pi@aipi.local
The authenticity of host 'aipi.local (240f:3a:2015:1:d2bc:86d5:c441:cf02)' can't be established.
ECDSA key fingerprint is SHA256:kvpvVx0nE3M3xgk7oRfjbRu7VycLSU2TQZWOGofK9ZU.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'aipi.local,240f:3a:2015:1:d2bc:86d5:c441:cf02' (ECDSA) to the list of known hosts.
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan  5 08:06:32 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos
pi@aipi:~ $ sudo apt-get install python-pyaudio python3-pyaudio sox
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下の追加パッケージがインストールされます:
  libopencore-amrnb0 libopencore-amrwb0 libsox-fmt-alsa libsox-fmt-base libsox2
提案パッケージ:
  libsox-fmt-all python-pyaudio-doc
以下のパッケージが新たにインストールされます:
  libopencore-amrnb0 libopencore-amrwb0 libsox-fmt-alsa libsox-fmt-base libsox2 python-pyaudio python3-pyaudio
  sox
アップグレード: 0 個、新規インストール: 8 個、削除: 0 個、保留: 0 個。
647 kB のアーカイブを取得する必要があります。
この操作後に追加で 1,422 kB のディスク容量が消費されます。
続行しますか? [Y/n] Y
0% [raspbian.raspberrypi.org (2a00:1098:0:80:1000:75:0:3) へ接続しています]
取得:1 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf libopencore-amrnb0 armhf 0.1.3-2.1 [80.4 kB]
取得:2 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf libopencore-amrwb0 armhf 0.1.3-2.1 [42.0 kB]
取得:3 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf libsox2 armhf 14.4.1-5 [231 kB]
取得:4 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf libsox-fmt-alsa armhf 14.4.1-5 [47.0 kB]
取得:5 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf libsox-fmt-base armhf 14.4.1-5 [63.8 kB]
取得:6 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf python-pyaudio armhf 0.2.11-1 [24.3 kB]
取得:7 http://ftp.tsukuba.wide.ad.jp/Linux/raspbian/raspbian stretch/main armhf python3-pyaudio armhf 0.2.11-1 [24.3 kB]
取得:8 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf sox armhf 14.4.1-5 [135 kB]
647 kB を 3分 16秒 で取得しました (3,298 B/s)                           
以前に未選択のパッケージ libopencore-amrnb0:armhf を選択しています。
(データベースを読み込んでいます ... 現在 134256 個のファイルとディレクトリがインストールされています。)
.../0-libopencore-amrnb0_0.1.3-2.1_armhf.deb を展開する準備をしています ...
libopencore-amrnb0:armhf (0.1.3-2.1) を展開しています...
以前に未選択のパッケージ libopencore-amrwb0:armhf を選択しています。
.../1-libopencore-amrwb0_0.1.3-2.1_armhf.deb を展開する準備をしています ...
libopencore-amrwb0:armhf (0.1.3-2.1) を展開しています...
以前に未選択のパッケージ libsox2:armhf を選択しています。
.../2-libsox2_14.4.1-5_armhf.deb を展開する準備をしています ...
libsox2:armhf (14.4.1-5) を展開しています...
以前に未選択のパッケージ libsox-fmt-alsa:armhf を選択しています。
.../3-libsox-fmt-alsa_14.4.1-5_armhf.deb を展開する準備をしています ...
libsox-fmt-alsa:armhf (14.4.1-5) を展開しています...
以前に未選択のパッケージ libsox-fmt-base:armhf を選択しています。
.../4-libsox-fmt-base_14.4.1-5_armhf.deb を展開する準備をしています ...
libsox-fmt-base:armhf (14.4.1-5) を展開しています...
以前に未選択のパッケージ python-pyaudio を選択しています。
.../5-python-pyaudio_0.2.11-1_armhf.deb を展開する準備をしています ...
python-pyaudio (0.2.11-1) を展開しています...
以前に未選択のパッケージ python3-pyaudio を選択しています。
.../6-python3-pyaudio_0.2.11-1_armhf.deb を展開する準備をしています ...
python3-pyaudio (0.2.11-1) を展開しています...
以前に未選択のパッケージ sox を選択しています。
.../7-sox_14.4.1-5_armhf.deb を展開する準備をしています ...
sox (14.4.1-5) を展開しています...
mime-support (3.60) のトリガを処理しています ...
libsox2:armhf (14.4.1-5) を設定しています ...
python-pyaudio (0.2.11-1) を設定しています ...
libopencore-amrnb0:armhf (0.1.3-2.1) を設定しています ...
man-db (2.7.6.1-2) のトリガを処理しています ...
libopencore-amrwb0:armhf (0.1.3-2.1) を設定しています ...
python3-pyaudio (0.2.11-1) を設定しています ...
libsox-fmt-base:armhf (14.4.1-5) を設定しています ...
libsox-fmt-alsa:armhf (14.4.1-5) を設定しています ...
sox (14.4.1-5) を設定しています ...
pi@aipi:~ $ sudo pip install pyaudio
Requirement already satisfied: pyaudio in /usr/lib/python2.7/dist-packages
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ aplay -l
**** ハードウェアデバイス PLAYBACK のリスト ****
カード 0: ALSA [bcm2835 ALSA], デバイス 0: bcm2835 ALSA [bcm2835 ALSA]
  サブデバイス: 7/7
  サブデバイス #0: subdevice #0
  サブデバイス #1: subdevice #1
  サブデバイス #2: subdevice #2
  サブデバイス #3: subdevice #3
  サブデバイス #4: subdevice #4
  サブデバイス #5: subdevice #5
  サブデバイス #6: subdevice #6
カード 0: ALSA [bcm2835 ALSA], デバイス 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  サブデバイス: 1/1
  サブデバイス #0: subdevice #0
pi@aipi:~ $ arecord -l
**** ハードウェアデバイス CAPTURE のリスト ****
カード 1: Device [USB PnP Sound Device], デバイス 0: USB Audio [USB Audio]
  サブデバイス: 1/1
  サブデバイス #0: subdevice #0
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
Traceback (most recent call last):
  File "demo.py", line 1, in <module>
    import snowboydecoder
  File "/home/pi/smart/snowboy/snowboydecoder.py", line 5, in <module>
    import snowboydetect
  File "/home/pi/smart/snowboy/snowboydetect.py", line 28, in <module>
    _snowboydetect = swig_import_helper()
  File "/home/pi/smart/snowboy/snowboydetect.py", line 24, in swig_import_helper
    _mod = imp.load_module('_snowboydetect', fp, pathname, description)
ImportError: libf77blas.so.3: cannot open shared object file: No such file or directory
pi@aipi:~/smart/snowboy $ sudo apt-get install libatlas-base-dev
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下の追加パッケージがインストールされます:
  gfortran gfortran-6 libatlas-dev libatlas3-base libblas-dev libgfortran-6-dev
提案パッケージ:
  gfortran-doc gfortran-6-doc libgfortran3-dbg libcoarrays-dev libblas-doc liblapack-doc liblapack-dev
  liblapack-doc-man
以下のパッケージが新たにインストールされます:
  gfortran gfortran-6 libatlas-base-dev libatlas-dev libatlas3-base libblas-dev libgfortran-6-dev
アップグレード: 0 個、新規インストール: 7 個、削除: 0 個、保留: 0 個。
10.2 MB のアーカイブを取得する必要があります。
この操作後に追加で 48.4 MB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf libgfortran-6-dev armhf 6.3.0-18+rpi1+deb9u1 [199 kB]
取得:2 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf gfortran-6 armhf 6.3.0-18+rpi1+deb9u1 [5,421 kB]
取得:3 http://raspbian.raspberrypi.org/raspbian stretch/main armhf gfortran armhf 4:6.3.0-4 [1,352 B]          
取得:4 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf libatlas3-base armhf 3.10.3-1+rpi1 [1,920 kB]
取得:5 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf libblas-dev armhf 3.7.0-2 [114 kB]
取得:6 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf libatlas-dev armhf 3.10.3-1+rpi1 [65.9 kB]
取得:7 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf libatlas-base-dev armhf 3.10.3-1+rpi1 [2,528 kB]
10.2 MB を 10秒 で取得しました (1,014 kB/s)                                                                    
以前に未選択のパッケージ libgfortran-6-dev:armhf を選択しています。
(データベースを読み込んでいます ... 現在 134352 個のファイルとディレクトリがインストールされています。)
.../0-libgfortran-6-dev_6.3.0-18+rpi1+deb9u1_armhf.deb を展開する準備をしています ...
libgfortran-6-dev:armhf (6.3.0-18+rpi1+deb9u1) を展開しています...
以前に未選択のパッケージ gfortran-6 を選択しています。
.../1-gfortran-6_6.3.0-18+rpi1+deb9u1_armhf.deb を展開する準備をしています ...
gfortran-6 (6.3.0-18+rpi1+deb9u1) を展開しています...
以前に未選択のパッケージ gfortran を選択しています。
.../2-gfortran_4%3a6.3.0-4_armhf.deb を展開する準備をしています ...
gfortran (4:6.3.0-4) を展開しています...
以前に未選択のパッケージ libatlas3-base を選択しています。
.../3-libatlas3-base_3.10.3-1+rpi1_armhf.deb を展開する準備をしています ...
libatlas3-base (3.10.3-1+rpi1) を展開しています...
以前に未選択のパッケージ libblas-dev を選択しています。
.../4-libblas-dev_3.7.0-2_armhf.deb を展開する準備をしています ...
libblas-dev (3.7.0-2) を展開しています...
以前に未選択のパッケージ libatlas-dev を選択しています。
.../5-libatlas-dev_3.10.3-1+rpi1_armhf.deb を展開する準備をしています ...
libatlas-dev (3.10.3-1+rpi1) を展開しています...
以前に未選択のパッケージ libatlas-base-dev を選択しています。
.../6-libatlas-base-dev_3.10.3-1+rpi1_armhf.deb を展開する準備をしています ...
libatlas-base-dev (3.10.3-1+rpi1) を展開しています...
libatlas3-base (3.10.3-1+rpi1) を設定しています ...
update-alternatives: /usr/lib/libblas.so.3 (libblas.so.3) を提供するために自動モードで /usr/lib/atlas-base/atlas/libblas.so.3 を使います
update-alternatives: /usr/lib/liblapack.so.3 (liblapack.so.3) を提供するために自動モードで /usr/lib/atlas-base/atlas/liblapack.so.3 を使います
libgfortran-6-dev:armhf (6.3.0-18+rpi1+deb9u1) を設定しています ...
libc-bin (2.24-11+deb9u3) のトリガを処理しています ...
man-db (2.7.6.1-2) のトリガを処理しています ...
gfortran-6 (6.3.0-18+rpi1+deb9u1) を設定しています ...
gfortran (4:6.3.0-4) を設定しています ...
update-alternatives: /usr/bin/f95 (f95) を提供するために自動モードで /usr/bin/gfortran を使います
update-alternatives: /usr/bin/f77 (f77) を提供するために自動モードで /usr/bin/gfortran を使います
libblas-dev (3.7.0-2) を設定しています ...
update-alternatives: /usr/lib/libblas.so (libblas.so) を提供するために自動モードで /usr/lib/libblas/libblas.so を使います
libatlas-dev (3.10.3-1+rpi1) を設定しています ...
libatlas-base-dev (3.10.3-1+rpi1) を設定しています ...
update-alternatives: /usr/lib/libblas.so (libblas.so) を提供するために自動モードで /usr/lib/atlas-base/atlas/libblas.so を使います
update-alternatives: /usr/lib/liblapack.so (liblapack.so) を提供するために自動モードで /usr/lib/atlas-base/atlas/liblapack.so を使います
pi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Expression 'paInvalidSampleRate' failed in 'src/hostapi/alsa/pa_linux_alsa.c', line: 2048
Expression 'PaAlsaStreamComponent_InitialConfigure( &self->capture, inParams, self->primeBuffers, hwParamsCapture, &realSr )' failed in 'src/hostapi/alsa/pa_linux_alsa.c', line: 2719
Expression 'PaAlsaStream_Configure( stream, inputParameters, outputParameters, sampleRate, framesPerBuffer, &inputLatency, &outputLatency, &hostBufferSizeMode )' failed in 'src/hostapi/alsa/pa_linux_alsa.c', line: 2843
Traceback (most recent call last):
  File "demo.py", line 27, in <module>
    detector = snowboydecoder.HotwordDetector(model, sensitivity=0.5)
  File "/home/pi/smart/snowboy/snowboydecoder.py", line 115, in __init__
    stream_callback=audio_callback)
  File "/usr/lib/python2.7/dist-packages/pyaudio.py", line 750, in open
    stream = Stream(self, *args, **kwargs)
  File "/usr/lib/python2.7/dist-packages/pyaudio.py", line 441, in __init__
    self._stream = pa.open(**arguments)
IOError: [Errno -9997] Invalid sample rate
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ arecord -l
**** ハードウェアデバイス CAPTURE のリスト ****
カード 1: Device [USB PnP Sound Device], デバイス 0: USB Audio [USB Audio]
  サブデバイス: 1/1
  サブデバイス #0: subdevice #0
pi@aipi:~/smart/snowboy $ aplay -l
**** ハードウェアデバイス PLAYBACK のリスト ****
カード 0: ALSA [bcm2835 ALSA], デバイス 0: bcm2835 ALSA [bcm2835 ALSA]
  サブデバイス: 7/7
  サブデバイス #0: subdevice #0
  サブデバイス #1: subdevice #1
  サブデバイス #2: subdevice #2
  サブデバイス #3: subdevice #3
  サブデバイス #4: subdevice #4
  サブデバイス #5: subdevice #5
  サブデバイス #6: subdevice #6
カード 0: ALSA [bcm2835 ALSA], デバイス 1: bcm2835 ALSA [bcm2835 IEC958/HDMI]
  サブデバイス: 1/1
  サブデバイス #0: subdevice #0
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ cd ..
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ python bme_led.py 
Traceback (most recent call last):
  File "bme_led.py", line 3, in <module>
    from smbus2 import SMBus
ImportError: No module named smbus2
pi@aipi:~/smart $ sudo pip install smbus2
Collecting smbus2
  Downloading https://files.pythonhosted.org/packages/58/4e/816148dc435d9c46616e972c4b4211b8e133f641ed2551fafd1c5a29de9f/smbus2-0.2.2.tar.gz
Building wheels for collected packages: smbus2
  Running setup.py bdist_wheel for smbus2 ... done
  Stored in directory: /root/.cache/pip/wheels/19/14/a5/0f2888cfffaadb48b22f9ba8702d0757a05c2d5e4094ce7207
Successfully built smbus2
Installing collected packages: smbus2
Successfully installed smbus2-0.2.2
pi@aipi:~/smart $ python bme_led.py 
temp : 18.77  ℃
pressure : 1011.81 hPa
hum :  40.42 ％
今の室温は、18.8度、湿度は、40.4パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Traceback (most recent call last):
  File "pixel.py", line 1, in <module>
    import board
ImportError: No module named 'board'
快適です！
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ cd
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ arecord -f cd -Dhw:1 | aplay -Dhw:0
録音中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 44100 Hz, ステレオ
arecord: set_params:1305: チャネル数が使用不可能
aplay: playback:2787: リードエラー
pi@aipi:~ $ sudo vi .asoundrc
pi@aipi:~ $ sudo reboot now
Connection to aipi.local closed by remote host.
Connection to aipi.local closed.
KMBP:Downloads ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan  5 08:25:51 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ cd smart/snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
^Cpi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
^Cpi@aipi:~/smart/snowboy $ alsamixer
pi@aipi:~/smart/snowboy $ alsamixer
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ python demo.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
^Cpi@aipi:~/smart/snowboy $ arecord -f cd -Dhw:1 | aplay -Dhw:0
録音中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 44100 Hz, ステレオ
arecord: set_params:1305: チャネル数が使用不可能
aplay: playback:2787: リードエラー
pi@aipi:~/smart/snowboy $ arecord -f S16_LE -r 16000 -D 1 t.wav
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM 1
arecord: main:788: audio open error: そのようなファイルやディレクトリはありません
pi@aipi:~/smart/snowboy $ arecord -l
**** ハードウェアデバイス CAPTURE のリスト ****
カード 1: Device [USB PnP Sound Device], デバイス 0: USB Audio [USB Audio]
  サブデバイス: 1/1
  サブデバイス #0: subdevice #0
pi@aipi:~/smart/snowboy $ ls
README.md          demo.py          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.py
__pycache__        demo2.py         requirements.txt  snowboydecoder.py                   snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  resources         snowboydecoder.pyc                  version
pi@aipi:~/smart/snowboy $ sudo apt-get update
ヒット:1 http://archive.raspberrypi.org/debian stretch InRelease                                               
取得:2 http://raspbian.raspberrypi.org/raspbian stretch InRelease [15.0 kB]                                    
15.0 kB を 1秒 で取得しました (11.1 kB/s)                       
パッケージリストを読み込んでいます... 完了
pi@aipi:~/smart/snowboy $ sudo shutdown now
Connection to aipi.local closed by remote host.
Connection to aipi.local closed.
KMBP:Downloads ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan  5 13:02:59 2019 from 192.168.0.8
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ cd smart/snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.pyc
__pycache__        demo.py          light.pyc         snowboydecoder.py                   version
_snowboydetect.so  demo2.py         requirements.txt  snowboydecoder.pyc                  wake_temp.py
bme.py             demo_arecord.py  resources         snowboydetect.py
pi@aipi:~/smart/snowboy $ cd resources/
pi@aipi:~/smart/snowboy/resources $ ls
alexa.umdl  alexa_02092017.umdl  common.res  ding.wav  dong.wav  snowboy.umdl
pi@aipi:~/smart/snowboy/resources $ sudo vi training.py
pi@aipi:~/smart/snowboy/resources $ python training.py 
  File "training.py", line 11
SyntaxError: Non-ASCII character '\xe3' in file training.py on line 11, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
pi@aipi:~/smart/snowboy/resources $ sudo vi training.py
pi@aipi:~/smart/snowboy/resources $ rec -r 16000 -c 1 -b 16 -e signed-integer 1.wav
rec WARN formats: can't set sample rate 16000; using 44100

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 44100
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:03.34 [00:00:00.00] Out:46.1k [      |      ]        Clip:0    ^C
Aborted.
pi@aipi:~/smart/snowboy/resources $ rec -r 16000 -c 1 -b 16 -e signed-integer 2.wav
rec WARN formats: can't set sample rate 16000; using 44100

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 44100
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:02.79 [00:00:00.00] Out:40.6k [      |      ]        Clip:0    ^C
Aborted.
pi@aipi:~/smart/snowboy/resources $ rec -r 16000 -c 1 -b 16 -e signed-integer 3.wav
rec WARN formats: can't set sample rate 16000; using 44100

Input File     : 'default' (alsa)
Channels       : 1
Sample Rate    : 44100
Precision      : 16-bit
Sample Encoding: 16-bit Signed Integer PCM

In:0.00% 00:00:02.97 [00:00:00.00] Out:40.6k [      |      ]        Clip:0    ^C
Aborted.
pi@aipi:~/smart/snowboy/resources $ ls
1.wav  2.wav  3.wav  alexa.umdl  alexa_02092017.umdl  common.res  ding.wav  dong.wav  snowboy.umdl  training.py
pi@aipi:~/smart/snowboy/resources $ python training.py 1.wav 2.wav 3.wav oheya.pmdl
Saved model to 'oheya.pmdl'.
pi@aipi:~/smart/snowboy/resources $ ls
1.wav  3.wav       alexa_02092017.umdl  ding.wav  oheya.pmdl    training.py
2.wav  alexa.umdl  common.res           dong.wav  snowboy.umdl
pi@aipi:~/smart/snowboy/resources $ cd ..
pi@aipi:~/smart/snowboy $ python demo.py resources/oheya.pmdl
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
Listening... Press Ctrl+C to exit
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:12:41
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:12:43
^Cpi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.pyc
__pycache__        demo.py          light.pyc         snowboydecoder.py                   version
_snowboydetect.so  demo2.py         requirements.txt  snowboydecoder.pyc                  wake_temp.py
bme.py             demo_arecord.py  resources         snowboydetect.py
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
  File "wake_led.py", line 19
    print(“エラーです。モデル名を指定して下さい。”)
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
Traceback (most recent call last):
  File "wake_led.py", line 24, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.py          rpi-arm-raspbian-8.0-1.1.1.tar.bz2  snowboydetect.pyc
__pycache__        demo.py          light.pyc         snowboydecoder.py                   version
_snowboydetect.so  demo2.py         requirements.txt  snowboydecoder.pyc                  wake_led.py
bme.py             demo_arecord.py  resources         snowboydetect.py                    wake_temp.py
pi@aipi:~/smart/snowboy $ sudo cp demo.py wake.py
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
Traceback (most recent call last):
  File "wake_led.py", line 23, in <module>
    detector = snowboydecoder.HotWordDetector(model, sensitivity=0.5)
AttributeError: 'module' object has no attribute 'HotWordDetector'
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py
pi@aipi:~/smart/snowboy $ sudo vi wake.py
pi@aipi:~/smart/snowboy $ python wake.py resources/oheya.pmdl 
  File "wake.py", line 21
SyntaxError: Non-ASCII character '\xe3' in file wake.py on line 21, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details
pi@aipi:~/smart/snowboy $ sudo vi wake.py
pi@aipi:~/smart/snowboy $ python wake.py resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:18:22
^Cpi@aipi:~/smart/snowboy sudo vi wake.pyl 
pi@aipi:~/smart/snowboy $ python wake.py resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
Traceback (most recent call last):
  File "wake.py", line 35, in <module>
    detector.start(detected_callback=led.blink, #snowboydecoder.play_audio_file,
NameError: name 'led' is not defined
pi@aipi:~/smart/snowboy $ sudo vi wake.py
pi@aipi:~/smart/snowboy $ python wake.py resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:19:26
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:19:28
^Cpi@aipi:~/smart/snowboy $ ls
README.md          demo.py          requirements.txt                    snowboydetect.py   wake_temp.py
__pycache__        demo2.py         resources                           snowboydetect.pyc
_snowboydetect.so  demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
bme.pyc            light.pyc        snowboydecoder.pyc                  wake_led.py
pi@aipi:~/smart/snowboy $ sudo mkdir arc
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo mv wake_led.py arc/
pi@aipi:~/smart/snowboy $ sudo cp wake.py wake_led.py
pi@aipi:~/smart/snowboy $ python wake_led.py 
エラーです。モデル名を指定して下さい。
pi@aipi:~/smart/snowboy $ python wake_led.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
/home/pi/smart/snowboy/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
^Cpi@aipi:~/smart/snowboy $ python wake_led.py resources/snowboy.umdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
/home/pi/smart/snowboy/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:20:31
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:20:34
^Cpi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo vi demo2.py 
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo cp wake_led.py wake2_led.py
pi@aipi:~/smart/snowboy $ sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
Traceback (most recent call last):
  File "wake2_led.py", line 37, in <module>
    sensitivity = [0.5]*len(models)
NameError: name 'models' is not defined
pi@aipi:~/smart/snowboy $ sudo vi demo2.py 
pi@aipi:~/smart/snowboy $ sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
/home/pi/smart/snowboy/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
^Cpi@aipi:~/smart/snowboy $ sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
Traceback (most recent call last):
  File "wake2_led.py", line 7, in <module>
    import GPIO
ImportError: No module named GPIO
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake2_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_led.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc   wake_temp.py
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo vi wake_temp.py
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake2_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_led.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc   wake_temp.py
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo vi bme.py
pi@aipi:~/smart/snowboy $ sudo vi wake_temp.py
pi@aipi:~/smart/snowboy $ sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:26:55
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:26:57
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:27:01
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:27:08
^Cpi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake2_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_led.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc   wake_temp.py
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:28:18
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:28:21
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:28:24
^Cpi@aipi:~/smart/snowboy sudo vi wake2_led.py 
pi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:28:55
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:29:05
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:29:07
^Cpi@aipi:~/smart/snowboy $ python wake_led.py resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
/home/pi/smart/snowboy/light.py:8: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(self.port, GPIO.OUT)
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:29:41
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:29:43
^Cpi@aipi:~/smart/snowboy $ python wake2_led.py resources/snowboy.umdl resources/oheya.pmdl 
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.front.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM front
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.rear
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.center_lfe
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.side
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround21
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround40.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround40
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround41
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround50
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround51.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround51
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.surround71.0:CARD=0'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM surround71
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM iec958
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'cards.bcm2835_alsa.pcm.iec958.0:CARD=0,AES0=4,AES1=130,AES2=0,AES3=2'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:5007:(snd_config_expand) Evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM spdif
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.hdmi
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.modem
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM cards.pcm.phoneline
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
ALSA lib confmisc.c:1281:(snd_func_refer) Unable to find definition 'defaults.bluealsa.device'
ALSA lib conf.c:4528:(_snd_config_evaluate) function snd_func_refer returned error: No such file or directory
ALSA lib conf.c:4996:(snd_config_expand) Args evaluate error: No such file or directory
ALSA lib pcm.c:2495:(snd_pcm_open_noupdate) Unknown PCM bluealsa
Cannot connect to server socket err = No such file or directory
Cannot connect to server request channel
jack server is not running or cannot be started
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
JackShmReadWritePtr::~JackShmReadWritePtr - Init not done for -1, skipping unlock
ウェイクワードを発話して下さい。Ctrl+Cで終了します。
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:30:55
INFO:snowboy:Keyword 1 detected at time: 2019-01-05 13:30:57
INFO:snowboy:Keyword 2 detected at time: 2019-01-05 13:30:59
^Cpi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake2_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_led.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc   wake_temp.py
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake.py
pi@aipi:~/smart/snowboy $ sudo mv wake.py arc/
pi@aipi:~/smart/snowboy $ sudo shutdown now
Connection to aipi.local closed by remote host.
Connection to aipi.local closed.
KMBP:Downloads ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Jan  5 17:17:10 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  smart
pi@aipi:~ $ cd smart
pi@aipi:~/smart $ ls
BME280  aquestalkpi  bme280.py   parse_pulse.rb  pixelfull.py  remotetv.lircd.conf  sony.lircd.conf  tv
air     blinka.py    bme_led.py  pixel.py        raspi3        snowboy              test.wav
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake2_led.py
pi@aipi:~/smart/snowboy $ sudo vi wake_led.py 
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake2_led.py
pi@aipi:~/smart/snowboy $ sudo vi bme.py
pi@aipi:~/smart/snowboy $ sudo vi bme.py
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake2_led.py
pi@aipi:~/smart/snowboy $ ls
README.md          bme.pyc          light.pyc                           snowboydecoder.pyc  wake_led.py
__pycache__        demo.py          requirements.txt                    snowboydetect.py    wake_temp.py
_snowboydetect.so  demo2.py         resources                           snowboydetect.pyc
arc                demo_arecord.py  rpi-arm-raspbian-8.0-1.1.1.tar.bz2  version
bme.py             light.py         snowboydecoder.py                   wake2_led.py
pi@aipi:~/smart/snowboy $ sudo vi wake_temp.py 

import snowboydecoder
import sys
import signal

# Demo code for listening two hotwords at the same time

interrupted = False

import bme

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

if len(sys.argv) != 3:
    print("Error: need to specify 2 model names")
    print("Usage: python demo.py 1st.model 2nd.model")
    sys.exit(-1)

models = sys.argv[1:]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

sensitivity = [0.5]*len(models)
detector = snowboydecoder.HotwordDetector(models, sensitivity=sensitivity)
callbacks = [lambda: bme.temp_led(), #snowboydecoder.play_audio_file(snowboydecoder.DETECT_DING),
             lambda: snowboydecoder.play_audio_file(snowboydecoder.DETECT_DONG)]
print('Listening... Press Ctrl+C to exit')

# main loop
# make sure you have the same numbers of callbacks and models
detector.start(detected_callback=callbacks,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()
