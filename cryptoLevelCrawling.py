import datetime
import json
from urllib.request import *
from bs4 import BeautifulSoup
from urllib.error import *

def retrieveCoinAndPriceCoingecko(page,requestedAsset,retrieveExtra=False):
    try:
        req = Request('https://www.coingecko.com/?page='+str(page), headers={'User-Agent': 'Mozilla/5.0'})
    except HTTPError:
        raise Exception("Crawling is finished")
    else:
        webpage = urlopen(req).read()
        bsObj=BeautifulSoup(webpage)
        assetDict={}

    line=0

    asset=''

    for tr in bsObj.find("table").findAll("tr"):
        if line>0:
            try:
                pos=tr.find("td",{"class":"table-number tw-text-left text-xs cg-sticky-col cg-sticky-second-col tw-max-w-14 lg:tw-w-14"}).text.strip()
                asset=tr.find("span",{"class":"tw-hidden d-lg-inline font-normal text-3xs ml-2"}).text.strip()
                date=datetime.datetime.now().strftime("%Y-%m-%d")
                if requestedAsset == None or asset in requestedAsset:
                    price=float(tr.find("td", {"class": "td-price price text-right pl-0"}).text.strip().replace('$','').replace(',',''))
                    mcap=tr.find("td",{"class":"td-market_cap cap col-market cap-price text-right"}).span.text.strip().replace('$','').replace(',','')

                    link=tr.find("a",{"class":"d-lg-none font-bold tw-w-12"}).attrs['href']

                    ath=''
                    if retrieveExtra:
                        try:
                            reqSubLink = Request('https://www.coingecko.com/' + str(link), headers={'User-Agent': 'Mozilla/5.0'})
                            webpageSubLink = urlopen(reqSubLink).read()
                            bsObjSub = BeautifulSoup(webpageSubLink)
                            ath = bsObjSub.find(text='All-Time High').parent.parent.parent.find("span",{"class":"no-wrap"}).text
                        except Exception:
                            pass



                    assetDict[asset]={"pos":pos,"price":price,"mcap":mcap,"ath":ath,"date":date}
            except Exception as e:
                raise Exception("Crawling is finished")
        line+=1
    if(requestedAsset==None):
        return assetDict
    else:
        return assetDict


def retrieveFullCoingecko(requestedAsset=None,retrieveExtra=False,maxPage=1):
    assetDict = {}
    continueCrawl=True
    page=1
    while continueCrawl and page <= maxPage:
        try:
            assetDict.update(retrieveCoinAndPriceCoingecko(page,requestedAsset,retrieveExtra))
        except Exception:
            continueCrawl=False
        page+=1


    return json.dumps(assetDict)

    #for assetKey in assetDict.keys():
    #    print(assetDict[assetKey]["pos"] + " " + assetKey+" "+ str(assetDict[assetKey]["price"]) +" "+ assetDict[assetKey]["mcap"]+" "+ assetDict[assetKey]["ath"])