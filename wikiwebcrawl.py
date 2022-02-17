import datetime
import random
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup


random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html=urlopen("https://en.wikipedia.org/"+articleUrl)
    bsObj=BeautifulSoup(html)
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

def printLinks():
    totalCrawl=0
    links = getLinks("/wiki/Kevin_Bacon")
    while len(links) > 0 and totalCrawl<100:
        newArticle = links[random.randint(0, len(links))].attrs["href"]
        html = urlopen("https://en.wikipedia.org/"+newArticle)
        bsObj = BeautifulSoup(html)
        print(bsObj.h1.text)
        totalCrawl+=1
        links=getLinks(newArticle)