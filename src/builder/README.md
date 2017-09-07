Builder Module
===============================================================================

Builder 모듈은 Trainer 모듈에 의해 훈련된 weight값을 읽어 RNN 모델로 구축하는 모듈입니다. </br>

## Dependencies
- [Numpy](http://www.numpy.org/)


##
Trainer 모듈에 의해 [/src/model](https://github.com/CNUPiedPiper/HARU/tree/master/src/model) 디렉토리에 원하는 모델 번호의 weight값들이 제대로 저장됐는지 확인 후, Builder 모듈의 생성자로 모델 번호를 전달하여 모델을 구축합니다.

모델의 구조는 다음과 같습니다.
<p align="center">
  <img src="https://github.com/CNUPiedPiper/HARU/tree/master/src/builder/Rough_model.png">
</p>

모델 구축 후 run 함수에 input, status1, status2의 순서대로 전달하여(status의 초기값은 0) output, status1, status2의 순서로 결과값을 전달받습니다. [test.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/builder/test.py) 코드를 통해 Sequence2Vector 모듈과의 연계 및 실제 결과를 테스트하실 수 있습니다.


``` python
model = mb.ModelBuilder(model_number)
s2v = sentence2vec.Sentence2Vec()

result = np.array(s2v.sentence2vec(sys.argv[2]))
status_1 = np.zeros([100])
status_2 = np.zeros([100])
for i in xrange(result.shape[0]):
    output, status_1, status_2 = model.run(result[i, :], status_1, status_2)
    print 'prob :', output
```
