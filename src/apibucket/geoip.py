#-*- coding: utf-8 -*-
import pygeoip
import requests
from bs4 import BeautifulSoup

class Geoip:
    def __init__(self):
        self.geo_data = pygeoip.GeoIP('GeoLiteCity.dat')

        r = requests.get('http://ip.ojj.kr')
        soup = BeautifulSoup(r.text, 'html.parser')
        result = soup.find('font',attrs={'face':'verdana', 'color':'RED'})
        ip = result.text

        rec = self.geo_data.record_by_name(ip)
        self.city = rec['city']
        self.lat = rec['latitude']
        self.lon = rec['longitude']

    def get_geo(self):
        return self.city, self.lat, self.lon
