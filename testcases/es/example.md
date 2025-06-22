Ejemplo de demostración para i18n-markdown-translator
=====================================================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> Este es un caso de prueba. </p>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">Haga clic aquí para ver mi sitio web</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">Apoyándame</a></p>

Anuncio de tu amigable programador en solitario
-----------------------------------------------

<table align="center"><tr><td valign="top" width="33%">

### Proyectos y Repos

* [MensaarLecker](https://github.com/GreenMeeple/MensaarLecker) Un scraper totalmente automatizado y un sitio web estático para Saarbrücken Mensa, impulsado por Python, Selenium, Google Sheets y GitHub Actions.
* [UDSFAHRPLAN](https://github.com/GreenMeeple/uds-fahrplan) Un bot ligero de Telegram diseñado para estudiantes de la Universidad de Saarland
* [hafas-bitmask-calculator](https://github.com/GreenMeeple/hafas-bitmask-calculator) Una sencilla herramienta basada en la web que le ayuda a decodificar y codificar las máscaras de bits utilizadas por la API de HAFAS.
* [hexo-zhruby](https://github.com/GreenMeeple/hexo-zhruby) Un plugin de Hexo Tag desarrollado con Node.js
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) Un programa en C++ basado en el juego de mesa Azul de Michael Kiesling.
* [Más proyectos](https://github.com/GreenMeeple?tab=repositories)

</TD>
<td valign="top" width="33%">

### Personal Blog

* [Experiencia y notas de desarrollo de python-telegram-bot](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan Bot](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- Una herramienta muy querida para descubrir el menú favorito de las damas de Mensa usando selenio🥨 🍽](https://greenmeeple.github.io/projects/mensaar/)
* [Registro de desarrollo de MensaarLecker (3) -- Implementación e integración de bots de Telegram](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot Development Log (5) -- Explicaciones sobre las sesiones y solicitudes de bots](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [Más publicaciones](https://greenmeeple.github.io/)

</TD>
</tr></mesa>

---

Caso de prueba de [la demostración de markdown-it](https://markdown-it.github.io/)
==================================================================================

H1 Encabezamiento
=================

Encabezamiento h2
-----------------

### Encabezamiento h3

#### Encabezamiento h4

##### h5 Encabezamiento

###### Encabezamiento h6

Reglas horizontales
-------------------

---



---



---

Énfasis
-------

**Este es un texto en negrita**

**Este es un texto en negrita**

*Este es texto en cursiva*

*Este es texto en cursiva*

~~Tachado~~

Citas en bloque
---------------

> Las citas en bloque también se pueden anidar...
>
> > ... mediante el uso de signos adicionales de mayor que uno al lado del otro...
> >
> > > ... o con espacios entre flechas.

Listas
------

Desordenada

* Cree una lista comenzando una línea con `+`, `-`, o `*`
* Las sublistas se forman sangrando 2 espacios:
  + El cambio de carácter del marcador fuerza el inicio de una nueva lista:
    - Las rosas son rojas
    - Las violetas son azules
    - Incluso tú cambias el símbolo
* ¡Sigue siendo fácil de hacer!

Ordenado

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Puedes usar números secuenciales...
5. ... o mantenga todos los números como `1.`

Iniciar la numeración con desplazamiento:

57. Foo
58. barra

Código
------

Inline `code`

Código con sangría

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

Código de bloque "vallas"

```
Sample text here...
```

Resaltado de sintaxis

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

Mesas
-----

| Descripción de la | opción |
| --- | --- |
| datos | Ruta de acceso a los archivos de datos para proporcionar los datos que se pasarán a las plantillas. |
| motor | motor que se utilizará para el procesamiento de plantillas. El manillar es el valor predeterminado. |
| Ext | Extensión que se utilizará para los archivos dest. |

Columnas alineadas a la derecha

| Descripción de la | opción |
| --- | --- |
| datos | Ruta de acceso a los archivos de datos para proporcionar los datos que se pasarán a las plantillas. |
| motor | motor que se utilizará para el procesamiento de plantillas. El manillar es el valor predeterminado. |
| Ext | Extensión que se utilizará para los archivos dest. |

Enlaces
-------

[Texto del enlace](http://dev.nodeca.com)

<https://github.com/nodeca/pica> de enlace autoconvertido (habilitar linkify para ver)

Imágenes
--------

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [Notas](https://github.com/markdown-it/markdown-it-footnote)

Enlace a la nota a pie de página 1[[1].](#fn1)

Enlace a la nota 2[[2]](#fn2).

Nota a pie de página en línea[[3]](#fn3) definición.

Referencia duplicada de la nota al pie [[2:1]](#fn2).

---

1. La nota al pie **puede tener marcado**

   y varios párrafos. [↩︎](#fnref1)
2. Texto de la nota a pie de página. [↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. Texto de la nota a pie de página [↩en línea ︎](#fnref3)