import time
from kite_trade import *

enc_t = "rlHk8tuBOkW0zCyZjuSMreBqK3/4uEQ87tUu5sJUApHxEo8+PjJFqGqvM2TA72U8v9Cz2N3a7rxP+mvynMPgqdujoPUJEVmo9Xsztq4ynnV1rvNQYLFHWg=="
email = "avinash9588@gmail.com"
kite = KiteApp(enc_t)

def price_fetcher(symbol):
    start_time = time.time()  # Record the start time
    
    while True:
        try:
            # Attempt to fetch the price
            price = kite.ltp(["NSE:" + symbol])
            final_price = price["NSE:" + symbol]["last_price"]
            return final_price
        except KeyError as e:
            # Handle KeyError
            elapsed_time = time.time() - start_time
            if elapsed_time >= 60:
                # If 60 seconds have passed and price is still not fetched, raise an exception
                raise Exception("Failed to fetch price for symbol {} after 60 seconds".format(symbol))
            
            # Sleep for a short interval before retrying
            time.sleep(0.001)  # Retry every 0.25 seconds

# Call price_fetcher function
start_time = time.time()  # Record the start time of the loop
while True:
    price = price_fetcher('WIPRO')
    print(price)  # Print fetched price
    # Write fetched price to a text file
    with open("price_data.txt", "a") as file:
        file.write(str(price) + "\n")
    
    # Calculate the elapsed time
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Print the elapsed time
    print("Elapsed time for one loop iteration: {:.6f} seconds".format(elapsed_time))
    
    # Reset the start time for the next iteration
    start_time = time.time()

