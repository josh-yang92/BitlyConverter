import bitly_api
import requests

from bs4 import BeautifulSoup


#   shortening the long url
def getShortLink(APIUser, APIKey, longurl):
    b = bitly_api.Connection(APIUser, APIKey)
    response = b.shorten(uri=longurl)
    return response['url']


#   get the product name
def getItemName(itemLink):
    resp = requests.get(itemLink)
    a = BeautifulSoup(resp.text, 'html.parser')
    b = a.find_all(name='h1', attrs={'itemprop': 'name'})
    itemName = []
    for item in b:
        for names in item.contents:
            try:
                n = names.text
                itemName.append(n)
            except:
                continue
    return ' '.join(itemName)
