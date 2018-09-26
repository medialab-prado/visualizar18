Taller de webscraping (25/09/2018)
==================================

## Antes de empezar

Necesitamos tener instalado el lenguaje de progranmación **Python** (versión 3.x) y el gestor de paquetes de python **Pip**. Algunas referencias para instalarlo en:

* [GNU/Linux](https://www.tecmint.com/install-pip-in-linux/)
* [Mac OS X](https://ahmadawais.com/install-pip-macos-os-x-python/)
* [Windows](http://www.steptoinstall.com/python-install-pip-on-windows-7-windows-8.html)

Una vez instalado Python y Pip debes ejecutar en la terminal los siguientes comandos para cargar las librerías que usaremos.

```
pip install requests

pip install beautifulsoup

pip install lxml

pip install wget
```

## Ficheros

Cada uno de los ficheros es un script escrito en Python y que hace uso de las librerías instaladas con Pip, pero cada uno con un método y proposito diferente.

* **get_emails.py**: Obtiene todos los emails de una página web
* **get_images.py**: Ontiene todas las imágenes de una página web
* **get_headings_from_urls.py**: Obtiene todos los títulos de ls noticias de la portada de lazaron.es
* **get_keywords_from_urls.py**: Obtiene todos *keywords* de un conjunto de páginas webs (incluídas en el fichero urls.txt)

## Ejecución

Abre la terminal y escribe:

```
python nombre_del_fichero.py
```

## Otras feferencias

* [Extracción de datos con herramientas digitales](https://speakerdeck.com/pr3ssh/extraccion-de-datos-para-el-desarrollo-con-herramientas-digitales)
* [Todas las presentaciones](https://speakerdeck.com/pr3ssh/)
