Naver Text2Speech API
===============================================================================

이 디렉토리는 [Naver Text2Speech API](https://developers.naver.com/products/clova/tts/)를 라즈베리파이에서 Python으로 사용 할 수 있도록 Class화 해놓은 파일입니다.<br>

This directory contains [Naver Text2Speech API](https://developers.naver.com/products/clova/tts/) Python Class for using at Raspberry PI.<br><br>



먼저 [Naver API Key](https://developers.naver.com/main/)를 등록 한 뒤, 
[src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 에 다음과 같이 작성하여 사용합니다.<br>

Before you use it, register [Naver API Key](https://developers.naver.com/main/) and write to [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) as follows.

``` ini
[NAVER]
id = "YOUR 'developers.naver.com' ID" 
secret = "YOUR 'developers.naver.com' SECRET" 
```
