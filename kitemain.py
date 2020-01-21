import json
import logging
from kiteconnect import KiteConnect
from kiteconnect.connect import KiteConnect
from kiteconnect.ticker import KiteTicker
from kiteconnect import exceptions
from datetime import datetime
api_key = "nf3b7k253eeuc9wz"
limit=80.00
time1="09:15:15"
time2="14:30:01"
kite = KiteConnect(api_key=api_key)
with open('access_token.json') as json_file:
    data1 = json.load(json_file)
access_token = data1['access_token']
#print(access_token)
#print(access_token)
kite.set_access_token(access_token)
#get pnl
data=kite.holdings()
#print(data)
pnl1=0
for x in range(len(data)):
    data1 = data[x]
    y= data1['pnl']
    pnl1=pnl1+y
pnl=round(pnl1, 2)
#print(pnl)
#get current time
now = datetime.now()
time = now.strftime("%H:%M:%S")
#print(type(time))
#print(kite.orders())
#abc=kite.cancel_order()
#to get data
fetcheddata = kite.quote(['NSE:IDEA'])
#print(fetcheddata)
if(pnl>limit or time>=time1 or time>=time2):
    # Retrieve the list of positions.
    pos = kite._get("portfolio.positions")
    pos1 = pos['net']
    for x in range(len(pos1)):
        pos2 = pos1[x]
        trading_symbol = pos2['tradingsymbol']
        exchange = pos2['exchange']
        quantity = pos2['quantity']
        product = pos2['product']
        product1 = 'kite.PRODUCT_'+product
        a=[product1]
        print(a)
        if (quantity > 0):
            try:
                order_id = kite.place_order(tradingsymbol=trading_symbol,
                                            exchange=kite.EXCHANGE_NSE,
                                            transaction_type=kite.TRANSACTION_TYPE_SELL,
                                            quantity=quantity,
                                            order_type=kite.ORDER_TYPE_MARKET,
                                            product=kite.PRODUCT_MIS,
                                            variety=kite.VARIETY_REGULAR)
                logging.info("Order placed. ID is: {}".format(order_id))
                print("placed")
                print("order_id")
            except Exception as e:
                print("not placed")
                logging.info("Order placement failed: {}".format(e.message))
        else:
            print("quantity else sell")
        if(quantity < 0):
            # buy sell
            try:
                order_id = kite.place_order(tradingsymbol=trading_symbol,
                                            exchange=kite.EXCHANGE_NSE,
                                            transaction_type=kite.TRANSACTION_TYPE_BUY,
                                            quantity=abs(quantity),
                                            order_type=kite.ORDER_TYPE_MARKET,
                                            product=kite.PRODUCT_MIS,
                                            variety=kite.VARIETY_REGULAR)
                logging.info("Order placed. ID is: {}".format(order_id))
                print("placed")
            except Exception as e:
                print("not placed")
                logging.info("Order placement failed: {}".format(e.message))
        else:
            print("quantity else buy")

else:
    print("pnl else")
#print(kite._get("portfolio.positions"))
'''if(pnl>limit or time==time1 or time==time2):
    pos = kite.positions()
    print(pos)
    kite.cancel_order()
    #print("exit position")

else:
    print("enter choice 1.buy 2.sell")
    ch=int(input("1/2"))
    if(ch==1):
        # buy sell
        try:
            order_id = kite.place_order(tradingsymbol="IDEA",
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_BUY,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML,
                                        variety=kite.VARIETY_REGULAR)
            logging.info("Order placed. ID is: {}".format(order_id))
            print("placed")
        except Exception as e:
            print("not placed")
            logging.info("Order placement failed: {}".format(e.message))
    if (ch == 2):
        # sell shares
        try:
            order_id = kite.place_order(tradingsymbol="IDEA",
                                        exchange=kite.EXCHANGE_NSE,
                                        transaction_type=kite.TRANSACTION_TYPE_SELL,
                                        quantity=1,
                                        order_type=kite.ORDER_TYPE_MARKET,
                                        product=kite.PRODUCT_NRML,
                                        variety=kite.VARIETY_REGULAR)
            logging.info("Order placed. ID is: {}".format(order_id))
            print("placed")
        except Exception as e:
            print("not placed")
            logging.info("Order placement failed: {}".format(e.message))'''



# Fetch all orders
#print(kite.orders())
# Get instruments
#print(kite.instruments())

#__all__ = ["KiteConnect", "KiteTicker", "exceptions"]


