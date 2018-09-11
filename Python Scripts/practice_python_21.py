# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 21:18:30 2017

@author: rosie_000

Exercise 21: use the code from Exercise 17 and write the results to a text file
"""

import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,"html.parser")
headl = soup.find_all("h2", "story-heading")


"""with open('Exercise_21.txt', 'w') as open_f:
    for story in headl:
        open_f.write(story.text.replace("'b'" and "b'","\n").encode('utf-8').strip())"""
with open('Exercise_21.txt', 'w') as open_f:
    for story in headl:
        open_f.write(story.text.encode('utf-8').strip()+'\n')