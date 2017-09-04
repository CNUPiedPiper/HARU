Haru(Humanic Awareness and Response Unit) 
===============================================================================

<p align="center">
  <img src="http://i.imgur.com/0TUUXZO.png">
</p>

## Standalone Version
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

## Getting started

먼저 텍스트를 음성으로 변환시키는 모듈을 사용하기 위해 [config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 를 작성합니다.</br>
작성방법은 [여기](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech)에서 확인할 수 있습니다.</br>
First, write a [config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) to use the module to convert the text to speech.</br>
You can find how to write [here](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech).

// /model, functions.py, train_runner를 채우고 실행한다.</br>
// led_controller(option)</br>

Then run main.py as follows:
``` bash
$ sudo python main.py
```

## Structure

// 여기에 디렉토리와 파일에 대해 한줄씩 설명
- [/apibucket](https://github.com/CNUPiedPiper/HARU/tree/master/src/apibucket) - [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py) 에서 사용할 수 있는 모듈들의 디렉토리입니다. </br>
- [/builder](https://github.com/CNUPiedPiper/HARU/tree/master/src/builder) - 피쳐값을 읽어와서 모델을 만드는 디렉토리입니다.</br>
- [/detector](https://github.com/CNUPiedPiper/HARU/tree/master/src/detector) - HARU를 깨우는 사용자의 행동을 탐지하는 모듈들의 디렉토리입니다. </br>
- [/model](https://github.com/CNUPiedPiper/HARU/tree/master/src/model) - 트레이닝시킨 모델의 피쳐값이 있는 디렉토리입니다. </br>
- [/recorder](https://github.com/CNUPiedPiper/HARU/tree/master/src/recorder) - 사용자의 음성 명령을 바이너리 데이터로 녹음하는 모듈의 디렉토리 입니다. </br>
- [/sentence2vec](https://github.com/CNUPiedPiper/HARU/tree/master/src/sentence2vec) - 사용자의 명령 텍스트를 벡터값으로 변환시키는 모듈의 디렉토리 입니다. </br>
- [/speech_recognition](https://github.com/CNUPiedPiper/HARU/tree/master/src/speech_recognition) - 바이너리 데이터로 변환시킨 음성 명령을 텍스트로 변환시키는 모듈의 디렉토리 입니다. </br>
- [/text2speech](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech) - HARU가 만든 텍스트 형태의 답을 음성형태로 변환시키는 모듈의 디렉토리 입니다. </br>
- [/trainer](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer) - RNN모델을 훈련하는 모듈의 디렉토리 입니다. </br>
- [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py) - HARU가 할 수 있는 기능들을 구현한 모듈 파일입니다</br>
- [led_controller.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/led_controller.py) - led를 사용하여 HARU의 진행상황을 알 수 있도록 해주는 모듈 파일입니다. </br>
- [train_runner.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/train_runner.py) - [traner.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/trainer/trainer.py)모듈을 [main.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/main.py)에서 실행시키는 파일입니다. </br>
- [config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) - api key를 저장하여 사용하는 파일입니다. </br>
- [main.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/main.py) - HARU를 실행하는 파일입니다. </br>
