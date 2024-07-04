from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def my_portfolio(request):
    btc_price, eth_price = fetch_prices()

    context = {
        'btc_price': btc_price,
        'eth_price': eth_price,
    }
    return render(request, 'index.html', context)

def fetch_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd'
    }

    response = requests.get(url, params=params)
    data = response.json()

    btc_price = data['bitcoin']['usd']
    eth_price = data['ethereum']['usd']

    return btc_price, eth_price