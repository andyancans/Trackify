from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation, ROUND_DOWN
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from portfolio.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import AddHoldingsForm
import requests
from accounts.models import Holding

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

@login_required
def my_profile(request):
    btc_price = Decimal('0.00')
    eth_price = Decimal('0.00')
    btc_amount = Decimal('0.00')
    eth_amount = Decimal('0.00')
    btc_value = Decimal('0.00')
    eth_value = Decimal('0.00')
    total_value = Decimal('0.00')

    form = AddHoldingsForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            new_holding = form.save(commit=False)
            new_holding.user = request.user
            if new_holding.amount < 0:
                try:
                    current_holding = Holding.objects.get(user=request.user, currency=new_holding.currency)
                    if abs(new_holding.amount) > current_holding.amount:
                        messages.error(request, 'Cannot remove more than you have')
                    else:
                        current_holding.amount += new_holding.amount
                        current_holding.save()
                        if current_holding.amount == 0:
                            current_holding.delete()
                except Holding.DoesNotExist:
                    messages.error(request, 'You do not have any holdings to remove.')
            else:
                current_holding, created = Holding.objects.get_or_create(user=request.user, currency=new_holding.currency)
                current_holding.amount += new_holding.amount
                current_holding.save()
            
            return redirect('my_profile')

    try:
        btc_price, eth_price = fetch_prices()
        btc_price = Decimal(btc_price) if btc_price is not None else Decimal('0.00')
        eth_price = Decimal(eth_price) if eth_price is not None else Decimal('0.00')
    except (TypeError, InvalidOperation):
        btc_price = Decimal('0.00')
        eth_price = Decimal('0.00')

    holdings = Holding.objects.filter(user=request.user)

    btc_amount = sum(Decimal(holding.amount) for holding in holdings.filter(currency='BTC'))
    eth_amount = sum(Decimal(holding.amount) for holding in holdings.filter(currency='ETH'))

    btc_value = btc_amount * btc_price
    eth_value = eth_amount * eth_price

    total_value = btc_value + eth_value

    context = {
        'btc_price': round(btc_price, 2),
        'eth_price': round(eth_price, 2),
        'btc_amount': round(btc_amount, 4),
        'eth_amount': round(eth_amount, 4),
        'btc_value': round(btc_value, 2),
        'eth_value': round(eth_value, 2),
        'total_value': round(total_value, 2),
        'form': form,
    }
    return render(request, 'myprofile.html', context)

@login_required
def add_holdings(request):
    if request.method == 'POST':
        form = AddHoldingsForm(request.POST)
        if form.is_valid():
            currency = form.cleaned_data.get('currency')
            amount = form.cleaned_data.get('amount')
            
            try:
                amount = Decimal(amount).quantize(Decimal('0.000001'))
                
                if amount <= 0:
                    messages.error(request, 'Amount must be greater than zero.')
                    return redirect('add_holdings')

                current_holding, created = Holding.objects.get_or_create(user=request.user, currency=currency)
                current_holding.amount += amount
                current_holding.save()
                messages.success(request, f'Successfully added {amount} {currency}.')
                return redirect('my_profile')
            
            except InvalidOperation:
                messages.error(request, 'Invalid amount entered, Please try again')
                return redirect('add_holdings')
        else:
            messages.error(request, 'Invalid submission, please make sure all fields are filled out correctly')
    
    else:
        form = AddHoldingsForm()
    
    return render(request, 'add_holdings.html', {'form': form})

@login_required
def remove_holdings(request):
    if request.method == 'POST':
        crypto_type = request.POST.get('crypto_type')
        amount = Decimal(request.POST.get('amount'))
        if amount > 0:
            total_removed = remove_holding(request.user, crypto_type, amount)
            if total_removed < amount:
                messages.warning(request, f'Only {total_removed} {crypto_type} was removed, as it was the total amount available')
            else:
                messages.success(request, 'Holding removed successfully!')
        else:
            messages.error(request, 'Amount to remove must be greater than zero.')
        return redirect('my_profile')

def remove_holding(user, crypto_type, amount):
    holdings = Holding.objects.filter(user=user, currency=crypto_type).order_by('amount')
    total_removed = Decimal('0.00')
    for holding in holdings:
        if amount <= 0:
            break
        if holding.amount <= amount:
            total_removed += holding.amount
            amount -= holding.amount
            holding.delete()
        else:
            holding.amount -= amount
            total_removed += amount
            holding.save()
            amount = 0
    return total_removed

@login_required
def remove_holding_by_id(request, holding_id):
    holding = Holding.objects.get(id=holding_id, user=request.user)
    if holding:
        holding.delete()
    return redirect('my_profile')