#!/bin/env python
#coding:utf-8

import os 
from bs4 import BeautifulSoup
import json
import requests

user_agent ='Mozilla/5.0 (Windows NT 6.3; Win64; x64)'
headers = {'User-Agent':user_agent}
r = requests.get('http://seputu.com/',headers=headers)
#print r.text
soup = BeautifulSoup(r.text,'html.parser',from_encoding='utf-8')
content=[]

for mulu in soup.find_all(class_="mulu"):
    h2 = mulu.find('h2')
        if h2 != None:
	        h2_title = h2.string
		        #print h2_title
			        list1=[]
				        for a in mulu.find(class_='box').find_all('a'):
					            href = a.get('href')
						                #print href
								            box_title = a.get('title')
									                #print box_title
											            list1.append({'href':href,'box_title':box_title})
												            content.append({'title':h2_title,'content':list1})
													    with open('F:/\Git/\qiye.json','wb') as fp:
													        json.dump(content,fp=fp,indent=4)
