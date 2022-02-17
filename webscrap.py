from urllib.request import urlopen, Request
from urllib.error import URLError
from bs4 import BeautifulSoup
import ssl


def wikiLinkTest():
    html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
    bsObj = BeautifulSoup(html)

    bsObj.findAll("a")

    for link in bsObj.findAll("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])


def siblingTest():
    context = ssl._create_unverified_context()
    html = urlopen('http://pythonscraping.com/pages/page3.html',context=context)
    bs=BeautifulSoup(html)

    for sibling in bs.find("table",{"id":"giftList"}).tr:
        print(sibling)




def spanTest():
    context = ssl._create_unverified_context()

    try:
       #html=urlopen('https://pythonscraping.com/pages/warandpeace.html',context=context)
       req = Request('https://www.coingecko.com', headers={'User-Agent': 'Mozilla/5.0'})
       webpage = urlopen(req).read()
       #html=urlopen('https://www.coingecko.com',context=context)
    except URLError as e:
        print(e)
    else:
        bsObj=BeautifulSoup(webpage)
        green = bsObj.findAll("span",{"class":"d-md-inline currency-name"})

        for g in green:
            print(g.text)

        allThe=bsObj.findAll



def firstTest():
    try:
        #html=urlopen('http://pythonscrapping.com/pages/page1.html')
        html = urlopen('http://www.coinmarketcap.com')
    except URLError as e:
        print(e)
        print('Web Scrapping aborted')
    else:
        if html:
            bsObj = BeautifulSoup(html.read())

            table = bsObj.findAll("table")

            table[0].findAll("a")

            if bsObj.hx:
                print(bsObj.hx)
            else:
                print('Html doesnt have h1 tag')
        else:
            print('Html is not valid')

