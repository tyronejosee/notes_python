# Flask

Desarrollador(es): Armin Ronacher

Lanzamiento: Abril 1, 2010

Tipo: Framework Web

Licencia: BSD

- [Flask Website](https://palletsprojects.com/p/flask/)
- [Flask GitHub](https://github.com/pallets/flask)

## Introducción

**Flask** es un micro marco de trabajo web escrito en Python. Se clasifica como un microframework porque no requiere herramientas o bibliotecas particulares. No tiene una capa de abstracción de base de datos, validación de formularios ni ningún otro componente donde las bibliotecas de terceros preexistentes proporcionan funciones comunes. Sin embargo, Flask admite extensiones que pueden agregar características de la aplicación como si estuvieran implementadas en Flask mismo. Existen extensiones para mapeadores objeto-relacional, validación de formularios, manejo de carga, diversas tecnologías de autenticación abierta y varias herramientas comunes relacionadas con marcos de trabajo.

Las aplicaciones que utilizan el marco de trabajo Flask incluyen Pinterest y LinkedIn.

## Historia

Flask fue creado por Armin Ronacher de Pocoo, un grupo internacional de entusiastas de Python formado en 2004. Según Ronacher, la idea originalmente fue una broma del Día de los Inocentes lo suficientemente popular como para convertirse en una aplicación seria. El nombre es un juego de palabras con el marco de trabajo anterior Bottle. Cuando Ronacher y Georg Brandl crearon un sistema de tablón de anuncios escrito en Python en 2004, se desarrollaron los proyectos Pocoo Werkzeug y Jinja.

En abril de 2016, el equipo de Pocoo fue disuelto y el desarrollo de Flask y las bibliotecas relacionadas pasó al recién formado proyecto Pallets.[[11]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-11)[[12]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-12). Desde 2018, los datos y objetos relacionados con Flask se pueden renderizar con Bootstrap.

Flask se ha vuelto popular entre los entusiastas de Python. A partir de octubre de 2020, tiene el segundo mayor número de estrellas en GitHub entre los marcos de trabajo de desarrollo web de Python, ligeramente detrás de Django, y fue votado como el marco de trabajo web más popular en la Encuesta de Desarrolladores de Python 2018, 2019, 2020 y 2021.[[15]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-15)[[16]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-16)[[17]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-17)[[18]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-18)

## Componentes

El microframework Flask es parte de los Proyectos Pallets (anteriormente Pocoo) y se basa en varios otros de ellos, todos bajo una licencia BSD.

### Werkzeug

Werkzeug (en alemán, "herramienta") es una biblioteca de utilidades para el lenguaje de programación Python para aplicaciones de la Interfaz de Pasarela del Servidor Web (WSGI). Werkzeug puede instanciar objetos para solicitudes, respuestas y funciones de utilidad. Se puede utilizar como base para un marco de trabajo personalizado y admite Python 2.7 y 3.5 y versiones posteriores.[[19]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-AR-Werkzeug-19)[[20]](https://es.wikipedia.org/wiki/Flask_(marco_de_trabajo_web)#cite_note-20)

### Jinja

Jinja, también de Ronacher, es un motor de plantillas para el lenguaje de programación Python. Al igual que el marco de trabajo web Django, maneja plantillas en un entorno seguro (sandbox).

### MarkupSafe

MarkupSafe es una biblioteca de manejo de cadenas para el lenguaje de programación Python. El tipo de objeto MarkupSafe extiende el tipo de cadena de Python y marca su contenido como "seguro"; al combinar MarkupSafe con cadenas regulares, las cadenas no marcadas se escapan automáticamente, evitando la doble escape de cadenas ya marcadas.

### ItsDangerous

ItsDangerous es una biblioteca segura de serialización de datos para el lenguaje de programación Python. Se utiliza para almacenar la sesión de una aplicación Flask en una cookie sin permitir que los usuarios manipulen el contenido de la sesión.

## Características

- Servidor de desarrollo y depurador
- Soporte integrado para pruebas unitarias
- Despacho de solicitudes RESTful
- Usa la plantilla Jinja
- Soporte para cookies seguras (sesiones del lado del cliente)
- 100% compatible con WSGI 1.0
- Basado en Unicode
- Documentación completa
- Compatibilidad con Google App Engine
- Extensiones disponibles para ampliar la funcionalidad

## Ejemplo

El siguiente código muestra una aplicación web simple que muestra "¡Hola Mundo!" cuando se visita:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello() -> str:
    return "¡Hola Mundo!"

if __name__ == "__main__":
    app.run()
```
