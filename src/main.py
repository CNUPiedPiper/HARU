#-*- coding: utf-8 -*-
from os import listdir
from os.path import abspath, dirname
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import functions
import types
from builder import modelbuilder
from sentence2vec import sentence2vec
from recorder import recorder
from detector import hotword
from text2speech import text2speech
from speech_recognition import transcribe_streaming
import configparser

class Main:
    class Classifier:
        def __init__(self):
            self.s2v = sentence2vec.Sentence2Vec()
            self.model_set = []
            for f in listdir( ''.join([dirname(abspath(__file__)), '/model']) ):
                self.model_set.append(modelbuilder.ModelBuilder(f))

        def classify(self, input_sentence):
            input_vector = np.array(self.s2v.sentence2vec(input_sentence))
            
            result = np.array([])
            for model in self.model_set:
                status = 0
                for i in xrange(input_vector.shape[0]):
                    prop, status = model.run(input_vector[i, :], status)
                result = np.append(result, prop)

            max_index = np.argmax(result)
            if result[max_index] < 0.5:
                return 0
            else:
                return max_index + 1

    def __init__(self):
        self.classifier = self.Classifier()
        self.response = [functions.__dict__.get(func) for func in dir(functions)
                           if isinstance(functions.__dict__.get(func), types.FunctionType)]
        self.response = self.response[::-1] 

        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        naver_id = self.config.get('NAVER', 'id')
        naver_secret = self.config.get('NAVER', 'secret')

        self.detector = hotword.hotword()
        self.speaker = text2speech.Text2Speech(naver_id, naver_secret)
        self.rec = recorder.Recorder()

    def main_flow(self):
        print('[HARU] In Main flow..')
        print('[HARU] Recording now.. Ask a question now') 
        audio_buffer = self.rec.record_audio()
        sentence = transcribe_streaming.transcribe_streaming(audio_buffer)
        self.rec.close_buf()
        #sentence = u'오늘 날씨는 어때'
        response_number = self.classifier.classify(sentence)
        answer_text = self.response[response_number](None)
        self.speaker.speak(answer_text)
        self.run()

    def run(self):
        print('run')
        while True:
            self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    Main().run()
