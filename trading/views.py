# trading/views.py

from django.shortcuts import render
from django.http import JsonResponse
from .trading_bot import fetch_stock_price, execute_trades

def index(request):
    return render(request, 'index.html')

def run_trading_bot(request):
    stock_symbol = 'AAPL'  # Example stock symbol
    stock_data = fetch_stock_price(stock_symbol)

    if stock_data:
        result = execute_trades(stock_data)
        return JsonResponse(result)
    else:
        return JsonResponse({"error": "Failed to fetch stock data"}, status=400)
