# Doctest

- **Desarrollador(es):** Tim Peters
- **Lanzamiento:** 2001
- **Licencia:** Python Software Foundation License
- **Tipo:** Módulo Integrado
- [Doctest: Documentación](https://docs.python.org/3/library/doctest.html)

## Introducción

La sección de doctest en Python es una herramienta integrada que permite combinar la creación de documentación y pruebas en un solo proceso. Su propósito principal es proporcionar ejemplos de uso en la docstring de un módulo, clase o función, y luego verificar automáticamente si los resultados obtenidos coinciden con los resultados esperados. De esta manera, se fomenta la creación de documentación actualizada y precisa, al mismo tiempo que se establece un conjunto de pruebas que pueden ser ejecutadas para asegurar el correcto funcionamiento del código. El doctest simplifica el proceso de mantener la documentación y las pruebas sincronizadas, mejorando la calidad del software y la comprensión de su funcionamiento.

## Historia

El doctest fue introducido por Tim Peters en Python 2.1 como una forma de mejorar la documentación y la verificación de código en la biblioteca estándar. Fue influenciado por el módulo "Example" de Modula-3. Desde su incorporación, el doctest ha ganado popularidad por su enfoque en la creación de ejemplos reales en la documentación, lo que permite a los desarrolladores entender rápidamente cómo usar una función o clase mientras se mantienen pruebas automatizadas para garantizar su funcionalidad continua y precisa.

## Carácteristicas

- **Integración de Documentación y Pruebas:** El doctest permite escribir ejemplos de uso directamente en las docstrings del código, creando una relación estrecha entre la documentación y las pruebas automatizadas.
- **Ejecución Automática:** Los ejemplos en las docstrings se ejecutan automáticamente como pruebas cuando se ejecuta el módulo o script, ayudando a identificar rápidamente discrepancias entre los resultados reales y los esperados.
- **Verificación de Salida:** No solo verifica los valores de retorno, sino también la salida impresa, lo que garantiza que los ejemplos sean completos y precisos.
- **Múltiples Opciones de Uso:** Permite una variedad de formatos para indicar la salida esperada, lo que facilita la escritura de ejemplos en docstrings.
- **Herramienta de Línea de Comandos:** Python proporciona una herramienta de línea de comandos, **`doctest`**, que puede utilizarse para ejecutar pruebas doctest de manera independiente.
- **Facilita el Mantenimiento:** El doctest fomenta la actualización regular de la documentación, ya que los ejemplos incorrectos se identifican como fallas de prueba.
- **Enfoque en Ejemplos Reales:** Los ejemplos doctest se asemejan a las interacciones del mundo real, lo que hace que la documentación sea más práctica y comprensible para los desarrolladores.
