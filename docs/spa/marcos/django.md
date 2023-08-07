# Django

Autor(es): Adrian Holovaty, Simon Willison

Desarrollador(es): Django Software Foundation

Lanzamiento Inicial: Julio, 21, 2005

Escrito en: Python

Tamaño: 8.9 MB

Tipo: Framework Web

Licencia: 3-clause BSD

www.djangoproject.com

github.com/django/django

**Django** (pronunciado [JANG-goh]; a veces estilizado como **django**) es un [marco de trabajo web](https://es.wikipedia.org/wiki/Marco_de_trabajo_web) [libre y de código abierto](https://es.wikipedia.org/wiki/Software_libre_y_de_c%C3%B3digo_abierto) basado en [Python](https://es.wikipedia.org/wiki/Python) que sigue el patrón arquitectónico de modelo-vista-controlador (MVC). Es mantenido por la [Fundación de Software Django](https://es.wikipedia.org/wiki/Fundaci%C3%B3n_de_Software_Django) (DSF), una organización independiente establecida en Estados Unidos como una entidad sin fines de lucro 501(c)(3).

El objetivo principal de Django es facilitar la creación de sitios web complejos impulsados por bases de datos. El marco de trabajo enfatiza la "reutilización" y la "conectabilidad" de componentes, menos código, baja interconexión, desarrollo rápido y el principio de "no repitas lo mismo". Python se utiliza en todo el proceso, incluso para la configuración, los archivos y los modelos de datos. Django también proporciona una interfaz administrativa opcional de "crear, leer, actualizar y eliminar" que se genera dinámicamente a través de la introspección y se configura mediante modelos de administración.

Algunos sitios conocidos que utilizan Django son Instagram, Mozilla, Disqus, Bitbucket, Nextdoor y Clubhouse.

## Historia

Django fue creado en otoño de 2003, cuando los programadores web del periódico *Lawrence Journal-World*, Adrian Holovaty y Simon Willison, comenzaron a utilizar Python para construir aplicaciones. Jacob Kaplan-Moss fue contratado temprano en el desarrollo de Django poco antes de que terminara la pasantía de Simon Willison. Se lanzó públicamente bajo una licencia BSD en julio de 2005. El marco de trabajo fue nombrado en honor al guitarrista Django Reinhardt. Adrian Holovaty es un guitarrista de jazz romaní y un gran admirador de Django Reinhardt.

En junio de 2008, se anunció que la recién formada Fundación de Software Django (DSF) mantendría Django en el futuro.

## Características

A pesar de tener su propia nomenclatura, como llamar a los objetos invocables que generan las respuestas HTTP "vistas", el marco central de Django se puede ver como una arquitectura de modelo-vista-controlador (MVC). Consiste en un mapeador objeto-relacional (ORM) que actúa como mediador entre los modelos de datos (definidos como clases de Python) y una base de datos relacional (modelo), un sistema para procesar solicitudes HTTP con un sistema de plantillas web (vista) y un despachador de URL basado en expresiones regulares (controlador).

También incluidas en el marco central se encuentran:

- Un servidor web ligero e independiente para desarrollo y pruebas.
- Un sistema de serialización y validación de formularios que puede traducir entre formularios HTML y valores adecuados para almacenamiento en la base de datos.
- Un sistema de plantillas que utiliza el concepto de herencia tomado de la programación orientada a objetos.
- Un marco de trabajo de almacenamiento en caché que puede utilizar varios métodos de caché.
- Soporte para clases de middleware que pueden intervenir en diversas etapas del procesamiento de solicitudes y llevar a cabo funciones personalizadas.
- Un sistema interno de despacho que permite a los componentes de una aplicación comunicar eventos entre sí a través de señales predefinidas.
- Un sistema de internacionalización, que incluye traducciones de los propios componentes de Django a varios idiomas.
- Un sistema de serialización que puede producir y leer representaciones en XML y/o JSON de instancias de modelos de Django.
- Un sistema para ampliar las capacidades del motor de plantillas.
- Una interfaz para el marco de pruebas unitarias integrado de Python.

### **Aplicaciones incluidas[[editar](https://es.wikipedia.org/w/index.php?title=Django_(framework_web)&action=edit&section=4)]**

La distribución principal de Django también incluye un número de aplicaciones en su paquete "contrib", que incluyen:

- Un sistema de autenticación extensible.
- La interfaz administrativa dinámica.
- Herramientas para generar fuentes de sindicación [RSS](https://es.wikipedia.org/wiki/RSS_(formato)) y [Atom](https://es.wikipedia.org/wiki/Atom_(est%C3%A1ndar)).
- Un marco de trabajo "Sitios" que permite que una instalación de Django ejecute múltiples sitios web, cada uno con su propio contenido y aplicaciones.
- Herramientas para generar [Google Sitemaps](https://es.wikipedia.org/wiki/Google_Sitemaps).
- Mitigación incorporada para ataques típicos de la web, como falsificación de solicitud entre sitios (CSRF), scripting entre sitios (XSS), inyección SQL, cracking de contraseñas y otros. La mayoría de estas defensas están activadas de forma predeterminada.
- Un marco para crear aplicaciones [SIG](https://es.wikipedia.org/wiki/Sistema_de_Informaci%C3%B3n_Geogr%C3%A1fica).

### **Extensibilidad**

El sistema de configuración de Django permite que código de terceros se integre en un proyecto regular, siempre y cuando siga las convenciones de la aplicación reutilizable. Hay más de 5000 paquetes disponibles para extender el comportamiento original del marco de trabajo, proporcionando soluciones para problemas que la herramienta original no abordó: registro, búsqueda, provisión y consumo de API, sistemas de gestión de contenido (CMS), etc.

Sin embargo, esta extensibilidad está mitigada por las dependencias de los componentes internos. Aunque la filosofía de Django implica un acoplamiento flojo, los filtros y etiquetas de plantilla asumen una implementación de motor, y tanto la autenticación como las aplicaciones empaquetadas de administración requieren el uso del ORM interno. Ninguno de estos filtros o aplicaciones empaquetadas es obligatorio para ejecutar un proyecto de Django, pero las aplicaciones reutilizables tienden a depender de ellos, alentando a los desarrolladores a seguir utilizando el conjunto oficial para beneficiarse plenamente del ecosistema de aplicaciones.

### **Disposiciones del servidor[[editar](https://es.wikipedia.org/w/index.php?title=Django_(framework_web)&action=edit&section=6)]**

Django se puede ejecutar en conjunto con [Apache](https://es.wikipedia.org/wiki/Servidor_HTTP_Apache), [Nginx](https://es.wikipedia.org/wiki/Nginx) utilizando [WSGI](https://es.wikipedia.org/wiki/Interfaz_de_pasarela_del_servidor_web), [Gunicorn](https://es.wikipedia.org/wiki/Gunicorn) o [Cherokee](https://es.wikipedia.org/wiki/Cherokee_(servidor_web)) utilizando flup (un módulo de Python). Django también incluye la capacidad de iniciar un servidor [FastCGI](https://es.wikipedia.org/wiki/FastCGI), lo que permite su uso detrás de cualquier servidor web que admita FastCGI, como [Lighttpd](https://es.wikipedia.org/wiki/Lighttpd) o [Hiawatha](https://es.wikipedia.org/wiki/Hiawatha_(servidor_web)). También es posible utilizar otros servidores web compatibles con [WSGI](https://es.wikipedia.org/wiki/Interfaz_de_pasarela_del_servidor_web). Django admite oficialmente cinco bases de datos: [PostgreSQL](https://es.wikipedia.org/wiki/PostgreSQL), [MySQL](https://es.wikipedia.org/wiki/MySQL), [MariaDB](https://es.wikipedia.org/wiki/MariaDB), [SQLite](https://es.wikipedia.org/wiki/SQLite) y [Oracle](https://es.wikipedia.org/wiki/Oracle_Database). [Microsoft SQL Server](https://es.wikipedia.org/wiki/Microsoft_SQL_Server) se puede utilizar con django-mssql, mientras que existen bases de datos externas similares para [IBM Db2](https://es.wikipedia.org/wiki/IBM_Db2), [SQL Anywhere](https://es.wikipedia.org/wiki/SQL_Anywhere) y [Firebird](https://es.wikipedia.org/wiki/Firebird_(base_de_datos)). Existe un fork llamado django-nonrel, que admite bases de datos NoSQL, como [MongoDB](https://es.wikipedia.org/wiki/MongoDB) y Datastore de [Google App Engine](https://es.wikipedia.org/wiki/Google_App_Engine).

Django también se puede ejecutar junto con [Jython](https://es.wikipedia.org/wiki/Jython) en cualquier servidor de aplicaciones [Java EE](https://es.wikipedia.org/wiki/Java_EE), como [GlassFish](https://es.wikipedia.org/wiki/GlassFish) o [JBoss](https://es.wikipedia.org/wiki/JBoss). En este caso, debe instalarse django-jython para proporcionar controladores [JDBC](https://es.wikipedia.org/wiki/JDBC) para la conectividad con bases de datos, que también puede brindar funcionalidad para compilar Django en un archivo .war adecuado para implementación.

## DjangoCon

Existe una conferencia semianual para desarrolladores y usuarios de Django, llamada "DjangoCon", que se ha celebrado desde septiembre de 2008. DjangoCon se lleva a cabo anualmente en Europa, en mayo o junio; mientras que otra se realiza en Estados Unidos en agosto o septiembre, en varias ciudades. DjangoCon 2012 tuvo lugar en Washington, D.C., del 3 al 8 de septiembre. DjangoCon 2013 se llevó a cabo en Chicago en el Hyatt Regency Hotel y las sesiones de trabajo posteriores (Sprints) se organizaron en Digital Bootcamp, un centro de capacitación en informática. DjangoCon US 2014 regresó a Portland, Oregón, del 30 de agosto al 6 de septiembre. DjangoCon US 2015 se celebró en Austin, Texas, del 6 al 11 de septiembre en el AT&T Executive Center. DjangoCon US 2016 se realizó en Filadelfia, Pensilvania, en The Wharton School de la Universidad de Pensilvania, del 17 al 22 de julio. DjangoCon US 2017 se llevó a cabo en Spokane, Washington; en 2018, DjangoCon US tuvo lugar en San Diego, California. DjangoCon US 2019 se realizó nuevamente en San Diego, California, del 22 al 27 de septiembre. DjangoCon 2021 se llevó a cabo de manera virtual y en 2022, DjangoCon US regresó a San Diego del 16 al 21 de octubre.

Por lo general, las mini-conferencias de Django se celebran cada año como parte de la conferencia australiana de Python, 'PyCon AU'. Estas mini-conferencias se han realizado previamente en:

- Hobart, Australia, en julio de 2013.
- Brisbane, Australia, en agosto de 2014 y 2015.
- Melbourne, Australia, en agosto de 2016 y 2017.
- Sídney, Australia, en agosto de 2018 y 2019.

Django ha generado grupos de usuarios y reuniones en todo el mundo, siendo el grupo más notable la organización Django Girls, que comenzó en Polonia pero que ahora ha tenido eventos en 91 países.

## Adaptaciones a otros lenguajes

Los programadores han adaptado el diseño del motor de plantillas de Django de Python a otros lenguajes, proporcionando un buen soporte multiplataforma. Algunas de estas opciones son adaptaciones directas, mientras que otras, aunque están inspiradas en Django y mantienen sus conceptos, toman la libertad de apartarse del diseño original de Django:

- Liquid para Ruby.
- Template::Swig para Perl.
- Twig para PHP y JavaScript.
- Jinja para Python.
- ErlyDTL para Erlang.

## CMS Basados en Django

Django como framework es capaz de construir un sistema de gestión de contenidos (CMS) completo. Sin embargo, existen proyectos de CMS dedicados que se construyen sobre y extienden el framework Django. A continuación, se presenta una lista de algunos de los CMS basados en Django más populares:

- Django CMS.
- Wagtail.
- Mezzanine.
