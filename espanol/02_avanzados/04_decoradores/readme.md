# Decoradores

## Definición

Un decorador es un patrón de diseño en Python que permite al usuario agregar nueva funcionalidad a un objeto existente sin modificar su estructura. Los decoradores se suelen llamar antes de la definición de una función que se desea decorar. Las funciones en Python son ciudadanos de primera clase. Esto significa que admiten operaciones como ser pasadas como argumento, devueltas por una función, modificadas y asignadas a una variable. Este es un concepto fundamental que se debe entender antes de adentrarse en la creación de decoradores en Python.

## Propósito

Su propósito principal es agregar funcionalidades adicionales a objetos existentes sin cambiar su implementación interna. Los decoradores actúan como envoltorios alrededor de las funciones o clases, permitiendo agregar código adicional antes o después de su ejecución, sin necesidad de modificar directamente el código original. Esto promueve la modularidad y reutilización de código en Python.

## Resumen

Los decoradores alteran dinámicamente la funcionalidad de una función, método o clase sin tener que usar subclases directamente o cambiar el código fuente de la función que se está decorando. El uso de decoradores en Python también garantiza que tu código sea DRY (Don't Repeat Yourself). Los decoradores tienen varios casos de uso, como:

Autorización en frameworks de Python como Flask y Django.
Registro (logging).
Medición del tiempo de ejecución.
Sincronización.