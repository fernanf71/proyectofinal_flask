from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length
from datetime import date


listaMonedas = ['EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']

class MovimientosForm(FlaskForm):
    desde = SelectField('From', choices=listaMonedas)
    hacia = SelectField('To', choices=listaMonedas)
    q1 = FloatField('Q', validators=[DataRequired()])
    q2 = FloatField('Q')
    pu = FloatField('P.U.')

    aceptar = SubmitField('Aceptar')
    cancelar = SubmitField('Cancelar')
    calc = SubmitField('Calcular')
    volver = SubmitField('Volver')

class Status(FlaskForm):
    invertido = FloatField('Invertido')
    valorActual = FloatField('Valor actual')
    volver = SubmitField('Volver')