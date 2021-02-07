
from movimientos import app
from movimientos.balance import valorActual
from requests import Request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from config import API_KEY
import json, requests

listaMonedas = ['EUR', 'BTC.', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']

def exchange(desde, q1, hacia):

  url = f'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={q1}&symbol={desde}&convert={hacia}&CMC_PRO_API_KEY={API_KEY}'
      
  respuesta = requests.get(url)

  if respuesta.status_code == 200:
    datos = respuesta.json() # es un metodo del objeto respuesta
    precioTotal = datos['data']['quote'][hacia]['price']
    return precioTotal


'''
def EURexchange():
  
  saldoMonedas = valorActual()
  valorActualEuros = 0

  for desde in saldoMonedas:
    q1 = saldoMonedas[desde]
    
    url = f'https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={q1}&symbol={desde}&convert="EUR"&CMC_PRO_API_KEY={API_KEY}'

    respuesta = requests.get(url)

    if respuesta.status_code == 200:
      datos = respuesta.json() # es un metodo del objeto respuesta
      valorActualEuros  += datos['data']['quote'][hacia]['price']
  return valorActualEuros
  '''