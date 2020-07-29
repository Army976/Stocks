from django.shortcuts import render

def home(request):
	import json
	import requests

	#pk_105a3fc7af8d4b7783bccbb17b5d4048
	api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_105a3fc7af8d4b7783bccbb17b5d4048")

	try:
		api = json.loads(api_request.content)
	except Exception as e:
		api = "Error..."

	return render(request, 'home.html', {'api': api})

def about(request):
	return render(request, 'about.html', {})

