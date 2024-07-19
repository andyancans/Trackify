from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from portfolio.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
import requests

# Create your views here.

def fetch_prices():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum',
        'vs_currencies': 'usd'
    }
    
    response = requests.get(url, params=params)
    data = response.json()

    btc_price = data.get('bitcoin', {}).get('usd')
    eth_price = data.get('ethereum', {}).get('usd')

    return btc_price, eth_price

def my_portfolio(request):
    btc_price, eth_price = fetch_prices()

    context = {
        'btc_price': btc_price,
        'eth_price': eth_price,
    }
    return render(request, 'index.html', context)

