from bs4 import BeautifulSoup
import requests

# Fetch HTML from the ALL Pages Site
url = "https://yugioh.fandom.com/wiki/Special:AllPages"
req = requests.get(url)

soup = BeautifulSoup(req.text,'html.parser')
print(soup.select(".mw-allpages-body"))
