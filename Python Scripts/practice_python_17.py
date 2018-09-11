# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 10:58:17 2017

@author: rosie_000

Exercise 17: print out a list of the article headlines on the NY Times home page
"""
import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'

r = requests.get(url)
r_html = r.text

hllist =[]

soup = BeautifulSoup(r_html,"html.parser")
headl = soup.find_all("h2", "story-heading")


for story in headl:
    print(story.text.replace("\n", " ").strip())
    
