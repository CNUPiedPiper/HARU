Sentence2Vec Module
===============================================================================

KoNLPy의 문장 파싱 기능과 Gensim의 Word2Vec 기능을 이용하여 문장을 n개의 형태소로 분할하고, 이를 n x 100 형태의 Matrix로 변환해주는 모듈입니다.</br>

## Dependencies
- [KoNLPy](http://konlpy-ko.readthedocs.io/ko/v0.4.3/)
- [Gensim](https://radimrehurek.com/gensim/)


##
Sentence2Vec 객체 생성 후, sentence2vec 함수에 Matrix로 변환할 문장을 인자로 넘겨주어 호출하면, 함수 호출의 결과로 Matrix를 리턴받을 수 있습니다.


``` python
s = sentence2vec.Sentence2Vec()
result = s.sentence2vec(any_sentence)
```
