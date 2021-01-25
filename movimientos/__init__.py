from flask import Flask

#creamos la aplicacion: (aunque creas la aplicación aquí, el punto de entrada sigue siendo run.py)
app = Flask(__name__, instance_relative_config=True) #esto quiere decir que la configuración de la aplicación flask no la voy a hacer directamente en el código, sino que lo voy a hacer de forma relativa.
# de forma relativa quiere decir que en vez de ponerlo así: app.config['DBHost'] = 'localhost', me lo llevo al fichero de configuración.
app.config.from_object('config')

'''
app.config.from_object('config') # esto quiere decir que vamos a crear un fichero config en el directorio raiz y en este fichero vamos a poner la configuración de la aplicación.
# todas la variables (del fichero 'config.py') me las va a cargar en el atributo 'app.config' de la aplicación y voy a poder acceder a ellas cuando quiera.
'''

from movimientos import views  #al hacer esto en app si va a coger la ruta del @app.route('/'). Aqui si que importa el orden. No puedo poner este import al principio.