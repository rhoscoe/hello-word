# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:16:15 2017

@author: rosie_000

Exercise 19: Decode a Web Page 2
Using the requests and BeautifulSoup Python libraries, print to the screen the 
full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture .
Before it used to be on four separate pages, but now only 1, making the challenge easy.
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")
news = soup.find('div','component-newsletter-cta').decompose() #to get rid of Vanity Fair subscribe text
news = soup.find('div',"embed slideshow article-slideshow-embed row").decompose() #to get rid of slideshow photo text
news = soup.find_all("section", "content-section")

for story in news:
    print (story.text)