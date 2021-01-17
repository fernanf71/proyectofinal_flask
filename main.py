
 #This example uses Python 2.7 and the python-request library. Ver video FLASK min 1:50
from flask import Flask  #importamos la clase de aplicación FLASK
from coinmarketcap import Market
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

app = Flask(__name__) #creamos una instancia de la aplicación y como parámetro, el nombre de la aplicación, exactamente, el nombre de nuestro fichero


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'e3543c4a-2915-4aa8-805a-2b7f47213f26',
}

#hacer petición htpp
respuesta = requests.get(url, params=parameters, headers=headers)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()  #para transformar el texto de la respuesta en un json. Esto es un método del objeto response => respuesta.
    print(datos)
else:
    print('Se ha producido un error', respuesta.status_code)

@app.route('/')  # hay un método route dentro de FLASK, que actua como un decorador.
def movimientos():  # a app route pasa como parámetro la función movimientos.
  return '<h1>You are on the home page</h2>'


if __name__=='__main__':  # __name__ es una variable y se relaciona con 'app = Flask(__name__)'
  app.run()