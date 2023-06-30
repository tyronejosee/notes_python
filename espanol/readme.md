# Introducción

## ¿Qué es Python?

Python es un lenguaje de programación popular. Fue creado por Guido van Rossum y lanzado en 1991.

Se utiliza para:

- Desarrollo web (lado del servidor),
- Desarrollo de software,
- Matemáticas,
- Scripting de sistemas.

## ¿Qué puede hacer Python?

- Python se puede utilizar en un servidor para crear aplicaciones web.
- Python se puede utilizar junto con software para crear flujos de trabajo.
- Python puede conectarse a sistemas de bases de datos. También puede leer y modificar archivos.
- Python se puede utilizar para manejar grandes volúmenes de datos y realizar matemáticas complejas.
- Python se puede utilizar para prototipos rápidos o para el desarrollo de software listo para producción.

## ¿Por qué Python?

- Python funciona en diferentes plataformas (Windows, Mac, Linux, Raspberry Pi, etc.).
- Python tiene una sintaxis sencilla similar al lenguaje inglés.
- Python tiene una sintaxis que permite a los desarrolladores escribir programas con menos líneas que otros lenguajes de programación.
- Python se ejecuta en un sistema de intérprete, lo que significa que el código se puede ejecutar tan pronto como se escribe. Esto significa que el prototipado puede ser muy rápido.
- Python se puede tratar de manera procedural, orientada a objetos o funcional.

## Bueno saberlo

- La versión principal más reciente de Python es Python 3, que utilizaremos en este tutorial. Sin embargo, Python 2, aunque no se actualiza con nada más que actualizaciones de seguridad, sigue siendo bastante popular.
- En este tutorial, Python se escribirá en un editor de texto. Es posible escribir Python en un Entorno de Desarrollo Integrado, como Thonny, Pycharm, Netbeans o Eclipse, que son especialmente útiles para administrar colecciones más grandes de archivos de Python.

## Sintaxis de Python en comparación con otros lenguajes de programación

- Python fue diseñado para ser legible y tiene algunas similitudes con el lenguaje inglés con influencia de las matemáticas.
- Python utiliza saltos de línea para completar un comando, a diferencia de otros lenguajes de programación que a menudo utilizan punto y coma o paréntesis.
- Python se basa en la indentación, utilizando espacios en blanco, para definir el alcance, como el alcance de bucles, funciones y clases. Otros lenguajes de programación a menudo utilizan llaves de llave para este propósito.

## Python Install

Many PCs and Macs will have python already installed.

To check if you have python installed on a Windows PC, search in the start bar for Python or run the following on the Command Line (cmd.exe):

```bash
C:\Users\*Your Name*>python --version
```

To check if you have python installed on a Linux or Mac, then on linux open the command line or on Mac open the Terminal and type:

```bash
python --version
```

If you find that you do not have Python installed on your computer, then you can download it for free from the following website: [https://www.python.org/](https://www.python.org/)

## Python Quickstart

Python is an interpreted programming language, this means that as a developer you write Python (.py) files in a text editor and then put those files into the python interpreter to be executed.

The way to run a python file is like this on the command line:

```bash
C:\Users\*Your Name*>python helloworld.py
```

Where "helloworld.py" is the name of your python file.

Let's write our first Python file, called helloworld.py, which can be done in any text editor.

helloworld.py

```python
print("Hello, World!")
```

Simple as that. Save your file. Open your command line, navigate to the directory where you saved your file, and run:

C:\Users\*Your Name*>python helloworld.py

The output should read:

```bash
Hello, World!
```

Congratulations, you have written and executed your first Python program.

## The Python Command Line

To test a short amount of code in python sometimes it is quickest and easiest not to write the code in a file. This is made possible because Python can be run as a command line itself.

Type the following on the Windows, Mac or Linux command line:

```bash
C:\Users\*Your Name*>python
```

Or, if the "python" command did not work, you can try "py":

```bash
C:\Users\*Your Name*>py
```

From there you can write any python, including our hello world example from earlier in the tutorial:

```bash
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
```

Which will write "Hello, World!" in the command line:

```bash
C:\Users\Your Name>python
Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> print("Hello, World!")
Hello, World!
```

Whenever you are done in the python command line, you can simply type the following to quit the python command line interface:

```bash
exit()
```