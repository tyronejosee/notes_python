# PyUnit / Unittest

- **Desarrollador(es):** Kent Beck
- **Lanzamiento:** 1990
- **Licencia:** Python Software Foundation License
- **Tipo:** Testing Framework (Pruebas Unitarias)
- [PyUnit: Documentación](https://docs.python.org/3/library/unittest.html)

## Introducción

PyUnit, también conocido como unittest, es un marco de pruebas unitarias integrado en la biblioteca estándar de Python. Su funcionalidad principal radica en proporcionar una estructura para escribir y ejecutar pruebas unitarias de manera sistemática y organizada. El propósito central de PyUnit / Unittest es garantizar la calidad del código al automatizar la verificación de las funcionalidades individuales del software, facilitando la detección temprana de errores y simplificando la tarea de mantenimiento a lo largo del ciclo de vida del proyecto.

## Historia

El marco de pruebas PyUnit fue inspirado por el marco de pruebas JUnit de Java y fue creado por Kent Beck en 2000. Luego, fue adoptado y adaptado para Python como unittest. A lo largo de los años, unittest ha sido ampliamente utilizado en la comunidad de desarrollo de Python para realizar pruebas unitarias y ha sido influyente en la cultura de pruebas en el lenguaje. A pesar de su enfoque más estructurado y detallado en comparación con algunos marcos de pruebas modernos, sigue siendo una opción sólida para proyectos que desean utilizar la biblioteca estándar de Python para sus pruebas.

## Características

- **Clases de Prueba:** Utiliza clases de prueba que heredan de la clase **`unittest.TestCase`** para agrupar y organizar pruebas relacionadas.
- **Métodos de Prueba:** Las pruebas se definen como métodos dentro de las clases de prueba, usando el prefijo "test_".
- **Métodos de Configuración:** Proporciona métodos de configuración como **`setUp`** y **`tearDown`** para preparar y limpiar el estado para cada prueba.
- **Assertions Integradas:** Ofrece una variedad de métodos de aserción (assertions) integrados para verificar condiciones y resultados esperados.
- **Descubrimiento de Pruebas:** Puede descubrir y ejecutar automáticamente pruebas en un módulo o directorio.
- **Reportes Detallados:** Genera informes detallados sobre las pruebas ejecutadas y los resultados obtenidos.
- **Soporte de Cobertura:** Puede integrarse con herramientas de medición de cobertura de código para evaluar la efectividad de las pruebas.
- **Ejecución Programática:** Las pruebas pueden ser ejecutadas programáticamente a través de scripts.
- **Extensibilidad:** Permite la creación de clases de prueba personalizadas y la implementación de métodos adicionales.
