import requests
from bs4 import BeautifulSoup

url = "https://www.nseindia.com/live_market/dynaContent/live_watch/fxTracker/optChainDataByExpDates.jsp"

page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
item = soup.select_one("div:contains('REFERENCE RATE') > strong").text
print(item)
