밑의 Google Original Reference를 따르면 Google account key에 관한 json파일을 받고, ~/.bashrc에 export를 명시해주지만

저희의 경우엔 실행시 json path를 제대로 못가져오는 에러가 발생하여

[/speech_recognition/transcribe_streaming.py](https://github.com/CNUPiedPiper/HARU/blob/master/src/speech_recognition/transcribe_streaming.py) 에서 밑의 방법으로 해결하였습니다.

``` python
# line 30, write your google account key json path
google_json_key_path = '/home/pi/HARU-6bad27ee1998.json'

# line 37
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = google_json_key_path
```


# Google Cloud Speech API Python Samples
This directory contains samples for Google Cloud Speech API. The Google Cloud Speech API enables easy integration of Google speech recognition technologies into developer applications. Send audio and receive a text transcription from the Cloud Speech API service.

## Setup
### Authentication
Authentication is typically done through Application Default Credentials, which means you do not have to change the code to authenticate as long as your environment has credentials.

You can create a [Service Account key file](https://developers.google.com/identity/protocols/OAuth2ServiceAccount#creatinganaccount). This file can be used to authenticate to Google Cloud Platform services from any environment. To use the file, set the ``GOOGLE_APPLICATION_CREDENTIALS`` environment variable to the path to the key file.
</br>
``` bash
    # ~/.bashrc
    export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service_account.json
```

## Install Dependencies
1. Install [pip](https://pip.pypa.io/) and [virtualenv](https://virtualenv.pypa.io/) if you do not already have them.

2. Create a virtualenv. Samples are compatible with Python 2.7 and 3.4+.

``` bash
    $ virtualenv env
    $ source env/bin/activate
```

3. Install the dependencies needed to run the samples.

``` bash
    $ pip install -r requirements.txt
```

## Samples
### Transcribe Streaming
To run this sample:

``` bash

    $ python transcribe_streaming.py

    usage: transcribe_streaming.py [-h] stream

    Google Cloud Speech API sample application using the streaming API.

    Example usage:
        python transcribe_streaming.py resources/audio.raw

    positional arguments:
        stream    File to stream to the API

    optional arguments:
        -h, --help    show this help message and exit
```

## The client library

This sample uses the [Google Cloud Client Library for Python](https://googlecloudplatform.github.io/google-cloud-python/). You can read the documentation for more details on API usage and use GitHub to [browse the source](https://github.com/GoogleCloudPlatform/google-cloud-python) and  [report issues](https://github.com/GoogleCloudPlatform/google-cloud-python/issues)
