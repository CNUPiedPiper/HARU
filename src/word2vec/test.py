import sys
import parser
import word2vec

p = parser.Parser()
c = word2vec.Word2Vec()
segment_set = p.parse_sentence(sys.argv[1])
segment = ["{}/{}".format(word, tag) for word, tag in segment_set]
result = []
for seg in segment:
	try:
		result.append(c.word2vec(seg))
	except KeyError as e:
		continue
print(result)
