#-*- coding: utf-8 -*-
from konlpy.tag import Twitter
import sys

class Parser:
	def __init__(self):
		self.twitter = Twitter()

	def parse_sentence(self, sentence):
		result = self.twitter.pos(sentence.decode('utf-8'), norm=True, stem=True)
		return result

if __name__ == "__main__":
	parser = Parser()
	result = parser.parse_sentence('오늘 대전 날씨는 어떄')
	print(result)
