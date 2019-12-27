import re
import requests
import json
from bs4 import BeautifulSoup
import numpy as np
url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.findAll('table', attrs={'id':'octable'})
pager_row = tables[0].findAll('tr')
t_fields = []
fields = pager_row[1].findAll('th')
for x in range(len(fields)):
 t_fields.append(fields[x].text)
print(t_fields)
data = []
for y in range(len(pager_row)):
 t_data = pager_row[y].findAll('td')
 for x in range(len(t_data)):
  a=t_data[x].text
  for k in a.split("\n"):
    b=re.sub(r"[^a-zA-Z0-9]+", ' ', k)
data.append(b)
print(data)
spot_table = soup.findAll('table')
pager_row1 = spot_table[0].find('b')
get_spot_price=pager_row1.text.split(' ')
spot_price=(float(get_spot_price[1]))
print(spot_price)
pager_row2 = tables[0].findAll('tr')
stock_price_data = []
for y in range(len(pager_row2)):
 tb_data=pager_row2[y].findAll('td',attrs={'class':'grybg'})
 for x in range(len(tb_data)):
  stock_price_value=tb_data[x].findAll('b')
  for z in range(len(stock_price_value)):
   ab=float(stock_price_value[z].text)
   stock_price_data.append(ab)
print(stock_price_data)

