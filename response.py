import json
import logging
from kiteconnect import KiteConnect
from kiteconnect.connect import KiteConnect
from kiteconnect.ticker import KiteTicker
from kiteconnect import exceptions
def access2():
    api_key = "nf3b7k253eeuc9wz"
    kite = KiteConnect(api_key=api_key)
    api_secret = "8q9dnewn0vg0740bjizoatuzlx767f0t"
    request_token = "PWOx3hgEcruPJLHqNJ3ztwHJZsccMIIm"
    data = []
    data = kite.generate_session(request_token, api_secret=api_secret)
    return(data)
    print(data)
data=access2()
a1=data["access_token"]
access_token={"access_token":a1}
with open('access_token.json', 'w') as outfile:
    json.dump(access_token, outfile)
with open('access_token.json') as json_file:
    data1 = json.load(json_file)
print(data1)
#print(data["access_token"])