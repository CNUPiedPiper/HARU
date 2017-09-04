Trainer Module
===============================================================================

이 디렉토리는 사용자의 음성 명령들을 특정 번호로 분류시키는 기능을 가진 RNN 모델을 훈련하는 모듈입니다. </br>

This directory is a moudle that trains the RNN model which classifies user's input sentences into specific numbers.

## Dependencies
- [Tensorflow](https://www.tensorflow.org/)


##
[/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) 에 분류되고 싶은 문장들을 각각의 모델 번호가 주어진 파일에 다음과 같이 넣어줍니다.</br>

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
