#-*- coding: utf-8 -*-
import gensim
import sys
from os.path import abspath

class Word2Vec:
    def __init__(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
        self.model = gensim.models.Word2Vec.load(abspath('../word2vec/res/model'))

    def word2vec(self, word):
        if isinstance(word, list):
            result = []
            for w in word:
                result.append(self.model.wv[w.decode('utf-8')])
            return result

        return self.model.wv[word.decode('utf-8')]

if __name__ == '__main__':
    word2vec = Word2Vec()
    print(word2vec.word2vec('오늘/Noun'))
