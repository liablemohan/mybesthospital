# from datetime import datetime
# import json
import requests 

# getting inputs for conversions
amount = int(input("Enter the amount: "))
from_currency = input("From Currency code in caps: ").upper()
to_currency = input("To Currency code in caps: ").upper()

dated = input("Enter date (YEAR-MO-00): ")

# declared inputs for debugging
# amount = 10
# from_currency = "USD"
# to_currency = "INR"

# dated = '2022-09-26'


api_key = '7VTZOLJV33IIXQ9H'

# requesting conversion rate
base_url = 'https://www.alphavantage.co/query?function=FX_DAILY'
main_url = base_url + '&from_symbol=' + from_currency + '&to_symbol=' + to_currency + '&apikey=' + api_key 

# storing response 
response = requests.get(main_url)
result = response.json()

# extracting rate and refresh time 
key = result['Meta Data']
daily = result['Time Series FX (Daily)']
date = daily[dated]
rate = float(date['4. close'])
refresh_time = key ['5. Last Refreshed']

# doing conversion
output = rate * amount


# printing results
print("Latest Available: " , refresh_time)
print("current Rate:" , rate , to_currency)
print("amount:" , output , to_currency)