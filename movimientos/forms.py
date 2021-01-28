from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length
from datetime import date


listaMonedas = ['EUR', 'BTC', 'ETH', 'XRP', 'LTC', 'BCH', 'BNB', 'USDT', 'EOS', 'BSV', 'XLM', 'ADA', 'TRX']

class MovimientosForm(FlaskForm):
    desde = SelectField('From', choices=listaMonedas, validators=[DataRequired()])
    hacia = SelectField('To', choices=listaMonedas, validators=[DataRequired()] )
    q1 = FloatField('Q', validators=[DataRequired()])
    q2 = FloatField('Q', validators=[DataRequired()])
    pu = FloatField('PU', validators=[DataRequired()])

    aceptar = SubmitField('Aceptar')
    cancelar = SubmitField('Cancelar')
    calc = SubmitField('Calcular')