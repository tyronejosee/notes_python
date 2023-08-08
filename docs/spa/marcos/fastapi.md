# FastAPI

- Desarrollador(es): Sebastián Ramírez
- Lanzamiento: Diciembre 5, 2018
- Tipo: Framework Web
- Licencia: MIT
- [FastAPI Website](https://fastapi.tiangolo.com/)
- [FastAPI GitHub](https://github.com/tiangolo/fastapi)

## Introducción

**FastAPI** es un moderno framework para construir [APIs](https://es.wikipedia.org/wiki/Interfaz_de_programaci%C3%B3n_de_aplicaciones) [RESTful](https://es.wikipedia.org/wiki/Transferencia_de_estado_representacional) en [Python](https://es.wikipedia.org/wiki/Python_(lenguaje_de_programaci%C3%B3n)). Fue lanzado por primera vez en 2018 y ha ganado rápidamente popularidad entre los desarrolladores debido a su facilidad de uso, velocidad y robustez. FastAPI se basa en Pydantic y utiliza indicadores de tipo para [validar](https://es.wikipedia.org/wiki/Validaci%C3%B3n_de_datos), [serializar](https://es.wikipedia.org/wiki/Serializaci%C3%B3n) y deserializar datos. También genera automáticamente documentación [OpenAPI](https://es.wikipedia.org/wiki/OpenAPI) para las APIs construidas con él.[[3]](https://es.wikipedia.org/wiki/FastAPI#cite_note-3)

FastAPI soporta completamente la programación [asincrónica](https://es.wikipedia.org/wiki/Programaci%C3%B3n_as%C3%ADncrona) y puede ejecutarse en servidores [Gunicorn](https://es.wikipedia.org/wiki/Gunicorn) y [ASGI](https://es.wikipedia.org/wiki/Interfaz_de_pasarela_del_servidor_as%C3%ADncrono) como Uvicorn e Hypercorn,[[4]](https://es.wikipedia.org/wiki/FastAPI#cite_note-4) lo que lo convierte en una buena elección para entornos de producción. Para mejorar la amigabilidad para los desarrolladores, el soporte del editor se tuvo en cuenta desde los primeros días del proyecto.[[5]](https://es.wikipedia.org/wiki/FastAPI#cite_note-5)

## Adopción y Uso en el Mundo Real

FastAPI fue el tercer framework web más querido en la Encuesta de Desarrolladores de Stack Overflow 2021.

T. Danka enfatizó su valor para aplicaciones de ciencia de datos.

Grandes empresas como Uber y Netflix lo utilizan para desarrollar algunas de sus aplicaciones.

## Ejemplo

El siguiente código muestra una aplicación web simple que muestra "¡Hola Mundo!" cuando se visita:

```python
**from** **fastapi** **import** FastAPI

app = FastAPI()

@app.get("/")
**def** read_root():
    **return** "Hola Mundo!"

```
