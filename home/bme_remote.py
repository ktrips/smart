Last login: Mon Feb  4 01:46:43 on ttys000
KMBP:~ ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb  5 01:17:10 2019
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1      julius_greeting.sh   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py      julius_ir_remote.py  light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_greeting.py  julius_start.sh      light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 986

Error: failed to bind socket
^Cpi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 1000

d = 2019-02-05 01:32:11.994543 
おはよう
おはようございます！今は2019年2月5日1時32分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.23  ℃
pressure : 1015.53 hPa
hum :  40.96 ％
今の室温は、24.2度、湿度は、41.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013231.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:33:13.774884 
おはよう
おはようございます！今は2019年2月5日1時33分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.26  ℃
pressure : 1015.58 hPa
hum :  40.66 ％
今の室温は、24.3度、湿度は、40.7パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013332.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:34:07.930316 
おはよう
おはようございます！今は2019年2月5日1時34分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.18  ℃
pressure : 1015.55 hPa
hum :  40.63 ％
今の室温は、24.2度、湿度は、40.6パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013426.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:35:23.377822 
おはよう
おはようございます！今は2019年2月5日1時35分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 23.95  ℃
pressure : 1015.62 hPa
hum :  41.86 ％
今の室温は、23.9度、湿度は、41.9パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013542.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:35:54.899265 
さようなら
No word detected
d = 2019-02-05 01:35:54.899991 
さようなら
No word detected
d = 2019-02-05 01:35:54.901024 
さようなら
No word detected
d = 2019-02-05 01:35:54.901663 
さようなら
No word detected
d = 2019-02-05 01:35:54.902254 
さようなら
No word detected
d = 2019-02-05 01:35:54.903038 
さようなら
No word detected
d = 2019-02-05 01:36:00.797293 
ただいま
おかえりなさい！おつかれさまでした！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 23.82  ℃
pressure : 1015.63 hPa
hum :  39.97 ％
今の室温は、23.8度、湿度は、40.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013616.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
d = 2019-02-05 01:36:29.138990 
さようなら
No word detected
d = 2019-02-05 01:36:29.139691 
さようなら
No word detected
d = 2019-02-05 01:36:29.140619 
さようなら
No word detected
d = 2019-02-05 01:36:29.141189 
さようなら
No word detected
d = 2019-02-05 01:36:29.141746 
さようなら
No word detected
^Cpi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ sudo apt-get install chkconfig
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下の追加パッケージがインストールされます:
  insserv
提案パッケージ:
  bootchart2
以下のパッケージが新たにインストールされます:
  chkconfig insserv
アップグレード: 0 個、新規インストール: 2 個、削除: 0 個、保留: 67 個。
67.5 kB のアーカイブを取得する必要があります。
この操作後に追加で 196 kB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf chkconfig all 11.4.54.60.1debian1 [9,766 B]
取得:2 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf insserv armhf 1.14.0-5.4 [57.7 kB]
67.5 kB を 1秒 で取得しました (42.6 kB/s)
以前に未選択のパッケージ chkconfig を選択しています。
(データベースを読み込んでいます ... 現在 135313 個のファイルとディレクトリがインストールされています。)
.../chkconfig_11.4.54.60.1debian1_all.deb を展開する準備をしています ...
chkconfig (11.4.54.60.1debian1) を展開しています...
以前に未選択のパッケージ insserv を選択しています。
.../insserv_1.14.0-5.4_armhf.deb を展開する準備をしています ...
insserv (1.14.0-5.4) を展開しています...
chkconfig (11.4.54.60.1debian1) を設定しています ...
man-db (2.7.6.1-2) のトリガを処理しています ...
insserv (1.14.0-5.4) を設定しています ...
pi@aipi:~/smart $ sudo /etc/init.d/cron start
[ ok ] Starting cron (via systemctl): cron.service.
pi@aipi:~/smart $ sudo chkconfig cron
cron  on
pi@aipi:~/smart $ crontab -e
no crontab for pi - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/ed
  2. /bin/nano        <---- easiest
  3. /usr/bin/vim.tiny

Choose 1-3 [2]: 2
crontab: installing new crontab
pi@aipi:~/smart $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 10 * * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:~/smart $ crontab -e
crontab: installing new crontab
pi@aipi:~/smart $ 
pi@aipi:~/smart $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 01 47 * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:~/smart $ sudo vi /etc/log/rsyslog.conf
pi@aipi:~/smart $ cd /etc/l
ld.so.conf.d/ ldap/         libnl-3/      libpaper.d/   libreoffice/  lightdm/      lighttpd/     lirc/         logcheck/     logrotate.d/  
pi@aipi:~/smart $ cd /etc/logcheck/
pi@aipi:/etc/logcheck $ ls
ignore.d.server
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
Display all 205 possibilities? (y or n)
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
pi@aipi:/etc/logcheck $ sudo vi /etc/sys
sysctl.conf  sysctl.d/    systemd/     
pi@aipi:/etc/logcheck $ sudo vi /etc/s
samba/                     sensors3.conf              skel/                      subuid                     systemd/
securetty                  services                   ssh/                       sudoers                    
security/                  sgml/                      ssl/                       sudoers.d/                 
selinux/                   shadow                     staff-group-for-usr-local  sysctl.conf                
sensors.d/                 shells                     subgid                     sysctl.d/                  
pi@aipi:/etc/logcheck $ sudo vi /etc/rsyslog.
rsyslog.conf  rsyslog.d/    
pi@aipi:/etc/logcheck $ sudo vi /etc/rsyslog.conf
pi@aipi:/etc/logcheck $ sudo /etc/init.d/rsyslog restart
[ ok ] Restarting rsyslog (via systemctl): rsyslog.service.
pi@aipi:/etc/logcheck $ crontab -e
crontab: installing new crontab
pi@aipi:/etc/logcheck $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 2 * * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:/etc/logcheck $ sudo cat /var/log/cron.log
Feb  5 01:52:06 aipi crontab[17811]: (pi) BEGIN EDIT (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) REPLACE (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) END EDIT (pi)
Feb  5 01:52:52 aipi crontab[17839]: (pi) LIST (pi)
Feb  5 01:53:01 aipi cron[312]: (pi) RELOAD (crontabs/pi)
pi@aipi:/etc/logcheck $ sudo vi /var/log/cron.log
pi@aipi:/etc/logcheck $ sudo cat /var/log/cron.log
Feb  5 01:52:06 aipi crontab[17811]: (pi) BEGIN EDIT (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) REPLACE (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) END EDIT (pi)
Feb  5 01:52:52 aipi crontab[17839]: (pi) LIST (pi)
Feb  5 01:53:01 aipi cron[312]: (pi) RELOAD (crontabs/pi)
Feb  5 02:00:01 aipi CRON[17987]: (pi) CMD (python /home/pi/smart/camera_line.py)
Feb  5 02:00:09 aipi CRON[17983]: (CRON) info (No MTA installed, discarding output)
pi@aipi:/etc/logcheck $ crontab -e
crontab: installing new crontab
pi@aipi:/etc/logcheck $ packet_write_wait: Connection to 240f:3a:2015:1:f744:f2fb:54b7:6641 port 22: Broken pipe
KMBP:~ ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb  5 08:04:19 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  arc  image.jpg  smart  tensor
pi@aipi:~ $ cd
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ lks
-bash: lks: コマンドが見つかりません
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1      julius_greeting.sh   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py      julius_ir_remote.py  light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_greeting.py  julius_start.sh      light.pyc        snowboy              test.wav
pi@aipi:~/smart $ sudo cp juliusd.service juliusautod.service
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo cp julius_start.sh julius_auto.sh
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo vi julius_auto.sh
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo mv juliusd.service julius_start.sh arc/
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusautod.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py             remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc            snowboy              test.wav
pi@aipi:~/smart $ sudo mv juliusautod.service juliusd.service
pi@aipi:~/smart $ sudo vi julius
pi@aipi:~/smart $ sudo vi julius
julius-4.4.2.1/      julius_auto.py       julius_auto.sh       julius_greeting.py   julius_greeting.sh   julius_ir_remote.py  juliusd.service
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo cp juliusd.service /etc/systemd/system/
pi@aipi:~/smart $ sudo systemctl enable juliud
Failed to enable unit: File juliud.service: No such file or directory
pi@aipi:~/smart $ sudo systemctl enable juliusd
Created symlink /etc/systemd/system/multi-user.target.wants/juliusd.service → /etc/systemd/system/juliusd.service.
pi@aipi:~/smart $ sudo systemctl start juliusd
Failed to start juliusd.service: Unit juliusd.service is not loaded properly: Invalid argument.
See system logs and 'systemctl status juliusd.service' for details.
pi@aipi:~/smart $ sudo systemctl status juliusd
● juliusd.service - JuliusAuto
   Loaded: error (Reason: Invalid argument)
   Active: inactive (dead)

 2月 06 00:08:11 aipi systemd[1]: [/etc/systemd/system/juliusd.service:8] Executable path is not absolute, ignoring: pyton julius_auto.py
 2月 06 00:08:11 aipi systemd[1]: juliusd.service: Service lacks both ExecStart= and ExecStop= setting. Refusing.
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo systemctl enable juliusd
pi@aipi:~/smart $ sudo cp juliusd.service /etc/systemd/system/
pi@aipi:~/smart $ sudo systemctl enable juliusd
pi@aipi:~/smart $ sudo systemctl start juliusd
pi@aipi:~/smart $ sudo systemctl status juliusd
● juliusd.service - JuliusAuto
   Loaded: loaded (/etc/systemd/system/juliusd.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-02-06 00:11:00 JST; 4s ago
 Main PID: 14341 (python)
   CGroup: /system.slice/juliusd.service
           └─14341 /usr/bin/python /home/pi/smart/julius_auto.py

 2月 06 00:11:00 aipi systemd[1]: Started JuliusAuto.
pi@aipi:~/smart $ ps aux | grep julius
root     14341 91.0  0.9  12056  8608 ?        Rs   00:10   0:30 /usr/bin/python /home/pi/smart/julius_auto.py
pi       14374  0.0  0.0   3852   532 pts/0    S+   00:11   0:00 grep --color=auto julius
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ sudo cp camera_line.py snowboy/
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          bme.py          demo2.py         getTensor.py        julius_greeting.sh  resources           snowboydetect.pyc  wake_led.py
__pycache__        bme.pyc         demo_arecord.py  image.jpg           light.py            snowboydecoder.py   version            wake_oheya.py
_snowboydetect.so  camera_line.py  faceTensor.py    julius_auto.py      light.pyc           snowboydecoder.pyc  wake2_led.py       wake_temp.py
arc                demo.py         faceTensor.pyc   julius_greeting.py  requirements.txt    snowboydetect.py    wake2_tensor.py
pi@aipi:~/smart/snowboy $ sudo cp wake_oheya.py 
cp: 'wake_oheya.py' の後に宛先のファイルオペランドがありません
Try 'cp --help' for more information.
pi@aipi:~/smart/snowboy $ sudo cp wake_oheya.py wake2_remote.py
pi@aipi:~/smart/snowboy $ sudo vi wake2_remote.py 
pi@aipi:~/smart/snowboy $ python3 wake2_remote.py 
Traceback (most recent call last):
  File "wake2_remote.py", line 1, in <module>
    import snowboydecoder
  File "/home/pi/smart/snowboy/snowboydecoder.py", line 5, in <module>
    import snowboydetect
  File "/home/pi/smart/snowboy/snowboydetect.py", line 28, in <module>
    _snowboydetect = swig_import_helper()
  File "/home/pi/smart/snowboy/snowboydetect.py", line 24, in swig_import_helper
    _mod = imp.load_module('_snowboydetect', fp, pathname, description)
  File "/usr/lib/python3.5/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.5/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: dynamic module does not define module export function (PyInit__snowboydetect)
pi@aipi:~/smart/snowboy $ python wake2_remote.py 
Error: need to specify 2 model names
Usage: python demo.py 1st.model 2nd.model
pi@aipi:~/smart/snowboy $ python wake2_remote.py resources/snowboy.umdl resources/oheya.pmdl 
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
INFO:snowboy:Keyword 1 detected at time: 2019-02-06 00:17:52
/home/pi/smart/image/20190206/001752.jpg
{"status":200,"message":"ok"}
INFO:snowboy:Keyword 2 detected at time: 2019-02-06 00:17:59
temp : 22.60  ℃
pressure : 1020.76 hPa
hum :  48.26 ％
今の室温は、22.6度、湿度は、48.3パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
快適です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
^Cpi@aipi:~/smart/snowboy $ cd ..
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 14612

^Cpi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python camera_line.py 
Date dir already exists
/home/pi/smart/image/20190206/005235.jpg
{"status":200,"message":"ok"}
pi@aipi:~/smart $ exit
ログアウト
Connection to aipi.local closed.
KMBP:~ ktrips$ ssh pi@aipi.local
Warning: Permanently added the ECDSA host key for IP address '192.168.0.3' to the list of known hosts.
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Feb  6 08:17:10 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  arc  image.jpg  smart  tensor
pi@aipi:~ $ cd smart
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235051.jpg
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
  File "camera.py", line 24
    　　print(fname)
    ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235408.jpg
Traceback (most recent call last):
  File "camera.py", line 30, in <module>
    main()
  File "camera.py", line 27, in main
    line(fname)
NameError: global name 'line' is not defined
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235445.jpg
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235532.jpg
pi@aipi:~/smart $ sudo vi camera_line.py 
pi@aipi:~/smart $ sudo vi camera_line.py 
pi@aipi:~/smart $ sudo cp julius_auto.py julius_remote.py
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 83
    command = [‘tv’, 'tvon']
               ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 84
    elif u’加湿器オン’ in word:
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 84
    elif u’加湿器オン' in word:
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 10655

d = 2019-02-07 00:08:38.022401 
おはよう
おはようございます！今は2019年2月7日0時8分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 22.27  ℃
pressure : 1011.68 hPa
hum :  45.38 ％
今の室温は、22.3度、湿度は、45.4パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
/home/pi/smart/image/20190207/000858.jpg
^[{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
^[^Cpi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 10770

^Cpi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   julius_remote.py  light.pyc            snowboy         test.wav
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   juliusd.service   remote.lircd.conf    stv.lircd.conf
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.py          remotetv.lircd.conf  tensor
pi@aipi:~/smart $ sudo cp bme.py bme_remote.py
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
  File "bme_remote.py", line 172
    def temp_led:
                ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 22.36  ℃
pressure : 1011.99 hPa
hum :  44.51 ％
今の室温は、22.4度、湿度は、44.5パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
Traceback (most recent call last):
  File "bme_remote.py", line 215, in <module>
    temp_remote()
  File "bme_remote.py", line 211, in temp_remote
    subprocess.Popen(args)
NameError: global name 'subprocess' is not defined
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 22.01  ℃
pressure : 1012.07 hPa
hum :  44.78 ％
今の室温は、22.0度、湿度は、44.8パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 21.93  ℃
pressure : 1012.04 hPa
hum :  44.97 ％
今の室温は、21.9度、湿度は、45.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
pi@aipi:~/smart $ sudo vi bme_remote.py 

# -*- coding: utf-8 -*-
from smbus2 import SMBus
import time
import os
import subprocess

bus_number  = 1
i2c_address = 0x76

import RPi.GPIO as GPIO

from light import Light
interrupted = False
GPIO.setwarnings(False)

bus = SMBus(bus_number)

digT = []
digP = []
digH = []

t_fine = 0.0

aquest_dir = "/home/pi/smart/aquestalkpi/"

def writeReg(reg_address, data):
        bus.write_byte_data(i2c_address,reg_address,data)

def get_calib_param():
        calib = []

        for i in range (0x88,0x88+24):
                calib.append(bus.read_byte_data(i2c_address,i))
        calib.append(bus.read_byte_data(i2c_address,0xA1))
        for i in range (0xE1,0xE1+7):
                calib.append(bus.read_byte_data(i2c_address,i))

        digT.append((calib[1] << 8) | calib[0])
        digT.append((calib[3] << 8) | calib[2])
        digT.append((calib[5] << 8) | calib[4])
        digP.append((calib[7] << 8) | calib[6])
        digP.append((calib[9] << 8) | calib[8])
        digP.append((calib[11]<< 8) | calib[10])
        digP.append((calib[13]<< 8) | calib[12])
        digP.append((calib[15]<< 8) | calib[14])
        digP.append((calib[17]<< 8) | calib[16])
        digP.append((calib[19]<< 8) | calib[18])
        digP.append((calib[21]<< 8) | calib[20])
        digP.append((calib[23]<< 8) | calib[22])
        digH.append( calib[24] )
        digH.append((calib[26]<< 8) | calib[25])
        digH.append( calib[27] )
        digH.append((calib[28]<< 4) | (0x0F & calib[29]))
        digH.append((calib[30]<< 4) | ((calib[29] >> 4) & 0x0F))
        digH.append( calib[31] )

        for i in range(1,2):
                if digT[i] & 0x8000:
                        digT[i] = (-digT[i] ^ 0xFFFF) + 1

        for i in range(1,8):
                if digP[i] & 0x8000:
                        digP[i] = (-digP[i] ^ 0xFFFF) + 1

        for i in range(0,6):
                if digH[i] & 0x8000:
                        digH[i] = (-digH[i] ^ 0xFFFF) + 1

Last login: Mon Feb  4 01:46:43 on ttys000
KMBP:~ ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb  5 01:17:10 2019
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1      julius_greeting.sh   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py      julius_ir_remote.py  light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_greeting.py  julius_start.sh      light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 986

Error: failed to bind socket
^Cpi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 1000

d = 2019-02-05 01:32:11.994543 
おはよう
おはようございます！今は2019年2月5日1時32分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.23  ℃
pressure : 1015.53 hPa
hum :  40.96 ％
今の室温は、24.2度、湿度は、41.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013231.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:33:13.774884 
おはよう
おはようございます！今は2019年2月5日1時33分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.26  ℃
pressure : 1015.58 hPa
hum :  40.66 ％
今の室温は、24.3度、湿度は、40.7パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013332.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:34:07.930316 
おはよう
おはようございます！今は2019年2月5日1時34分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 24.18  ℃
pressure : 1015.55 hPa
hum :  40.63 ％
今の室温は、24.2度、湿度は、40.6パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013426.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:35:23.377822 
おはよう
おはようございます！今は2019年2月5日1時35分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 23.95  ℃
pressure : 1015.62 hPa
hum :  41.86 ％
今の室温は、23.9度、湿度は、41.9パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013542.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
d = 2019-02-05 01:35:54.899265 
さようなら
No word detected
d = 2019-02-05 01:35:54.899991 
さようなら
No word detected
d = 2019-02-05 01:35:54.901024 
さようなら
No word detected
d = 2019-02-05 01:35:54.901663 
さようなら
No word detected
d = 2019-02-05 01:35:54.902254 
さようなら
No word detected
d = 2019-02-05 01:35:54.903038 
さようなら
No word detected
d = 2019-02-05 01:36:00.797293 
ただいま
おかえりなさい！おつかれさまでした！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 23.82  ℃
pressure : 1015.63 hPa
hum :  39.97 ％
今の室温は、23.8度、湿度は、40.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Date dir already exists
/home/pi/smart/image/20190205/013616.jpg
{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
d = 2019-02-05 01:36:29.138990 
さようなら
No word detected
d = 2019-02-05 01:36:29.139691 
さようなら
No word detected
d = 2019-02-05 01:36:29.140619 
さようなら
No word detected
d = 2019-02-05 01:36:29.141189 
さようなら
No word detected
d = 2019-02-05 01:36:29.141746 
さようなら
No word detected
^Cpi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ ^C
pi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ sudo apt-get install chkconfig
パッケージリストを読み込んでいます... 完了
依存関係ツリーを作成しています                
状態情報を読み取っています... 完了
以下の追加パッケージがインストールされます:
  insserv
提案パッケージ:
  bootchart2
以下のパッケージが新たにインストールされます:
  chkconfig insserv
アップグレード: 0 個、新規インストール: 2 個、削除: 0 個、保留: 67 個。
67.5 kB のアーカイブを取得する必要があります。
この操作後に追加で 196 kB のディスク容量が消費されます。
続行しますか? [Y/n] Y
取得:1 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf chkconfig all 11.4.54.60.1debian1 [9,766 B]
取得:2 http://ftp.jaist.ac.jp/pub/Linux/raspbian-archive/raspbian stretch/main armhf insserv armhf 1.14.0-5.4 [57.7 kB]
67.5 kB を 1秒 で取得しました (42.6 kB/s)
以前に未選択のパッケージ chkconfig を選択しています。
(データベースを読み込んでいます ... 現在 135313 個のファイルとディレクトリがインストールされています。)
.../chkconfig_11.4.54.60.1debian1_all.deb を展開する準備をしています ...
chkconfig (11.4.54.60.1debian1) を展開しています...
以前に未選択のパッケージ insserv を選択しています。
.../insserv_1.14.0-5.4_armhf.deb を展開する準備をしています ...
insserv (1.14.0-5.4) を展開しています...
chkconfig (11.4.54.60.1debian1) を設定しています ...
man-db (2.7.6.1-2) のトリガを処理しています ...
insserv (1.14.0-5.4) を設定しています ...
pi@aipi:~/smart $ sudo /etc/init.d/cron start
[ ok ] Starting cron (via systemctl): cron.service.
pi@aipi:~/smart $ sudo chkconfig cron
cron  on
pi@aipi:~/smart $ crontab -e
no crontab for pi - using an empty one

Select an editor.  To change later, run 'select-editor'.
  1. /bin/ed
  2. /bin/nano        <---- easiest
  3. /usr/bin/vim.tiny

Choose 1-3 [2]: 2
crontab: installing new crontab
pi@aipi:~/smart $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 10 * * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:~/smart $ crontab -e
crontab: installing new crontab
pi@aipi:~/smart $ 
pi@aipi:~/smart $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 01 47 * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:~/smart $ sudo vi /etc/log/rsyslog.conf
pi@aipi:~/smart $ cd /etc/l
ld.so.conf.d/ ldap/         libnl-3/      libpaper.d/   libreoffice/  lightdm/      lighttpd/     lirc/         logcheck/     logrotate.d/  
pi@aipi:~/smart $ cd /etc/logcheck/
pi@aipi:/etc/logcheck $ ls
ignore.d.server
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
Display all 205 possibilities? (y or n)
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
pi@aipi:/etc/logcheck $ sudo vi /etc/syslog.conf
pi@aipi:/etc/logcheck $ sudo vi /etc/sys
sysctl.conf  sysctl.d/    systemd/     
pi@aipi:/etc/logcheck $ sudo vi /etc/s
samba/                     sensors3.conf              skel/                      subuid                     systemd/
securetty                  services                   ssh/                       sudoers                    
security/                  sgml/                      ssl/                       sudoers.d/                 
selinux/                   shadow                     staff-group-for-usr-local  sysctl.conf                
sensors.d/                 shells                     subgid                     sysctl.d/                  
pi@aipi:/etc/logcheck $ sudo vi /etc/rsyslog.
rsyslog.conf  rsyslog.d/    
pi@aipi:/etc/logcheck $ sudo vi /etc/rsyslog.conf
pi@aipi:/etc/logcheck $ sudo /etc/init.d/rsyslog restart
[ ok ] Restarting rsyslog (via systemctl): rsyslog.service.
pi@aipi:/etc/logcheck $ crontab -e
crontab: installing new crontab
pi@aipi:/etc/logcheck $ crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command

00 2 * * * python /home/pi/smart/camera_line.py
00 15 * * * python /home/pi/smart/camera_line.py

pi@aipi:/etc/logcheck $ sudo cat /var/log/cron.log
Feb  5 01:52:06 aipi crontab[17811]: (pi) BEGIN EDIT (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) REPLACE (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) END EDIT (pi)
Feb  5 01:52:52 aipi crontab[17839]: (pi) LIST (pi)
Feb  5 01:53:01 aipi cron[312]: (pi) RELOAD (crontabs/pi)
pi@aipi:/etc/logcheck $ sudo vi /var/log/cron.log
pi@aipi:/etc/logcheck $ sudo cat /var/log/cron.log
Feb  5 01:52:06 aipi crontab[17811]: (pi) BEGIN EDIT (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) REPLACE (pi)
Feb  5 01:52:46 aipi crontab[17811]: (pi) END EDIT (pi)
Feb  5 01:52:52 aipi crontab[17839]: (pi) LIST (pi)
Feb  5 01:53:01 aipi cron[312]: (pi) RELOAD (crontabs/pi)
Feb  5 02:00:01 aipi CRON[17987]: (pi) CMD (python /home/pi/smart/camera_line.py)
Feb  5 02:00:09 aipi CRON[17983]: (CRON) info (No MTA installed, discarding output)
pi@aipi:/etc/logcheck $ crontab -e
crontab: installing new crontab
pi@aipi:/etc/logcheck $ packet_write_wait: Connection to 240f:3a:2015:1:f744:f2fb:54b7:6641 port 22: Broken pipe
KMBP:~ ktrips$ ssh pi@aipi.local
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Tue Feb  5 08:04:19 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  arc  image.jpg  smart  tensor
pi@aipi:~ $ cd
pi@aipi:~ $ cd smart/
pi@aipi:~/smart $ lks
-bash: lks: コマンドが見つかりません
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1      julius_greeting.sh   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py      julius_ir_remote.py  light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_greeting.py  julius_start.sh      light.pyc        snowboy              test.wav
pi@aipi:~/smart $ sudo cp juliusd.service juliusautod.service
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo cp julius_start.sh julius_auto.sh
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo vi julius_auto.sh
pi@aipi:~/smart $ sudo vi juliusautod.service 
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo mv juliusd.service julius_start.sh arc/
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusautod.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py             remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc            snowboy              test.wav
pi@aipi:~/smart $ sudo mv juliusautod.service juliusd.service
pi@aipi:~/smart $ sudo vi julius
pi@aipi:~/smart $ sudo vi julius
julius-4.4.2.1/      julius_auto.py       julius_auto.sh       julius_greeting.py   julius_greeting.sh   julius_ir_remote.py  juliusd.service
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo cp juliusd.service /etc/systemd/system/
pi@aipi:~/smart $ sudo systemctl enable juliud
Failed to enable unit: File juliud.service: No such file or directory
pi@aipi:~/smart $ sudo systemctl enable juliusd
Created symlink /etc/systemd/system/multi-user.target.wants/juliusd.service → /etc/systemd/system/juliusd.service.
pi@aipi:~/smart $ sudo systemctl start juliusd
Failed to start juliusd.service: Unit juliusd.service is not loaded properly: Invalid argument.
See system logs and 'systemctl status juliusd.service' for details.
pi@aipi:~/smart $ sudo systemctl status juliusd
● juliusd.service - JuliusAuto
   Loaded: error (Reason: Invalid argument)
   Active: inactive (dead)

 2月 06 00:08:11 aipi systemd[1]: [/etc/systemd/system/juliusd.service:8] Executable path is not absolute, ignoring: pyton julius_auto.py
 2月 06 00:08:11 aipi systemd[1]: juliusd.service: Service lacks both ExecStart= and ExecStop= setting. Refusing.
pi@aipi:~/smart $ sudo vi juliusd.service 
pi@aipi:~/smart $ sudo systemctl enable juliusd
pi@aipi:~/smart $ sudo cp juliusd.service /etc/systemd/system/
pi@aipi:~/smart $ sudo systemctl enable juliusd
pi@aipi:~/smart $ sudo systemctl start juliusd
pi@aipi:~/smart $ sudo systemctl status juliusd
● juliusd.service - JuliusAuto
   Loaded: loaded (/etc/systemd/system/juliusd.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-02-06 00:11:00 JST; 4s ago
 Main PID: 14341 (python)
   CGroup: /system.slice/juliusd.service
           └─14341 /usr/bin/python /home/pi/smart/julius_auto.py

 2月 06 00:11:00 aipi systemd[1]: Started JuliusAuto.
pi@aipi:~/smart $ ps aux | grep julius
root     14341 91.0  0.9  12056  8608 ?        Rs   00:10   0:30 /usr/bin/python /home/pi/smart/julius_auto.py
pi       14374  0.0  0.0   3852   532 pts/0    S+   00:11   0:00 grep --color=auto julius
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ sudo cp camera_line.py snowboy/
pi@aipi:~/smart $ cd snowboy/
pi@aipi:~/smart/snowboy $ ls
README.md          bme.py          demo2.py         getTensor.py        julius_greeting.sh  resources           snowboydetect.pyc  wake_led.py
__pycache__        bme.pyc         demo_arecord.py  image.jpg           light.py            snowboydecoder.py   version            wake_oheya.py
_snowboydetect.so  camera_line.py  faceTensor.py    julius_auto.py      light.pyc           snowboydecoder.pyc  wake2_led.py       wake_temp.py
arc                demo.py         faceTensor.pyc   julius_greeting.py  requirements.txt    snowboydetect.py    wake2_tensor.py
pi@aipi:~/smart/snowboy $ sudo cp wake_oheya.py 
cp: 'wake_oheya.py' の後に宛先のファイルオペランドがありません
Try 'cp --help' for more information.
pi@aipi:~/smart/snowboy $ sudo cp wake_oheya.py wake2_remote.py
pi@aipi:~/smart/snowboy $ sudo vi wake2_remote.py 
pi@aipi:~/smart/snowboy $ python3 wake2_remote.py 
Traceback (most recent call last):
  File "wake2_remote.py", line 1, in <module>
    import snowboydecoder
  File "/home/pi/smart/snowboy/snowboydecoder.py", line 5, in <module>
    import snowboydetect
  File "/home/pi/smart/snowboy/snowboydetect.py", line 28, in <module>
    _snowboydetect = swig_import_helper()
  File "/home/pi/smart/snowboy/snowboydetect.py", line 24, in swig_import_helper
    _mod = imp.load_module('_snowboydetect', fp, pathname, description)
  File "/usr/lib/python3.5/imp.py", line 242, in load_module
    return load_dynamic(name, filename, file)
  File "/usr/lib/python3.5/imp.py", line 342, in load_dynamic
    return _load(spec)
ImportError: dynamic module does not define module export function (PyInit__snowboydetect)
pi@aipi:~/smart/snowboy $ python wake2_remote.py 
Error: need to specify 2 model names
Usage: python demo.py 1st.model 2nd.model
pi@aipi:~/smart/snowboy $ python wake2_remote.py resources/snowboy.umdl resources/oheya.pmdl 
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
INFO:snowboy:Keyword 1 detected at time: 2019-02-06 00:17:52
/home/pi/smart/image/20190206/001752.jpg
{"status":200,"message":"ok"}
INFO:snowboy:Keyword 2 detected at time: 2019-02-06 00:17:59
temp : 22.60  ℃
pressure : 1020.76 hPa
hum :  48.26 ％
今の室温は、22.6度、湿度は、48.3パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
快適です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
^Cpi@aipi:~/smart/snowboy $ cd ..
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python julius_auto.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 14612

^Cpi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python camera_line.py 
Date dir already exists
/home/pi/smart/image/20190206/005235.jpg
{"status":200,"message":"ok"}
pi@aipi:~/smart $ exit
ログアウト
Connection to aipi.local closed.
KMBP:~ ktrips$ ssh pi@aipi.local
Warning: Permanently added the ECDSA host key for IP address '192.168.0.3' to the list of known hosts.
pi@aipi.local's password: 
Linux aipi 4.14.79-v7+ #1159 SMP Sun Nov 4 17:50:20 GMT 2018 armv7l

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Wed Feb  6 08:17:10 2019
pi@aipi:~ $ ls
Desktop  Documents  Downloads  MagPi  Music  Pictures  Public  Templates  Videos  arc  image.jpg  smart  tensor
pi@aipi:~ $ cd smart
pi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   juliusd.service  remote.lircd.conf    stv.lircd.conf
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   light.py         remotetv.lircd.conf  tensor
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.pyc        snowboy              test.wav
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235051.jpg
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
  File "camera.py", line 24
    　　print(fname)
    ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235408.jpg
Traceback (most recent call last):
  File "camera.py", line 30, in <module>
    main()
  File "camera.py", line 27, in main
    line(fname)
NameError: global name 'line' is not defined
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235445.jpg
pi@aipi:~/smart $ sudo vi camera.py 
pi@aipi:~/smart $ python camera.py
Date dir already exists
/home/pi/smart/image/20190206/235532.jpg
pi@aipi:~/smart $ sudo vi camera_line.py 
pi@aipi:~/smart $ sudo vi camera_line.py 
pi@aipi:~/smart $ sudo cp julius_auto.py julius_remote.py
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 83
    command = [‘tv’, 'tvon']
               ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 84
    elif u’加湿器オン’ in word:
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
  File "julius_remote.py", line 84
    elif u’加湿器オン' in word:
          ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 10655

d = 2019-02-07 00:08:38.022401 
おはよう
おはようございます！今は2019年2月7日0時8分です！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
temp : 22.27  ℃
pressure : 1011.68 hPa
hum :  45.38 ％
今の室温は、22.3度、湿度は、45.4パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
/home/pi/smart/image/20190207/000858.jpg
^[{"status":200,"message":"ok"}
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['tv', 'tvon']
^[^Cpi@aipi:~/smart $ 
pi@aipi:~/smart $ 
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python julius_remote.py 
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
Julius runs with 10770

^Cpi@aipi:~/smart $ ls
BME280       arc        camera_line.py    julius-4.4.2.1  julius_greeting.py   julius_remote.py  light.pyc            snowboy         test.wav
__pycache__  bme.py     humid.lircd.conf  julius_auto.py  julius_greeting.sh   juliusd.service   remote.lircd.conf    stv.lircd.conf
aquestalkpi  camera.py  image             julius_auto.sh  julius_ir_remote.py  light.py          remotetv.lircd.conf  tensor
pi@aipi:~/smart $ sudo cp bme.py bme_remote.py
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
  File "bme_remote.py", line 172
    def temp_led:
                ^
SyntaxError: invalid syntax
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 22.36  ℃
pressure : 1011.99 hPa
hum :  44.51 ％
今の室温は、22.4度、湿度は、44.5パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
Traceback (most recent call last):
  File "bme_remote.py", line 215, in <module>
    temp_remote()
  File "bme_remote.py", line 211, in temp_remote
    subprocess.Popen(args)
NameError: global name 'subprocess' is not defined
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 22.01  ℃
pressure : 1012.07 hPa
hum :  44.78 ％
今の室温は、22.0度、湿度は、44.8パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
pi@aipi:~/smart $ sudo vi julius_remote.py 
pi@aipi:~/smart $ sudo vi bme_remote.py 
pi@aipi:~/smart $ python bme_remote.py 
temp : 21.93  ℃
pressure : 1012.04 hPa
hum :  44.97 ％
今の室温は、21.9度、湿度は、45.0パーセントです！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
乾燥してますね！
再生中 WAVE 'stdin' : Signed 16 bit Little Endian, レート 8000 Hz, モノラル
['humid', 'hon']
pi@aipi:~/smart $ sudo vi bme_remote.py 

def readData():
        data = []
        for i in range (0xF7, 0xF7+8):
                data.append(bus.read_byte_data(i2c_address,i))
        pres_raw = (data[0] << 12) | (data[1] << 4) | (data[2] >> 4)
        temp_raw = (data[3] << 12) | (data[4] << 4) | (data[5] >> 4)
        hum_raw  = (data[6] << 8)  |  data[7]

        temp = compensate_T(temp_raw)
        press= compensate_P(pres_raw)
        hum  = compensate_H(hum_raw)

        return temp, press, hum

def compensate_P(adc_P):
        global  t_fine
        pressure = 0.0

        v1 = (t_fine / 2.0) - 64000.0
        v2 = (((v1 / 4.0) * (v1 / 4.0)) / 2048) * digP[5]
        v2 = v2 + ((v1 * digP[4]) * 2.0)
        v2 = (v2 / 4.0) + (digP[3] * 65536.0)
        v1 = (((digP[2] * (((v1 / 4.0) * (v1 / 4.0)) / 8192)) / 8)  + ((digP[1] * v1) / 2.0)) / 262144
        v1 = ((32768 + v1) * digP[0]) / 32768

        if v1 == 0:
                return 0
        pressure = ((1048576 - adc_P) - (v2 / 4096)) * 3125
        if pressure < 0x80000000:
                pressure = (pressure * 2.0) / v1
        else:
                pressure = (pressure / v1) * 2
        v1 = (digP[8] * (((pressure / 8.0) * (pressure / 8.0)) / 8192.0)) / 4096
        v2 = ((pressure / 4.0) * digP[7]) / 8192.0
        pressure = pressure + ((v1 + v2 + digP[6]) / 16.0)

        print "pressure : %7.2f hPa" % (pressure/100)

        return pressure


def compensate_T(adc_T):
        global t_fine
        v1 = (adc_T / 16384.0 - digT[0] / 1024.0) * digT[1]
        v2 = (adc_T / 131072.0 - digT[0] / 8192.0) * (adc_T / 131072.0 - digT[0] / 8192.0) * digT[2]
        t_fine = v1 + v2
        temperature = t_fine / 5120.0
        print "temp : %-6.2f ℃" % (temperature)

        return temperature


def compensate_H(adc_H):
        global t_fine
        var_h = t_fine - 76800.0
        if var_h != 0:
                var_h = (adc_H - (digH[3] * 64.0 + digH[4]/16384.0 * var_h)) * (digH[1] / 65536.0 * (1.0 + digH[5] / 67108864.0 * var_h * (1.0 + digH[2] / 67108864.0 * var_h)))
        else:
                return 0
        var_h = var_h * (1.0 - digH[0] * var_h / 524288.0)
        if var_h > 100.0:
                var_h = 100.0
        elif var_h < 0.0:
                var_h = 0.0
        print "hum : %6.2f ％" % (var_h)

        return var_h

def setup():
        osrs_t = 1                      #Temperature oversampling x 1
        osrs_p = 1                      #Pressure oversampling x 1
        osrs_h = 1                      #Humidity oversampling x 1
        mode   = 3                      #Normal mode
        t_sb   = 5                      #Tstandby 1000ms
        filter = 0                      #Filter off
        spi3w_en = 0                    #3-wire SPI Disable

        ctrl_meas_reg = (osrs_t << 5) | (osrs_p << 2) | mode
        config_reg    = (t_sb << 5) | (filter << 2) | spi3w_en
        ctrl_hum_reg  = osrs_h

        writeReg(0xF2,ctrl_hum_reg)
        writeReg(0xF4,ctrl_meas_reg)
        writeReg(0xF5,config_reg)


setup()
get_calib_param()


def led_blink(color, count):
        if color == "red":
            led = Light(17)
        elif color == "green":
            led = Light(18)
        else:
            led = Light(17)
        for i in range(count):
            led.blink()
            time.sleep(1)


def temp_remote():
        try:
                temp, press, hum = readData()
        except KeyboardInterrupt:
                pass
        if temp:
            msg = "今の室温は、" + str(round(temp,1)) + "度、湿度は、" + str(round(hum,1)) + "パーセントです！"
            print msg
            os.system(aquest_dir + "AquesTalkPi " + msg + " | aplay")

        command = ["tv", "tvon"]
        if temp > 30:
            room = "暑くないですか？"
            command = ["air", "cool"]
            led_blink("red", 5)
        elif temp < 15:
            room = "寒いですね！"
            command = ["air", "warm"]
            led_blink("red", 4)
        elif hum > 70:
            room = "蒸し蒸ししますねー"
            command = ["air", "dry"]
            led_blink("red", 3)
        elif hum < 50:
            room = "乾燥してますね！"
            command = ["humid", "hon"]
            led_blink("red", 2)
        elif press < 1000:
            room = "低気圧ですね"
            led_blink("red", 1)
        else:
            room = "快適です！"
            led_blink("green", 3)

        if room:
            print room
            os.system(aquest_dir + "AquesTalkPi " + room + " | aplay")
            print command
            args = ['irsend', '-#', '1', 'SEND_ONCE', command[0], command[1]]
            subprocess.Popen(args)


if __name__ == '__main__':
    temp_remote()
  
