# voicekeyboard

#idea
device (rpi) with finerprint scanner and a microphone.
emulating a keybourd over usb where another computer is comnected
While finger is on scanner and print is confirmed:
    - listen on mikrofone
After Finger was released  
    - transfer sount to text
    - if text contens the word password query password app (1password) for a password
    - send passoword to connected computer as "keystrokes"
    - else 
    - any other text send to connected comupter as "keystrokes"


## inspired by
key-mime-pi:
https://mtlynch.io/key-mime-pi/
https://github.com/mtlynch/key-mime-pi.git

heise deepSpeech projects:
https://www.heise.de/hintergrund/Mozilla-DeepSpeech-Speech-to-Text-Schritt-fuer-Schritt-6048698.html
need this packages also before installing deepspeech:
sudo apt-get install python-dev libatlas-base-dev




## software used
1password commandline tool:
https://support.1password.com/command-line-getting-started/





## snippets
### playing and recording sound in Python
https://realpython.com/playing-and-recording-sound-python/

to instapp pyaudio in rpi:
https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone

