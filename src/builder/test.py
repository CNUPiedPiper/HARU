from os.path import abspath
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.insert(0, abspath('../sentence2vec'))
import numpy as np
import modelbuilder as mb
import sentence2vec

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '$python test.py model_number sentence_to_test'
        exit()

    model = mb.ModelBuilder(sys.argv[1])
    s2v = sentence2vec.Sentence2Vec()

    result = np.array(s2v.sentence2vec(sys.argv[2]))
    status_1 = np.zeros([100])
    status_2 = np.zeros([100])
    for i in xrange(result.shape[0]):
        output, status_1, status_2 = model.run(result[i, :], status_1, status_2)
        print 'prob :', output
