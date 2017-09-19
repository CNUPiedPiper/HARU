import parser
import word2vec

class Sentence2Vec:
    def __init__(self):
        self.parser = parser.Parser()
        self.w2v = word2vec.Word2Vec()

    def sentence2vec(self, sentence):
        word_set = self.parser.parse_sentence(sentence)
        p_input = ["{}/{}".format(word, tag) for word, tag in word_set]
        result = []
        for i in p_input:
        	try:
        		result.append(self.w2v.word2vec(i))
        	except KeyError as e:
	        	continue
        return result, p_input
