from django.shortcuts import render, redirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

def home(request):
	import json
	import requests

	if request.method == 'POST':
		ticker = request.POST['ticker']
		#pk_105a3fc7af8d4b7783bccbb17b5d4048
		api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker +"/quote?token=pk_105a3fc7af8d4b7783bccbb17b5d4048")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		return render(request, 'home.html', {'api': api})

	else:
		return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

def about(request):
	return render(request, 'about.html', {})

def add_stock(request):
	if request.method == 'POST':
		form = StockForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request, ("Stock Has Been Added!"))
			return redirect('add_stock')
	else:
		ticker = Stock.objects.all()
		return render(request, 'add_stock.html', {'ticker': ticker})

