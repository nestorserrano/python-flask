![Python](https://www.python.org/static/img/python-logo.png)

## Ejemplo Basico del MicroFrame Flask de Python

- Se crea un ejemplo basico de CRUD con Flask y Phyton.
- Se crea manual para instalación de Flask y Librerias
- ✨ Se instala y configura en Heroku con base de datos PostgresSQL ✨

## Librerias

* alembic==1.5.8
* click==7.1.2
* Flask==1.1.2
* Flask-Migrate==2.7.0
* Flask-SQLAlchemy==2.5.1
* Flask-WTF==0.14.3
* greenlet==1.0.0
* gunicorn==20.1.0
* itsdangerous==1.1.0
* Jinja2==2.11.3
* Mako==1.1.4
* MarkupSafe==1.1.1
* psycopg2-binary==2.8.6
* python-dateutil==2.8.1
* python-editor==1.0.4
* six==1.15.0
* SQLAlchemy==1.4.11
* Werkzeug==1.0.1
* WTForms==2.3.3

Este programa se crea en colaboracion con mi amigo [Efrafer](https://github.com/efrafer/nomina "Efrafer")

## Pre-Work

Se realizó todo el Proyecto en **Ubuntu 20.04 LTS**.

Debe Tener instalado los siguientes Programas en la Computadora con las últimas versiones:

```sh
$ sudo apt-get update
$ sudo apt-get upgrade
$ sudo apt-get install python3.9
$ sudo apt install python3-pip
$ sudo apt install -y python3-venv
```

Ver las Versiones de pip, pip3, python y python3 instaladas para el proyecto.

```sh
$ pip --version  # pip 20.0.2
$ pip3 --version # pip 20.0.2
$ python -V # 3.8.5
$ python3 -V # 3.8.5
$ python3.9 -V # 3.9.0
```

# Configurando Heroku desde su página Web

> Todas estas configuraciones son en la página web de Heroku.

En primer lugar debe crear una cuenta en [Heroku](https://signup.heroku.com/login "Heroku")

Una vez dentro de Heroku ir a la opción New >> Create new app en la parte superior derecha de la pantalla.

Coloca el nombre de su aplicacion y selecciona la Región (En mi caso utilicé United States)

Luego pulsar el botón **Create app**

Al Crear la Aplicación con un nombre sin espacios **<YourApp>**, pulsa la opción **Personal** a la izquierda de la pantalla y verá su aplicación creada más abajo, la selecciona se abrirá un menú donde debe seleccionar la última opción **Settings** en el menú de abajo 

Una vez en **Settings** buscar la opción **Buildpacks** y pulsar el botón **Add builpack** a la derecha

Seleccione **python** en la lista de Buildpack en la ventana que se abrió, por último pulse el botón **Save changes**

Luego nos dirigimos a la opción del menú llamada **Resources** 

Buscamos la Sección **Add-ons** y se pulsa el botón a la dereccha **New add-ons**

Seleccionamos desde la ventana que aparece el Add-ons **Heroku Postgres**

Automaticamente nos crea una base de datos y nos da la configuración en el menú **Settings** al seleccionar **Heroku Postgres** en la lista de los **Add-ons**

Tambien se puede crear por consola la base de datos. Para esta práctica se creó desde la página de Heroku

> Regresando a la Consola de Ubuntu 

# Conectarse con Heroku

Instalar Cliente:

```sh
(venv) $ sudo snap install --classic heroku 
```
> Asegúrese de que se haya agregado “/snap/bin” a la ruta. Si no se agrega a la ruta use el siguiente comando

```sh
(venv) $ export PATH=”$PATH:/snap/bin”
(venv) $ heroku --version  # Ver que exista una versión de Heroku instalada
heroku/7.52.0 linux-x64 node-v12.21.0 # Versión que está instalada
(venv) $ heroku login # Ingresar credenciales
```

> Ingresar credenciales en la página web que se abre, sino abre automáticamente pulsar sobre el enlace que ofrece con la tecla ctrl pulsada, le abrirá  una página para que inice sesión en **heroku**, al hacerlo puede cerrar la ventana del explorador y volve a la consola

```sh
(venv) $ heroku git:clone -a <YourAppHeroku>
(venv) $ cd <YourApp> # Entramos al Directorio de Trabajo de nuestra aplicación vacía
```

Git trae la Rama **master** por defecto pero Heroku trabaja con la rama **main**, a continuación los comandos para crear la rama **main** y eliminar la rama **master** en Git local

```sh
(venv) $ git checkout -b main # Se crea la Rama main
(venv) $ git branch -D master # Se elimina la Rama master
(venv) $ git push heroku main # Implemente la aplicación utilizando la nueva rama predeterminada
```

> Los comandos anteriores crean una carpeta de trabajo 

Entrar a esa carpeta

```sh
(venv) $ cd <YourAppHeroku>
```

Se crea y se activa un ambiente de Python para independizar nuestro sistema y luego hacer nuestro primer commit, debe crear el archivo **.gitignore**

```sh
$ pip install virtualenv  # Si no tiene la Dependencia Instalada, se instala
$ python3 -m venv venv # Crea el Ambiente Python en la Carpeta de Trabajo
$ source venv/bin/activate # Activa el Ambiente Python
$ echo venv > .gitignore
$ echo __pycache__ >> .gitignore
(venv) $git add .
(venv) $ git commit -am "Mi primer Commit"
(venv) $ git push heroku main
```
> Si aparece un error de Git que no puede publicar historias no relacionadas, utilice el siguiente comando:

```sh
(venv) $ git pull --allow-unrelated-histories origin main 
```

> Es importante que mientras utiliza el ambiente para este proyecto le otorgue permisos a la carpeta **venv** con el comando chmod 777

```sh
(venv) $ sudo chmod -R 777 venv
```

Se instalan Dependencias de Python que se van a utilizar con el comando **pip**

```sh
(venv) $ pip install flask
(venv) $ pip install Flask-SQLAlchemy
(venv) $ pip install gunicorn
(venv) $ pip install psycopg2-binary
(venv) $ pip install Flask-WTF
(venv) $ pip install sqlalchemy.dialects:postgres
```

Se crea el Archivo requirements.txt con la informacion del comando freeze dentro del Enviroment de Python. 

```sh
(venv) $ pip freeze > requirements.txt
```

Verficar que el archivo **requirements.txt** solo contenga las librerias y dependencias que se usaran en nuestro proyecto ya que puede generar errores en **Heroku** si el archivo de requerimientos trae todas las dependencias de Python Global

# Instalar PostgreSQL Localmente, crear base de datos y crear tabla

> Se puede crear una migración desde la misma aplicación pero este manual permite al usuario aprender tecnicas básicas para crear bases de datos por consola

# Instalar Postgres, crear Super Usuario y crear la base de datos:

```sh
(venv) $ sudo apt-get install postgresql postgresql-contrib # Instalar Postgres
(venv) $ sudo -u postgres createuser --superuser name_of_user # Crear Super Usuario
(venv) $ sudo -u name_of_user createdb name_of_database # Crear base de datos con el usuario creado
```

> Tenga en cuenta que si creó el **name_of_user** y el **name_of_database** como su nombre de usuario en su máquina, puede acceder a esa base de datos con ese usuario con el comando **psql**.

Para este ejemplo se utilizó el usuario por defecto de PostgresSQL  **postgres** y la base de datos **postgres** y se cambió a dicho usuario ya que era diferente al usuario actual

```sh
(venv) $ sudo -i -u postgres # Para cambiar al usuario postgres o en su defecto **name_of_user**
(venv) $ psql # Entra a PostgresSQL y se conecta a la base de datos asociada a ese usuario
    psql (12.6 (Ubuntu 12.6-0ubuntu0.20.04.1))
    Type "help" for help.
```

> Al entrar a la consola de PostgresSQL puede ejecutar el comando **\conninfo** para ver la conexión actual.

```sh
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".
postgres=# 
```
Se crea la tabla en la base de datos 

```sh
postgres=# CREATE TABLE nomina (
postgres=# cedula int NOT NULL PRIMARY KEY,
postgres=# fullname varchar (50) NOT NULL,
postgres=# sueldobas float,
postgres=# bono float,
postgres=# create_at date 
postgres=# ); # Aquí se crea la tabla al pulsar la tecla Enter
```

# Implementación de aplicaciones en Heroku

Crear un archivo **Procfile**, luego subir Archivos de Requerimientos y Procfile

```sh
(venv) $ echo web: gunicorn app:app > Procfile
(venv) $ git add Procfile requirements.txt
(venv) $ git commit -m "Add Heroku deployment files"
```

# Copiar la Tabla de PostgreSQL Local a PostgreSQL Heroku

```sh
(venv) $ heroku pg:push <name_of_database_local> <name_of_database_heroku> --app <YourAppHeroku>
```

Si el comando anterior no funciona y le solicitan las credenciales de su base de datos local puede ejecutar el comando de la siguiente manera:

```sh
(venv) $ PGUSER=postgres PGPASSWORD=password heroku pg:push <name_of_database_local> <name_of_database_heroku> --app <YourAppHeroku>
```

# Comandos utilizados para el manejo de  la Base de datos Heroku

```sh
(venv) $ heroku pg:info # Ver la configuración de la base de datos de Heroku
(venv) $ heroku pg:psql # Iniciar la consola de PostgreSQL
```

Si por alguna razón creó la base de datos y las tablas por consola en heroku puede actualizar la base de datos local con el siguiente comando:

```sh
(venv) heroku pg:pull <name_of_database_heroku> <name_of_database_local> --app <YourAppHeroku>

```

# Ejecutar localmente el Programa:

```sh
(venv) $ FLASK_ENV=development flask run
```

# Por último se obtiene la cadena de conexión de la base de datos

```sh
(venv) $ heroku config --app nomina2021
```

El valor obtenido se utilizará en la variable de la aplicación python **app.py** 

```python
    app = Flask(__name__)
    uri = <valor obtenido comando anterior>
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'cualquierclave'    
```
## Licencia

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

