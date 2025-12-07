import os 
from dotenv import load_dotenv
import requests
load_dotenv()
API_KEY = os.environ.get("API_KEY")
STOCK_ENDPOINT = os.environ.get("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.environ.get("NEWS_ENDPOINT")
STOCK_NAME = "TSLA"


stocks_params = {
    "function":"TIME_SERIES_DAILY",
    "symbol":STOCK_NAME,
    "apikey":API_KEY,
}
response  = requests.get(STOCK_ENDPOINT,params = stocks_params)


#Yesterday Closing Price
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday = data_list[0]
yesterday_closing_price = float(yesterday["4. close"])
print(f"yesterday's price {yesterday_closing_price}")
#day before yesterday price
day_before = data_list[1]
day_before_yesterday_closing_price = float(day_before["4. close"])
print(f"day before yesterday's price {day_before_yesterday_closing_price}")
#Change in the price 
Delta = (day_before_yesterday_closing_price - yesterday_closing_price)
print(Delta)


#percentage Difference :

diff_percentage = (Delta / float(yesterday_closing_price))*100
print(F"{diff_percentage}% change in price since yesterday")

if diff_percentage>5 or diff_percentage < -5:
    print("getNews")