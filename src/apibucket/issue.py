#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def get_issue():
    url = urllib2.urlopen('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
    soup = BeautifulSoup(url, 'html.parser')
    result = soup.find_all('ul')

    issue_data = list()

    text = u"오늘의 이슈로는 "

    for res in result:
        if res['class'][0] == 'rank_list':
            keywords = res.find_all('span')
            top = 0

            for key in keywords:
                if top == 10:
                    break
                text = text + unicode(key.contents[0]) + " "
                issue_data.append(key.contents[0])
                top = top + 1

            text = text + u"이가 있습니다."

            print('[HARU] {t}'.format(t=text))
            return text 

