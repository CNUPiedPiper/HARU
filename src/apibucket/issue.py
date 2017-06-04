#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
from bs4 import BeautifulSoup

def get_issue():
    url = urllib2.urlopen('http://datalab.naver.com/keyword/realtimeList.naver?where=main')
    soup = BeautifulSoup(url, 'html.parser')
    result = soup.find_all('ul')

    issue_data = list()
    issue_data.extend([u"오늘의 이슈로는"])

    for res in result:
        if res['class'][0] == 'rank_list':
            keywords = res.find_all('span')
            top = 0

            for key in keywords:
                if top == 10:
                    break

                data = key.contents[0].replace(' ','')
                issue_data.extend([unicode(data)])
                top = top + 1

            issue_data.extend([u"등 이있습니다."])

            text = ' '.join(issue_data)

            print('[HARU] {t}'.format(t=text))
            return text 

