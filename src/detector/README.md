Hotword Detection
===============================================================================

이 디렉토리는 Snowboy Hotword Detection API를 라즈베리파이에서 Python으로 사용 할 수 있도록 Class화 해놓은 파일입니다.</br>
This directory contains Snowboy Hotword Detection Python Class for using at Raspberry PI.</br>

Snowboy에 관련된 설명은 [여기](http://docs.kitt.ai/snowboy/)서 확인 할 수 있으며, 따로 설정해야 하는 API Key는 없습니다.</br>
Snowboy-related descriptions can be found [here](http://docs.kitt.ai/snowboy/), but there are no API Keys to set.

'하루야' 라고 부르거나 푸시버튼을 누르면 Haru가 깨어나서 사용자의 음성을 녹음 할 수 있는 상태가 됩니다.</br>
If you call it "Haru ya" or push the button, Haru will wake up and you will be able to record your voice.</br>

저희는 일반적인 푸시버튼을 사용하였으며, 이를 사용하기 위해 [WiringPi](https://github.com/neuralpi/WiringPi-Python) 모듈을 사용하였습니다.</br>
We used the general push button with the [WiringPi](https://github.com/neuralpi/WiringPi-Python) module.</br>

<p align="center">
  <img src="https://i.imgur.com/3NxqOUp.png">
</p>
