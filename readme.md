# Instalacion

Para crear un entorno virtual, en el terminal y dentro de la ruta del proyecto, incluir la siguiente instrucción:

        python -m venv venv

Para activar el entorno virtual, incluir la siguiente instrucción:

        venv\Scripts\activate


Se deberá crear un fichero con el nombre ".env" colgando del la carpeta principal "PROYECTO FINAL" e incluyendo las siguientes variables de entorno:

FLASK_APP=run.py
FLASK_ENV=development

Para desactivar este entorno, con el siguiente comando:

        venv\Scripts\deactivate

Para crear una variable de entorno 'FLASK_APP' y asignarle el archivo principal (run.py), se debe escribir en el terminal:

        set FLASK_APP=run.py

## Instalación de Dependencias
- Para instalar dependencias ejecutar:
        pip install -r requeriments.txt

## Obtención de la API coinmarket

  Para ejecutar el programa se requerirá API de https://coinmarketcap.com/. La documentación de la API se encuentra en:

        https://coinmarketcap.com/api/documentation/v1/

Se deberá obtener una API KEY que se incluirá en el fichero config.py (ver apartado "Fichero de configuración")

## Creación de la Base de Datos

Para crear la BBDD considere un programa para gestión de BBDD en SQLite (DB Browser). Puede considerar una heramienta para que facilite el manejo de la BBDD de manera gráfica. En el siguiente enlace puede descarlo:
        https://sqlitebrowser.org/

Se tendrá que hacer uso de la sentencia SQL para crear la tabla necesaria. Esta sentencia se encuentra en el fichero "initial.sql" en la ruta:

        movimientos/data/migrations/basededatos.db

La base de datos deberá crearse a través de la siguiente ruta:
        
        movimientos\data\basededatos.db

## Fichero de configuración

Se deberá renombrar el ficher "config_template.py" por "config.py" e incluir la siguiente información:

SECRET_KEY='Ponga aquí su clave para CSRF'
DBFILE = 'Ponga aquí la ruta a la base de datos'
API_KEY='Ponga aquí su API KEY de Coinmarket'

## Ejecución

Una vez realizado lo anterior, se ejecutará el proyecto a través de la siguiente instrucción en el terminal:

        flask run
