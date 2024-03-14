## Tesla stock checker
import requests
from datetime import datetime,timedelta

today = datetime.today().strftime('%Y-%m-%d')
yesterday = (datetime.now()-timedelta(1)).strftime('%Y-%m-%d')
two_days_ago = (datetime.now()-timedelta(2)).strftime('%Y-%m-%d')

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
stock_api_key = "2T5F7W0K24X5ILUR"
news_api = "266c915d8b594b0aa2f84a73d39bacdc"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key
}

news_params = {
    "q": COMPANY_NAME,
    "from": two_days_ago,
    "to": today,
    "sortBy": "popularity",
    "apiKey": news_api
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()
# print(stock_data)
yest_stock = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])
two_day_stock = float(stock_data["Time Series (Daily)"][two_days_ago]["4. close"])
perc_diff = abs((two_day_stock - yest_stock) / yest_stock)
if perc_diff >= 0.05:
    print("Get News")
else:
    print(f"Percent difference is {perc_diff*100}%")

response = requests.get(NEWS_ENDPOINT, params= news_params)
response.raise_for_status()
news_data = response.json()
for article in news_data["articles"][0:3]:
    print(article["title"])



