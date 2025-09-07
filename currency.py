import requests

API_KEY = 'fca_live_Twwg0XElqphJketbmTKdRqXKpAOxLe7LPyqWbuRu'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD',]

def convert_currency(base):
    currencies = ','.join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]

    except Exception as e:
        print(f"Error: {e}")
        return None

while True:
    base = input("Enter base currency (e.g., USD, EUR, Q to quit): ").upper()
    if base == "Q":
        break

    data = convert_currency('base')
    if not data:
        print("Failed to retrieve data. Please try again.")
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {value}")

