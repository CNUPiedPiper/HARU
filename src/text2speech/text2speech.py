# -*- coding: utf-8 -*-
import os
import sys
import urllib2
import pygame
from urllib2 import urlopen, Request
from urlparse import urlparse
from pygame import mixer, time

class Text2Speech:
    """ TTS Module class.

    This class speaks the text of answer about user's question using Naver Korean TTS API.
    You can check the references at 'https://developers.naver.com/docs/labs/tts/'.
    """

    def __init__(self, c_id, c_secret):
        """ Inits Text2Speech with API id and secret. 

        Args:
            c_id : The client id of the Naver API.
            c_secret : The client secret of the Naver API.
        """
        self.client_id = c_id
        self.client_secret = c_secret

    def play_sound(self, file_path):
        """ Play the sound of mp3 file using pygame mixer.

        Args:
            file_path : The file path of the mp3 file that user wants to play.
        """
        mixer.pre_init(44100, -16, 2, 256)
        mixer.init(frequency=16000, buffer=24000)
        pygame.init()
        mixer.music.load(file_path)
        mixer.music.play(loops=1)

        while mixer.music.get_busy():
            time.Clock().tick(100)

    def speak(self, input_text):
        """ Request TTS API with input_text and then save the output as mp3.

        Args:
            input_text : The input text of the answer from the user's question.
        """
        data = "speaker=mijin&speed=0&text=" + unicode(input_text);

        q = Request("https://openapi.naver.com/v1/voice/tts.bin")
        q.add_header("X-Naver-Client-Id", self.client_id)
        q.add_header("X-Naver-Client-Secret", self.client_secret)

        response = urllib2.urlopen(q, data=data.encode('utf-8'))
        rescode = response.getcode()

        if(rescode == 200):
            response_body = response.read()
            filename = '.response.mp3'

            with open(filename, 'wb') as f:
                f.write(response_body)
                
            self.play_sound(filename)
        else:
            print("Error Code:" + rescode)