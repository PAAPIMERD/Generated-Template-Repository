import time
from kite_trade import *

enc_t = "rlHk8tuBOkW0zCyZjuSMreBqK3/4uEQ87tUu5sJUApHxEo8+PjJFqGqvM2TA72U8v9Cz2N3a7rxP+mvynMPgqdujoPUJEVmo9Xsztq4ynnV1rvNQYLFHWg=="
email = "avinash9588@gmail.com"
kite = KiteApp(enc_t)

def price_fetcher(symbol):
    price = kite.ltp(["NSE:" + symbol])
    final_price = price["NSE:" + symbol]["last_price"]
    return final_price

while True:
    print(price_fetcher("WIPRO"))


