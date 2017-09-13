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
from led_controller import Led_controller

# Haru main class.
class Main:
    
    # Module for classifying user's order sentence.
    class Classifier:
        def __init__(self):
            self.s2v = sentence2vec.Sentence2Vec()
            self.model_set = []
            
            # Read neural network model from file.
            file_list = listdir( ''.join([dirname(abspath(__file__)), '/model']) )
            file_list.sort()
            for f in file_list:
                self.model_set.append(modelbuilder.ModelBuilder(f))

        def classify(self, input_sentence):
            # Convert input_sentence to vector using sentecne2vec.
            input_vector = np.array(self.s2v.sentence2vec(input_sentence))
            
            result = np.array([])
            model_number = 1
            
            # Put pre-processed vector to neural network model.
            for model in self.model_set:
                status_1 = np.zeros([100])
                status_2 = np.zeros([100])
                for i in xrange(input_vector.shape[0]):
                    prop, status_1, status_2 = model.run(input_vector[i, :], status_1, status_2)
                result = np.append(result, prop)
                print(''.join(['[HARU] Model', str(model_number), ' :: ', str(result[model_number-1])]))
                model_number = model_number + 1

            max_index = np.argmax(result)
            
            # No answer in model
            if result[max_index] < 0.5:
                return 0
            # Return argmax index
            else:
                return max_index + 1

    def __init__(self):
        self.classifier = self.Classifier()
        self.response = [functions.__dict__.get(func) for func in dir(functions)
                           if isinstance(functions.__dict__.get(func), types.FunctionType)]

        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        naver_id = self.config.get('NAVER', 'id')
        naver_secret = self.config.get('NAVER', 'secret')

        self.detector = hotword.hotword()
        self.speaker = text2speech.Text2Speech(naver_id, naver_secret)
        self.rec = recorder.Recorder()

        self.led = Led_controller()
        self.led.start()
        self.speaker.speak(u'안녕하세요')
        self.speaker.speak(u'하루를 시작합니다..')

    def main_flow(self):
        print('[HARU] In Main flow..')
        print('[HARU] Recording now.. Ask a question now') 
        self.speaker.speak(u'말씀하세요')
        self.led.turn_on()
        
        # Record user's order sentence.
        audio_buffer = self.rec.record_audio()

        print('[HARU] Now transcribe the audio buffer to text')
        self.led.turn_off()

        # Transcribing audio buffer streaming to korean.
        sentence = transcribe_streaming.transcribe_streaming(audio_buffer)
        
        #sentence = u'오늘 날씨는 어때'
        #sentence = u'오늘 이슈는 뭐야'
        #sentence = u'지금 몇시야'
        #sentence = u'이 노래가 뭐지'
        
        self.rec.close_buf()
        self.led.turn_on()

        # Get classified number from user's order sentence.
        response_number = self.classifier.classify(sentence)
        print('[HARU] Getting the result text from API')
        
        # Run app function
        answer_text = self.response[response_number](None)
        self.speaker.speak(answer_text)

        self.led.turn_off()
        
        # Call run funciton again.
        self.run()

    def run(self):
        # Detecting wake-up word.
        self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    print('[HARU] Starting the HARU')
    haru = Main()
    haru.run()
