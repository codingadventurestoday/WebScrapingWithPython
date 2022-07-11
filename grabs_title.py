import requests
from bs4 import BeautifulSoup as bs 

def get_title(url):
  try: 
#grabs the bytes of the given url 
    html = requests.get(url).content
   except:
    return None
  
  try: 
#creates a beautifulSoup object with the bytes from the data of the given url
    bsObj = bs(html)
#pulls the title from the bsObj at h1 of the body  
    title = bsObj.body.h1
   except:
    return None
   return title
title = get_title('https://www.pythonscraping.com/pages/page1.html')

if title == None:
  print("Title could not be found")
  
else: 
  print(title)
