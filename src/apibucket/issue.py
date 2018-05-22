#-*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import urllib2
from bs4 import BeautifulSoup

def get_issue():
    url = urllib2.urlopen('https://www.naver.com')
    soup = BeautifulSoup(url, 'html.parser')
    result = soup.select(".PM_CL_realtimeKeyword_rolling span[class*=ah_k]")
    
    issue_data = list()
    issue_data.extend([u"오늘의 이슈로는"])
    
    for idx, title in enumerate(result, 1):
        issue_data.extend([unicode(title.text), ','])
    
    issue_data.extend([u"등 이있습니다."])
    text = ' '.join(issue_data)
    print('[HARU] {t}'.format(t=text))
    return text
