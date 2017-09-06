Recorder
===============================================================================

이 디렉토리는 [Google Speech recognition](https://github.com/CNUPiedPiper/HARU/blob/master/src/speech_recognition/transcribe_streaming.py) 에 사용자의 음성 raw 데이터를 넘겨주기 위해 녹음 기능을 제공하는 모듈입니다.

This directory contains recording voice raw data module Python Class that delivers to [Google Speech recognition](https://github.com/CNUPiedPiper/HARU/blob/master/src/speech_recognition/transcribe_streaming.py).<br><br>

## How to use
먼저 [get_dev_index.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/recorder/get_dev_index.py)를 통해 Raspberry PI의 Audio Device 정보를 가져와서 할당 가능한 Device number를 알아냅니다.

Before you use, get the assignable audio device number in your Raspberry PI with [get_dev_index.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/recorder/get_dev_index.py).

``` bash
$ python get_dev_index.py
(0, 'Built-in Microphone', 2)
(1, 'Built-in Output', 0)
(2, 'HDMI', 0)
```

만약 Device 2번이 사용가능하면 [recorder.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/recorder/recorder.py) 에서 DEVICE_NUMBER를 해당 값으로 정해줍니다.

If Device 2 is assignable, set device number to 2 at [recorder.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/recorder/recorder.py).

``` python
# Set device number using get_dev_index.py's assignable device information.
DEVICE_NUMBER = 2
```

결과 값으로는 '.sound.raw'에 음성 raw 데이터를 저장하고, 해당 음성 파일의 시작 pointer를 반환합니다. 단 '.sound.raw' 파일에 실제 음성이 저장되지는 않습니다.(0 Bytes 더미파일)

It returns the pointer which is the beginning part at voice raw data('.sound.raw').
