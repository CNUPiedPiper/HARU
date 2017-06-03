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
from speaker import tts
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

            return np.argmax(result)

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
        self.speaker = tts.tts(naver_id, naver_secret)

    def main_flow(self):
        self.detector.terminate_detection()

        print('[HARU] In Main flow..')
        print('[HARU] Recording now.. Ask a question now') 
        recording.record_audio()

        answer_text = response[0](None)
        self.speaker.get_speech_file_path(answer_text)
        self.run()

    def run(self):
        print('run')
        self.detector.start_detection(self.main_flow)

if __name__ == "__main__":
    Main().run()
