import requests
from bs4 import BeautifulSoup
from dotenv import scraper

# Specify the URL to scrap
url = scraper

# send a request
r = requests.get(url)