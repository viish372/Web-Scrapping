import json
import logging
from kiteconnect import KiteConnect
from kiteconnect.connect import KiteConnect
from kiteconnect.ticker import KiteTicker
from kiteconnect import exceptions
from datetime import datetime
api_key = "nf3b7k253eeuc9wz"
time1="09:15:00"
time2='09:16:00'
time3="14:55:00"
time4="14:56:00"

kite = KiteConnect(api_key=api_key)
with open('data.json') as json_file:
    data1 = json.load(json_file)
access_token = data1['access_token']
limit= float(data1['pnl'])
kite.set_access_token(access_token)
'''data=kite.holdings()
pnl1=0
for x in range(len(data)):
    data1 = data[x]
    y= data1['pnl']
    pnl1=pnl1+y
pnl=round(pnl1, 2)'''
pos = kite._get("portfolio.positions")
pos1 = pos['net']
pnl1=0
for x in range(len(pos1)):
    pos2 = pos1[x]
    y=pos2['pnl']
    pnl1 = pnl1 + y
pnl = abs(round(pnl1, 2))
print(pnl)
now = datetime.now()
time = now.strftime("%H:%M:%S")

#to get data
fetcheddata = kite.quote(['NSE:IDEA'])
print(fetcheddata)
if(pnl>=limit or (time>=time1 and time<=time2)or (time>=time3 and time<time4)):
    # Retrieve the list of positions.
    pos = kite._get("portfolio.positions")
    pos1 = pos['net']
    print(pos)
    for x in range(len(pos1)):
        pos2 = pos1[x]
        trading_symbol = pos2['tradingsymbol']
        quantity = pos2['quantity']
        print(quantity)

else:
    print("pnl is less than limit")