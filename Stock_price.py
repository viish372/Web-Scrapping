import re
import requests
import json
import numpy as np
from bs4 import BeautifulSoup
url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.findAll('table', attrs={'id':'octable'})
#code to print completely data
'''pager_row = tables[0].findAll('tr')
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
print(data)'''
#code for spot price
spot_table = soup.findAll('table')
pager_row1 = spot_table[0].find('b')
get_spot_price=pager_row1.text.split(' ')
spot_price=(float(get_spot_price[1]))
print('spot price=',spot_price)
#code for stock price col
pager_row2 = tables[0].findAll('tr')
stock_price_data = []
for y in range(len(pager_row2)):
 tb_data=pager_row2[y].findAll('td',attrs={'class':'grybg'})
 for x in range(len(tb_data)):
  stock_price_value=tb_data[x].findAll('b')
  for z in range(len(stock_price_value)):
   ab=float(stock_price_value[z].text)
   stock_price_data.append(ab)
#print(stock_price_data)
#code to print lowest stock price
def closest(stock_price_data,spot_price):
 stock_price_data = np.asarray(stock_price_data)
 idx = (np.abs(stock_price_data - spot_price)).argmin()
 return stock_price_data[idx]
nearest_value=closest(stock_price_data, spot_price)
print('nearest value=',nearest_value)
#CODE to find index of nearest value
nearest_value_index=stock_price_data.index(nearest_value)
nearest_value_index=nearest_value_index+2
print('nearest_value_index=',nearest_value_index)
#code to find row releted to nearest value of stock price
nearest_value_row_data=[]
pager_row3 = tables[0].findAll('tr')
tb_data1=pager_row3[nearest_value_index].findAll('td')
for y in range(len(tb_data1)):
#tb_data1=pager_row3[nearest_value_index]
 i=tb_data1[y].text
 nearest_value_row_data.append(i)
#to get iv
iv1=nearest_value_row_data[4]
iv2=nearest_value_row_data[18]
print(nearest_value_row_data[11])
print('IV for calls=',iv1)
print('IV for puts=',iv2)
#to find OI data for puts
pager_row4 = tables[0].findAll('tr')
temp_puts_oi = []
temp_puts_change_in_oi = []
for y in range(len(pager_row4)):
 put_data=pager_row4[y].findAll('td',attrs={'class':'nobg'})
 if y==nearest_value_index:
  break
 for x in range(len(put_data)):
  if(x==9):
   print(put_data[x])
   p=put_data[x].text
   temp_puts_oi.append(p)
# print('-------------------------------------------------')
''' if(x==8):
print(put_data[x])
p=put_data[x].text
temp_puts_change_in_oi.append(p)'''
#print(temp_puts_data)
#for x in range(len(temp_puts_data)):
# print(temp_puts_data[x])
'''for x in range(len(temp_puts_data)):
if(temp_puts_data)==('-'):
temp_puts_data[x].replace('-','0')
print(temp_puts_data[x])'''
#for x in range(len(puts_data)):
# if(x%9==0):
#print(puts_data[x])
# calls_oi_value=.findAll('b')
# for z in range(nearest_value_index):
# ab=float(stock_price_value[z].text)
# calls_oi_data.append(ab)tb_data[x]
