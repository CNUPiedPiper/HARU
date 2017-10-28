import unittest
from os import listdir
from os.path import abspath, dirname
import sys
reload(sys)
import numpy as np
sys.setdefaultencoding('utf-8')
from builder import modelbuilder
from sentence2vec import sentence2vec

class Test(unittest.TestCase):

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
            result = self.s2v.sentence2vec(input_sentence)
            words_vec = result[0]
            words_raw = result[1]

            input_vector = np.array(words_vec)
            
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
                return 0, words_raw
            # Return argmax index
            else:
                return max_index + 1, words_raw

    def setUp(self):
        self.classifier = self.Classifier()
        self.eval_set = open('evaluation_set','r')
        self.examples = [ex.split(', ') for ex in self.eval_set]

    def tearDown(self):
        self.eval_set.close()

    def test_classify(self):
        for sentence, label in self.examples:
            print('\ninput : ' + sentence)
            print('label : ' + label)
            self.assertEqual(self.classifier.classify(sentence)[0], int(label[0]))

if __name__ == '__main__':
    unittest.main()
    