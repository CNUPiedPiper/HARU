from os import listdir
from os.path import abspath, dirname
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import functions
import types
from builder import modelbuilder
from sentence2vec import sentence2vec
from recorder import recorder
from geoip import geoip
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
            input_vector = np.array(s2v.sentence2vec(input_sentence))
            
            result = np.array([])
            for model in model_set:
                status = 0
                for i in xrange(input_vector.shape[0]):
                    prop, status = model.run(input_vector[i, :], status)
                np.append(result, prop)
			
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
        self.geo = geoip.Geoip().get_geo()
        self.city = self.geo[0]
        self.lat = self.geo[1]
        self.lon = self.geo[2]

        self.config = configparser.RawConfigParser()
        self.config.read('config.ini')
        weather_key = self.config.get('WEATHER', 'key')
        mise_key = self.config.get('MISE', 'key')
        naver_id = self.config.get('NAVER', 'id')
        naver_secret = self.config.get('NAVER', 'secret')

        self.detector = hotword.hotword()
        self.speaker = text2speech.Text2Speech(naver_id, naver_secret)
        self.rec = recorder.Recorder()

    def main_flow(self):
        print('[HARU] In Main flow..')
        print('[HARU] Recording now.. Ask a question now') 
        temp = self.rec.record_audio()
        transcribe_streaming.transcribe_streaming(temp)
        self.rec.close_buf()

        answer_text = self.response[0](None)
        self.speaker.speak(answer_text)
        self.run()

    def run(self):
        print('run')
        while True:
            self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    Main().run()
