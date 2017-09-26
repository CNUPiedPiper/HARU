Trainer Module
===============================================================================

&nbsp;&nbsp;이 디렉토리는 사용자의 음성 명령들을 특정 번호로 분류시키는 기능을 가진 RNN 모델을 훈련하는 모듈입니다. </br>
&nbsp;&nbsp;This directory is a moudle that trains the RNN model which classifies user's input sentences into specific numbers.

## Dependencies
- [Tensorflow](https://www.tensorflow.org/)


##
&nbsp;&nbsp;먼저 [/src](https://github.com/CNUPiedPiper/HARU/tree/master/src/) 디렉토리의  functions.py 파일 내에 HARU가 수행해야할 동작을 양식에 맞추어 구현합니다. 그다음 [/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) 디렉토리 내에 해당 동작을 수행시킬 문장들의 예시를 model# 형식의 이름을 가진 파일 내에 입력합니다. model의 번호와 함수의 번호는 일치해야 합니다.</br>
예시는 다음과 같습니다.</br>
&nbsp;&nbsp;Implement the function that HARU should perform in the form, in the function.py in the [/src](https://github.com/CNUPiedPiper/HARU/tree/master/src/) directory. Then, in the [/res](https://github.com/CNUPiedPiper/HARU/tree/master/src/trainer/res) directory, put the sentences to execute the previously implemented function in the file with the name of the model type. The number of model and the number of function must match each other.</br>

&nbsp;&nbsp;Here's an example:
</br>

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
&nbsp;&nbsp;그리고 다음과 같이 훈련 시키고 싶은 model number와 훈련 횟수를 인자로 넘겨서 실행시킵니다.</br>
&nbsp;&nbsp;Then, run with the model number and the number of training that you want to train as follows.

``` bash
# In src directory.
$ python trainer_runner.py model_number iteration_number
$ python trainer_runner.py 3 100
``` 
