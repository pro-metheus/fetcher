## fetchbot spider v.0.0.1 beta created by pro_metheus

import requests
from bs4 import BeautifulSoup as bs


def spider(a):  #the spider function who visits the links provided by the breaker
    if(requests.get(a)):
        r=requests.get(a)
        print(a+" found and is working...")
    #all other function goes here

    #or here

if __name__=='__main__':
    #the main obviously...
    a=input("enter the primary url")
    r=requests.get(a)
    #got the page...now let us break it
    content=str(r.text)
    #lets make a soup?
    soup=bs(content)
    #yum yum
    list_of_urls=soup.find_all('a')
    for links in list_of_urls:
        spider(links.get('href'))
        
    
