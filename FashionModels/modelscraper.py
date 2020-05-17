import re
import urllib
from urllib import parse
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import urllib.request
from bs4 import NavigableString
import sys
import json
import csv
import requests


class ModelScraper:
    def __init__(self, url):
        self.url = url
        # print("opening")
        self.html_text = None
        try:
            self.html_text = requests.get(self.url).content
            # self.html_text = urllib.request.urlopen(url).read().decode('utf-8')
            # self.html_text = requests.get(url).text
        except Exception as err:
            print(str(err))
            return
        else:
            print('Access successful to ',url)

        self.soup = None
        if self.html_text is not None:
            self.soup = BeautifulSoup(self.html_text, 'lxml')

    def scrap(self):
        if self.soup is None:
            return {}
        soup = self.soup
        details = dict()
        left_panel = soup.find("div",attrs={"class":"pure-u-1 pure-u-lg-10-24"})
        details['general_info']=" "
        for p in left_panel.findAll("p"):
            details['general_info'] += p.text +", "
        details['imdb_rating'] = soup.find("span",attrs={"itemprop":"ratingValue"}).text
        details['tv_shows']=" "
        tvdiv = soup.find("div",attrs={"id":"persontv-1"})
        if tvdiv:
            for a in tvdiv.findAll("a"):
                details['tv_shows']+=a.text+", "
        details['movies']=" "
        moviediv = soup.find("div",attrs={"id":"personmovies-1"})
        if moviediv:
            for a in moviediv.findAll("a"):
                details['movies']+=a.text+", "
        
        return details


if __name__ == '__main__':
    out_file = open("models_info.json", "a")
    with open('model_links.txt', 'r', encoding="utf-8") as f:
        for line in f:
            zr = ModelScraper(line)
            json.dump(zr.scrap(), out_file)
            out_file.write(',\n')
    out_file.close()
    
     #values row
    browser.close()