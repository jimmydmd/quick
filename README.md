# Prueba desarrollador Django

# Requisitos
    - docker 
    - docker-compose

# Instalacion 

Instalacion de entorno virtual dentro de la carpeta raiz del proyecto
    python -m venv venv

activacion entorno virtual 
	cd venv\Scripts
	activate

instalar requerimientos (dentro del archivo requirements.txt se encuentra la django, djangorestframework y psycopg2 "libreria para conexion a db")
    pip install -r requirements.txt

Se crea un nuevo proyecto utilizando el contenedor "web" descrito en el docker-compose.yml
    docker-compose run web django-admin startproject project_quick . 

Se debe configurar la clave "ALLOWED_HOSTS"  en el archivo settings.py permitiendo el trafico a nuestro contenedor
    ALLOWED_HOSTS = ['*']

Se inicia nuevamente el docker-compose
	docker-compose up

En  otra terminal podemos ejecutar las migraciones 
	docker-compose run web python manage.py makemigrations
	docker-compose run web python manage.py migrate

Se crean las apps requeridas 
    docker-compose run web  python manage.py startapp clients
    docker-compose run web  python manage.py startapp bills
    docker-compose run web  python manage.py startapp products
    docker-compose run web  python manage.py startapp bills_products

# Despliegue 

Una vez descargado el repo, el proyecto se construye con estos comandos
    docker-compose up --build

# Apis
    "clients": "http://localhost:8000/api/clients/",
    "bills": "http://localhost:8000/api/bills/",
    "products": "http://localhost:8000/api/products/",
    "bills_products": "http://localhost:8000/api/bills_products/"

# Consumo apis

Se realiza mediante JSON Web Token en el header utilizando el token

    key:Authorization
    value:Token c20987a10f19fa61ecaba8117febc816d0a59075

# Registro

El registro se realiza mediante un formulario con correo, nombre de usuario y contraseña 

    http://localhost:8000/register/

# Login 

El login se realiza mediante correo y contraseña anteriormente creados

    http://localhost:8000/login/
    user:jimmy@test.com
    pw:123456

# Exportacion de archivo .csv

El archivo contiene datos del cliente ademas de las facturas asociadas con el nombre de la compañia
    http://localhost:8000/export/

# Importacion de archivo .csv

La importacion se hace desde un archivo .csv para la creacion de clientes
    http://localhost:8000/import/

Ejemplo de contenido de archivo .csv (delimitado con ,)
    id, document, first_name, last_name, email
    12, 23233223, kkkk, lll, kk@test.com
