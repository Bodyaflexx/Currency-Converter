import requests

dict_with_currencies = {}
user_currency = input().lower()
url = f'http://www.floatrates.com/daily/{user_currency}.json'
rates = requests.get(url).json()
if user_currency != 'usd':
    dict_with_currencies['usd'] = float(rates['usd']['rate'])
if user_currency != 'eur':
    dict_with_currencies['eur'] = float(rates['eur']['rate'])

while True:
    currency = input().lower()
    if currency == '':
        break
    amount = float(input())
    print('Checking the cache...')
    if currency in dict_with_currencies:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        dict_with_currencies[currency] = float(rates[currency]['rate'])
    print(f'You received {round(amount * dict_with_currencies.get(currency), 2)} {currency.upper()}.')
