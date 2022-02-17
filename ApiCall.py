import json
from urllib.request import urlopen


def getCountry(ipAdress):
    response=urlopen("https://freegeoip.app/json/"+ipAdress).read().decode('utf-8')
    responsejson=json.loads(response)
    return responsejson.get("country_code")
