import logging
from kiteconnect import KiteConnect
from kiteconnect.connect import KiteConnect
from kiteconnect.ticker import KiteTicker
from kiteconnect import exceptions
def access1():
    api_key = "nf3b7k253eeuc9wz"
    logging.basicConfig(level=logging.DEBUG)
    kite = KiteConnect(api_key=api_key)
    print(kite.login_url())
access1()


