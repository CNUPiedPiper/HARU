from os import listdir
from os.path import abspath, dirname
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import functions
import types
from builder import modelbuilder
from sentence2vec import sentence2vec

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
    def run(self):
        print('run')

if __name__ == "__main__":
    m = Main()
    m.run()
