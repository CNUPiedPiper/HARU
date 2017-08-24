# APIBucket
[functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py) 에서 사용할 수 있는 모듈들의 디렉토리입니다. <br>
API를 이용하여 데이터를 가져오고 해당 데이터를 이용해 원하는 문장 형태로 반환합니다. 

This directory contains modules to use in [functions.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/functions.py).<br>
The module uses the API to fetch raw data and return it in the form of the desired statement using the data.

## [mise.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/apibucket/mise.py)
현재 미세먼지를 얻을 수 있는 모듈입니다.<br>
먼저 [한국환경공단_대기오염정보 조회 서비스](https://www.data.go.kr/dataset/15000581/openapi.do) 활용신청을 등록 한 뒤
[src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 에 다음과 같이 작성하여 사용합니다.

It is a module that can get current fine dust.<br>
Before you use it, register [Korea environment Public Corporation air pollution information inquiry service](https://www.data.go.kr/dataset/15000581/openapi.do) API Key and write to [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) as follows.
``` ini
[MISE]
key = "YOUR 'www.data.go.kr' KEY" 
```


## [weather.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/apibucket/weather.py)
현재 날씨정보를 얻을 수 있는 모듈입니다.<br>
먼저 [SK planet Developers](https://developers.skplanetx.com/apidoc/kor/weather/) API Key를 등록 한 뒤 [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 에 다음과 같이 작성하여 사용합니다.

It is a module that can get current weather.<br> 
Before you use it, register [SK planet Developers](https://developers.skplanetx.com/apidoc/kor/weather/) API Key and write to [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) as follows.
``` ini
[WEATHER]
key = "YOUR 'developers.skplanetx.com/apidoc/kor/weather' KEY"
```


## [issue.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/apibucket/issue.py)
현재 네이버 실시간 검색어를 얻을 수 있는 모듈입니다. 

It is a module that can get real-time issue keyword from Naver.


## [music_recognizer/music_recog.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/apibucket/music_recognizer/music_recog.py)
음악을 듣고 음악에 대한 정보를 얻을 수 있는 모듈입니다.<br>
먼저 [ACRCloud](https://www.acrcloud.com/) API Key를 등록 한 뒤 [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) 에 다음과 같이 작성하여 사용합니다.

It is a module that can get music title from music.<br>
Before you use it, register [ACRCloud](https://www.acrcloud.com/) API Key and write to [src/config.ini](https://github.com/CNUPiedPiper/HARU/blob/master/src/config.ini) as follows.
``` ini
[MUSIC_RECOGNIZER]
host = "YOUR 'https://www.acrcloud.com/' host"
key = "YOUR 'https://www.acrcloud.com/' key"
secret = "YOUR 'https://www.acrcloud.com/' secret"
```
