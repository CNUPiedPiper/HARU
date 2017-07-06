#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python recognition_api.py test.mp3
'''

import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

def recognize_music(music_file, host, key, secret):
    config = {
        'host': host.encode('utf-8'),
        'access_key': key.encode('utf-8'),
        'access_secret': secret.encode('utf-8'),
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':10 # seconds
    }

    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    #print re.recognize_by_file(music_file, 0, 10)

    buf = open(music_file, 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].  print re.recognize_by_filebuffer(buf, 0, 10) 
    result = re.recognize_by_filebuffer(buf, 0, 10)
    return result
