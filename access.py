import json
import logging
from kiteconnect import KiteConnect
from kiteconnect.connect import KiteConnect
from kiteconnect.ticker import KiteTicker
from kiteconnect import exceptions
def access2(r_t,pnl):
    api_key = "nf3b7k253eeuc9wz"
    kite = KiteConnect(api_key=api_key)
    api_secret = "8q9dnewn0vg0740bjizoatuzlx767f0t"
    request_token = r_t
    data = []
    data = kite.generate_session(request_token, api_secret=api_secret)
    a1 = data["access_token"]
    a2=pnl
    data1 = {"access_token": a1,"pnl":a2}
    with open('data.json', 'w') as outfile:
        json.dump(data1, outfile)
    with open('data.json') as json_file:
        data1 = json.load(json_file)
    print(data1)
    print(data1["access_token"])
