import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import sentence2vec

s = sentence2vec.Sentence2Vec()
result = s.sentence2vec(sys.argv[1])
print(result)
