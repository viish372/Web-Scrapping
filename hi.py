import requests
from bs4 import BeautifulSoup
url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'
response = requests.get(url)
#print(response)
soup = BeautifulSoup(response.text, "html.parser")
#print(soup)
pager_row=soup.findAll('tr')
for x in range(len(pager_row)):
 print(pager_row[x])
