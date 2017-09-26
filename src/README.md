Haru(Humanic Awareness and Response Unit) 
===============================================================================

<p align="center">
  <img src="http://i.imgur.com/0TUUXZO.png">
</p>

## Standalone Version
[![GitHub version](https://badge.fury.io/gh/boennemann%2Fbadges.svg)](http://badge.fury.io/gh/boennemann%2Fbadges)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

## Getting started

먼저 음성인식(STT)과 텍스트를 음성으로 변환시키는(TTS) 모듈을 사용하기 위해 [config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 를 작성하고,
[Google Cloud Speech API](https://github.com/CNUPiedPiper/HARU/tree/master/src/speech_recognition) 를 설정합니다.</br>
First, write a [config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) to use the module to convert the Text to Speech(TTS) and set the [Google Cloud Speech API](https://github.com/CNUPiedPiper/HARU/tree/master/src/speech_recognition) configuration.</br>

TTS 모듈에 대한 작성방법은 [여기](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech) 에서 확인할 수 있습니다.</br>
You can find how to write TTS module at [here](https://github.com/CNUPiedPiper/HARU/tree/master/src/text2speech).


그리고 다음과 같이 [main.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/main.py) 를 실행합니다.</br>
Then run [main.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/main.py) as follows.
``` bash
$ sudo python main.py
```

## Plug-in Interface
자신만의 스킬을 추가하고 싶으면 다음과 같은 과정을 진행합니다.</br>
If you want to add your own skills, proceed as follows.</br>


처음에는 [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py) 에 다음과 같이 원하는 번호와 그에 맞는 함수를 구현합니다.</br>
First, Implement the desired number and function as follows In [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py)

``` python
def function3(words):
    now = datetime.datetime.now()
    return u'지금은 {h}시 {m}분 입니다.'.format(h=now.hour, m=now.minute)
```

다른 라이브러리를 사용해 추가적으로 구현할 필요가 있는 함수는 [apibucket](https://github.com/CNUPiedPiper/HARU/tree/master/src/apibucket) 디렉토리에서 모듈 형태로 구현한 뒤 이를 [functions.py] (https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py)에서 추가시켜 사용합니다.</br>
If you have any functions that needs to be implemented using another library, you can implement it as a module in the [apibucket](https://github.com/CNUPiedPiper/HARU/tree/master/src/apibucket) directory and add it in [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py).
``` python
from apibucket import weather, issue, geoip
from apibucket.music_recognizer import music_recog
```

두번째로는 [/trainer/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) 에 분류되고 싶은 문장들을 각각의 모델 번호가 주어진 파일에 다음과 같이 넣어줍니다. 동작함수의 번호와 문장 예시 파일의 번호는 서로 일치하여야 합니다. </br>
Second, Put the sentences that you want to be classified in [/trainer/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) into the given file of each model number as follows. The number of the operation function and the number of the sentence example file must match each other.

``` 
# In model3 file.

지금 몇시니
지금 몇시야
시간 좀 알려줘
시간
몇시야
```


마지막으로, 훈련 시키고 싶은 Model 번호와 훈련 횟수를 인자로 넘겨서 [train_runner.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/train_runner.py) 를 실행시킵니다.</br>
Finally, run [train_runner.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/train_runner.py) with the model number and the number of training that you want to train as follows.
``` bash
# In src directory.
$ python train_runner.py model_number iteration_number
$ python train_runner.py 3 100
```


## Structure

- [/apibucket](https://github.com/CNUPiedPiper/HARU/tree/master/src/apibucket) - [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py) 에서 사용할 수 있는 모듈들의 디렉토리입니다. </br>
- [/builder](https://github.com/CNUPiedPiper/HARU/tree/master/src/builder) - HARU 실행 시, 저장된 피쳐값을 읽어와 모델을 빌드 디렉토리입니다.</br>
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
