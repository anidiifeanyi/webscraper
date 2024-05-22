from bs4 import BeautifulSoup
import requests

# Specify the URL to scrap
scrap = 'https://zerotomastery.io/courses/'
url = scrap

# send a request
r = requests.get(url)

# Get data 
soup = BeautifulSoup(r.content, 'lxml')

#select the data to scrap
title = soup.find_all('a', {'class':'general-cardstyles__CardTitle-sc-1cdshrd-3 jtxsIx'})

# display specific data
for title_text in title:
  print(title_text.getText())
  
  