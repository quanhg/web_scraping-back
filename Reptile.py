#!/usr/bin/env python
#coding:utf-8
import pandas as pd
from requests_html import HTMLSession

session = HTMLSession()
url = "https://www.jianshu.com/p/85f4624485b9"
r = session.get(url)

sel = "body > div.note > div.post > div.article > div.show-content > div > p > a"

def get_text_link_from_sel(sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext,mylink))
        return mylist
    except:
        return None

df = pd.DataFrame(get_text_link_from_sel(sel))
df.columns = ["text","link"]
df.to_csv("output.csv",encoding="gbk",index=False)


#print(r.html.text)
#print(r.html.links)
#print(r.html.absolute_links)
# print(results[0].text)
# print(results[0].absolute_links)
# print(
#     list(results[0].absolute_links)
# )
#