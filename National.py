import re
import requests
import json
import numpy as np
from bs4 import BeautifulSoup
url = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
tables = soup.findAll('table', attrs={'id':'octable'})
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
#code to get lowest stock price
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
 i=tb_data1[y].text
 nearest_value_row_data.append(i)
#to get iv
iv1=nearest_value_row_data[4]
iv2=nearest_value_row_data[18]
print(nearest_value_row_data[11])
print('IV for calls=',iv1)
print('IV for puts=',iv2)
#to find data for puts
pager_row4 = tables[0].findAll('tr')
temp_puts_oi = []
puts_oi=[]
temp_puts_change_in_oi = []
puts_change_in_oi=[]
temp_puts_volume=[]
puts_volume=[]
for y in range(len(pager_row4)):
 put_data=pager_row4[y].findAll('td',attrs={'class':'nobg'})
 if y==nearest_value_index:
  break
 for x in range(len(put_data)):
  if(x==9):
   p=put_data[x].text
   temp_puts_oi.append(p)
  if(x==8):
   q=put_data[x].text
   temp_puts_change_in_oi.append(q)
  if(x==7):
   r=put_data[x].text
   temp_puts_volume.append(r)
#puts data conversion
for x in range(len(temp_puts_oi)):
 a=temp_puts_oi[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 puts_oi.append(float(a))
for x in range(len(temp_puts_change_in_oi)):
 a=temp_puts_change_in_oi[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 puts_change_in_oi.append(float(a))
for x in range(len(temp_puts_volume)):
 a=temp_puts_volume[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 puts_volume.append(float(a))
#to find data for calls
temp_calls_oi = []
calls_oi=[]
temp_calls_change_in_oi = []
calls_change_in_oi=[]
temp_calls_volume=[]
calls_volume=[]
pager_row5 = tables[0].findAll('tr')
nearest_value_index2=nearest_value_index+1
print(nearest_value_index2)
print(len(pager_row5))
for y in range(nearest_value_index2,len(pager_row5)-1):
 call_data=pager_row5[y].findAll('td',attrs={'class':'nobg'})
 for x in range(len(call_data)):
  if(x==0):
   p=call_data[x].text
   temp_calls_oi.append(p)
  if(x==1):
   q=call_data[x].text
   temp_calls_change_in_oi.append(q)
  if(x==2):
   r=call_data[x].text
   temp_calls_volume.append(r)
#calls data conversion
for x in range(len(temp_calls_oi)):
 a=temp_calls_oi[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 calls_oi.append(float(a))
for x in range(len(temp_calls_change_in_oi)):
 a=temp_calls_change_in_oi[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 calls_change_in_oi.append(float(a))
for x in range(len(temp_calls_volume)):
 a=temp_calls_volume[x].strip().replace(",",'') 
 if(a)==('-'):
  a=0
 calls_volume.append(float(a))
#print(calls_oi)
#print(calls_change_in_oi)
#print(calls_volume)
#to find largest
def largest(arr,n):
 max = arr[0]
 for i in range(1, n):
  if arr[i] > max:
   max = arr[i]
 return max
n = len(temp_puts_change_in_oi)
print("---------------puts data-------------------")
l1 = largest(puts_oi,n)
print ("Largest puts oi",l1)
puts_oi_index=puts_oi.index(l1)
sp_puts_oi=stock_price_data[puts_oi_index]
print("largest stock price for puts oi",sp_puts_oi)
l2 = largest(puts_change_in_oi,n)
print ("Largest puts change in oi",l2)
puts_change_in_oi_index= puts_change_in_oi.index(l2)
sp_puts_change_in_oi=stock_price_data[puts_change_in_oi_index]
print("largest stock price for puts change in oi",sp_puts_change_in_oi)
l3 = largest(puts_volume,n)
print ("Largest  puts volume",l3)
puts_volume_index= puts_volume.index(l3)
sp_puts_volume=stock_price_data[puts_volume_index]
print("largest stock price for puts volume",sp_puts_volume)
n1=len(temp_calls_change_in_oi)
print("---------------calls data-------------------")
l4 = largest(calls_oi,n1)
print ("Largest calls oi",l4)
calls_oi_index= len(puts_oi)+calls_oi.index(l4)+1
sp_calls_oi=stock_price_data[calls_oi_index]
print("largest stock price for calls oi",sp_calls_oi)
l5 = largest(calls_change_in_oi,n1)
print ("Largest calls change in oi",l5)
calls_change_in_oi_index= len(puts_oi)+calls_change_in_oi.index(l5)+1
sp_calls_change_in_oi=stock_price_data[calls_change_in_oi_index]
print("largest stock price for calls change in oi",sp_calls_change_in_oi)
l6 = largest(calls_volume,n1)
print ("Largest calls volume",l6)
calls_volume_index= len(puts_oi)+calls_volume.index(l6)+1
sp_calls_volume=stock_price_data[calls_volume_index]
print("largest stock price for calls volume",sp_calls_volume)
