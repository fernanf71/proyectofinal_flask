
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

api_key = app.config[API_KEY]

def exchange(self):

    url = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={desde}&symbol=BTC&convert={hacia}}&CMC_PRO_API_KEY={api_key}}'
    
    respuesta = request.get(url)

    if respuesta.status == 200:
      print(repuesta.text)
    else:
      print('se ha producido un error', respuesta.status)