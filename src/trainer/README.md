Trainer Module
===============================================================================

이 디렉토리는 사용자의 음성 명령들을 특정 번호로 분류시키는 기능을 가진 RNN 모델을 훈련하는 모듈입니다. </br>

This directory is a moudle that trains the RNN model which classifies user's input sentences into specific numbers.

## Dependencies
- [Tensorflow](https://www.tensorflow.org/)


##
[/src](https://github.com/CNUPiedPiper/HARU/tree/master/src/) 디렉토리의  functions.py 파일 내에 HARU가 수행해야할 동작을 양식에 맞추어 구현한 다음, [/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) 디렉토리 내에 앞서 구현한 함수 번호에 맞춰, 해당 동작이 수행될 문장들의 예시를 model# 형식의 이름을 가진 파일 내에 입력합니다.</br>
예시는 다음과 같습니다.</br>

Put the sentences that you want to be classified in [/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) into the given file of each model number as follows.</br>

``` 
# In model1 file.

오늘 날씨는 어때
날씨좀 알려줘
오늘 추울려나
우산 가져가야돼
오늘 덥니
비가 올까
오늘 비와
날씨 알려줘
```

##
그리고 다음과 같이 훈련 시키고 싶은 model number와 훈련 횟수를 인자로 넘겨서 실행시킵니다.</br>

Then, run with the model number and the number of training that you want to train as follows.

``` bash
$ python trainer.py model_number iteration_number
``` 
