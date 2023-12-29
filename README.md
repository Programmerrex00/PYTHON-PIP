# Game Proyect

Para correr el juego debes seguir las siguientes instrucciones en la terminal:

```sh
cd game
python3 main.py 
```

Con el comando pip3 freeze para ver las librerias que tenemos instaladas

cuando tenermos una version antigua de cual sea la libreria e instalamos una version actual nos la desistalara e instalara la otra
ejm: pip3 install matplotlib==3.5.0 por pip3 install matplotlib==3.8.2


```
Hola Chicos! :D Verificar donde esta python y pip

which python3

which pip3

Si estas en linus o wsl debes instalar

sudo apt install -y python3-venv
Poner cada proyecto en su propio ambiente, entrar en cada carpeta.

python3 -m venv env
Activar el ambiente

source env/bin/activate
Salir del ambiente virtual

deactivate
Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo

pip3 install matplotlib==3.5.0
Verificar las instalaciones

pip3 freeze
```

pdt
luego de activar el ambiente virtual ejecutamos los comando which python3 o pip3 y veremos que estamos en otra rut
si ejecutamos el comando pip3 freeze veremos que no tenemos ninguna libreria ya que el ambiente virutal los omitio, toca volver a instalarlas


# Para tener en cuenta sobre requirements.txt

Generar el archivo con el siguiente comando

pip3 freeze > requirements.txt
Revisar lo que hay dentro del archivo

cat requirements.txt
Instalar las dependencias necesarias para contribuir más rápido en proyectos

pip3 install -r requirements.txt
Preparar archivo para contribución


# App Project
```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py

code . -r es para reutilizar la ventana de vsc

- Recuerda al hacer un un fork lo que hacemos es agregar el repositorio de github a nuestra variadad de repositorios y luego de eso hacemos los cambios necesarios para hacer el pull request al repositorio original y esperar que el dueño del repositorio acepte los cambios


paso a paso:

Crear un entorno

python3 -m venv env
Activar un entorno virtual

source env/bin/activate
Verificar que estemos dentro del entorno virtual

which python3
Instalar la dependencia dentro del entorno virtual

pip3 install requests
Verificar la instalacion

pip3 freeze
Crear el archivo para que cualquier persona pueda desplegar el proyecto

pip freeze > requeriments.txt
STORE


import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    for category in categories:
        print(category['name'])
MAIN


import store

def run():
    store.get_categories()

if __name__ == '__main__':
    run()


# OTRA EXPLICACION:

Hola Chicos! :D PANDAS

Es una de las librerias mas utilizadas en python y nos sirven para analizar y manipular datos de archivos duros
Activar anbiente del proyecto


source env/bin/activate
Verificar


which python3
Ver que hay dentro del archivo en el cual se evidencia que no hay pandas


cat reqruirements.txt
Agregar nueva libreria


pip3 install pandas
Verificar librerias instaladas


pip3 freeze
Actualizar el documento que contiene las librerias


pip3 freeze > requirements.txt


# Siguiente ejemplos instalamos fastapi y uvicorn (Version estander)(Servidor donde estara corriendo nuestra api)
pip3 install fastapi, en el entorno virtual de web-server 
pip3 install "uvicorn[standard]"

De esta manera iniciamos el servidor: uvicorn main:app --reload





Instalación en Ubuntu 🐧
Estos son los pasos para instalarlo dentro de Ubuntu, sin embargo, también puedes ver directamente Install Docker Engine on Ubuntu

sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo docker run hello-world




Comando para la construccion y levantamiento de mi contenedor en docker:

$  sudo docker-compose build

$  sudo docker-compose ps

$  sudo docker-compose up -d

$  sudo docker-compose exec app-csv bash

$ para bajar el contenedor lo hacemos con docker-compose down