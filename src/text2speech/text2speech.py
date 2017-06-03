# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import datetime
import pygame
from urllib2 import urlopen, Request
from urlparse import urlparse
from pygame import mixer, time

class text2speech:
    def __init__(self, c_id, c_secret):
        self.client_id = c_id
        self.client_secret = c_secret

    def play_sound(self, file_path):
        mixer.pre_init(44100, -16, 2, 256)
        mixer.init(frequency=16000, buffer=24000)
        pygame.init()
        mixer.music.load(file_path)
        mixer.music.play(loops=1)
        while mixer.music.get_busy():
            time.Clock().tick(100)

    def speak(self, input_text):
        data = "speaker=mijin&speed=0&text=" + unicode(input_text);

        q = Request("https://openapi.naver.com/v1/voice/tts.bin")
        q.add_header("X-Naver-Client-Id", self.client_id)
        q.add_header("X-Naver-Client-Secret", self.client_secret)

        response = urllib2.urlopen(q, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode == 200):
            print("Saved TTS to MP3")
            response_body = response.read()
            now = datetime.datetime.now()
            nowDatetime = now.strftime('%Y%m%d_%H:%M:%S')
            filename = str(nowDatetime) + '.mp3'
            
            with open(filename, 'wb') as f:
                f.write(response_body)

            self.play_sound(filename)
            return filename
            
        else:
            print("Error Code:" + rescode)

