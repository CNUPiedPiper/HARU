from os.path import abspath
import sys
sys.path.insert(0, abspath('../sentence2vec'))
import numpy as np
import modelbuilder as mb
import parser
import word2vec

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print '$python test.py model_number sentence_to_test'
        exit()

    model = mb.ModelBuilder(sys.argv[1])
    p = parser.Parser()
    w = word2vec.Word2Vec()

    sentence = ["{}/{}".format(word, tag) for word, tag in p.parse_sentence(sys.argv[2])]
    result = np.array(w.word2vec(sentence))

    status = np.zeros([1])
    for i in xrange(result.shape[0]):
        output, status = model.run(result[i, :], status)
        print 'prob :', output
