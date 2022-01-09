import requests
from notifypy import Notify


def get_price_data():
	'''
		This function requests to a public API without api key
		and get bitcoin's buy price data.
		if you get Connection refused error,
		connect to a safe VPN then run the script :)
	'''
	response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
	price = float(response.json()['data']['amount'])
	return price

def sendmessage():
	notification = Notify()
	notification.title = "Important"
	message = 'At this moment bitcoin is ' + str(get_price_data()) + ' dollars'
	notification.message = message
	notification.audio = "./bell.wav"
	notification.send()


sendmessage()

