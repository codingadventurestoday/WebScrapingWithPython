import requests 
from bs4 import BeautifulSoup as bs 

def create_obj(url):
    try: 
        html = requests.get(url).content
    except:
        return None 
      
    try: 
        bsObj = bs(html)
    except:
        return None 
    return bsObj  
   
bsObj = create_obj('https://www.pythonscraping.com/pages/warandpeace.html')
if bsObj == None:
    print('could not grab website')
    
else:
    try:
      """bsObj.findAll(tageName, tagAttributes gets a complete list of the tags on the page""""
        nameList = bsObj.findAll('span', {'class': 'green})
""" get_text() method strips all of the tags from the doc you are working with and returns a text only string"""
        for name in nameList:
            print(name.get_text())
    expect: 
        print('Could not grab the span tags in the bsObj')
                                                                       
