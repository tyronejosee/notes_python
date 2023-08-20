# Entornos Virtuales

## Introducción

Los entornos virtuales son herramientas esenciales en el desarrollo de software que permiten a los programadores crear ambientes aislados y autónomos para gestionar dependencias y configuraciones específicas de proyectos. Estos entornos son particularmente útiles cuando se trabaja en múltiples proyectos que podrían requerir diferentes versiones de bibliotecas y paquetes. Al proporcionar una forma de encapsular las dependencias, los entornos virtuales ayudan a evitar conflictos y garantizan la consistencia en el desarrollo.

## Tipos de Entornos Virtuales en Python

Python ofrece dos tipos principales de entornos virtuales:

- **Entornos virtuales basados en `venv`**: `venv` es un módulo incorporado en Python que permite crear entornos virtuales sin necesidad de instalar herramientas adicionales. Es ideal para proyectos más simples y específicos que solo requieren bibliotecas de Python.
- **Entornos virtuales basados en conda**: Conda es una herramienta de gestión de paquetes que puede manejar no solo paquetes de Python, sino también bibliotecas de otros lenguajes y dependencias del sistema. Es especialmente útil en proyectos científicos y de análisis de datos.

## Cuándo Usar Entornos Virtuales

Aquí hay una lista de situaciones en las que es recomendable utilizar entornos virtuales:

- **Proyectos Independientes**: Cuando estás trabajando en varios proyectos que requieren versiones diferentes de bibliotecas, los entornos virtuales garantizan que cada proyecto esté aislado y tenga sus propias dependencias.
- **Colaboración**: Si estás colaborando en un proyecto con otros desarrolladores, el uso de entornos virtuales asegura que todos estén trabajando en el mismo entorno configurado de manera consistente.
- **Pruebas de Bibliotecas**: Antes de integrar una nueva biblioteca en tu proyecto principal, puedes crear un entorno virtual para probarla y asegurarte de que no cause conflictos con otras bibliotecas existentes.
- **Entornos de Desarrollo y Producción**: Mantén entornos separados para el desarrollo y la producción. Esto ayuda a prevenir problemas causados por diferencias en las dependencias entre los dos entornos.

## Sección 4: Gestión de Entornos Virtuales en Python

### Crear un Entorno Virtual

Para crear un entorno virtual basado en `venv`:

```bash
python -m venv nombre_del_entorno

```

Para crear un entorno virtual basado en conda:

```bash
conda create -n nombre_del_entorno

```

### Activar y Desactivar un Entorno Virtual

En sistemas Unix:

- Activar: `source nombre_del_entorno/bin/activate`
- Desactivar: `deactivate`

En Windows:

- Activar: `nombre_del_entorno\\Scripts\\activate`
- Desactivar: `deactivate`

### Instalar Dependencias

Dentro de un entorno virtual, puedes instalar dependencias usando `pip` o `conda`, según el entorno virtual que estés utilizando:

```bash
pip install nombre_de_paquete

```

### Exportar Dependencias

Para exportar las dependencias instaladas en un entorno virtual basado en conda:

```bash
conda list --export > requirements.txt

```

### Eliminar un Entorno Virtual

Simplemente elimina la carpeta del entorno virtual. Asegúrate de que el entorno esté desactivado antes de hacerlo.
