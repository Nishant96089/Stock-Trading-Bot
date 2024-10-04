# trading/trading_bot.py

import requests

def fetch_stock_price(symbol):
    api_key = 'P3LV41HIJUPXE9TQ'  # Replace with your actual Alpha Vantage API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}"
    response = requests.get(url)
    data = response.json()

    if 'Time Series (1min)' in data:
        return data['Time Series (1min)']
    else:
        print(f"Error: 'Time Series (1min)' not found in response for {symbol}")
        print(data)  # Log the response for debugging
        return None

def execute_trades(stock_data):
    # Implement a simple trading logic, for example:
    for time, price_data in stock_data.items():
        close_price = float(price_data['4. close'])
        # Example: Buy when the stock price drops by 2%, Sell when it rises by 3%
        # This can be extended to include more sophisticated strategies
        print(f"Close price at {time}: {close_price}")
    return {"status": "Trading executed"}
