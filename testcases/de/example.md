Beispieldemo für i18n-markdown-translator
=========================================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> Dies ist ein Testfall. </S>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">Klicken Sie hier, um meine Website zu überprüfen</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">Support me</a></p>

Werbung von Ihrem freundlichen Solo-Programmierer
-------------------------------------------------

<table align="mitte"><tr><td valign="oben" width="33%">

### Projekte und Repos

* [MensaarLecker](https://github.com/GreenMeeple/MensaarLecker) Ein vollautomatischer Scraper und eine statische Website für die Mensa Saarbrücken, powered by Python, Selenium, Google Sheets und GitHub Actions.
* [udsfahrplan](https://github.com/GreenMeeple/uds-fahrplan) Ein leichter Telegram-Bot, der für Studenten der Universität des Saarlandes entwickelt wurde
* [hafas-bitmask-rechner](https://github.com/GreenMeeple/hafas-bitmask-calculator) Ein einfaches webbasiertes Tool, mit dem Sie Bitmasken dekodieren und codieren können, die von der HAFAS-API verwendet werden.
* [Hexo-Zhruby](https://github.com/GreenMeeple/hexo-zhruby) Ein Hexo Tag-Plugin, das mit Node.js entwickelt wurde
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) Ein C++-Programm, das auf dem Brettspiel Azul von Michael Kiesling basiert.
* [Weitere Projekte](https://github.com/GreenMeeple?tab=repositories)

</td>
<td valign="oben" width="33%">

### Persönlicher Blog

* [python-telegram-bot entwicklung erfahrungen und hinweise](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan Bot](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- Ein beliebtes Tool, um das Lieblingsmenü der Mensa-Damen mit Selen🥨 🍽 herauszufinden](https://greenmeeple.github.io/projects/mensaar/)
* [MensaarLecker Entwicklungsprotokoll (3) -- Bereitstellung und Integration von Telegram-Bots](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot Development Log (5) -- Erläuterungen zu Bot-Sitzungen und -Anfragen](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [Weitere Beiträge](https://greenmeeple.github.io/)

</td>
</tr></Tabelle>

---

Testfall aus [der markdown-it Demo](https://markdown-it.github.io/)
===================================================================

h1 Kurs
=======

h2 Kurs
-------

### h3 Kurs

#### h4 Kurs

##### h5 Kurs

###### h6 Kurs

Horizontale Regeln
------------------

---



---



---

Betonung
--------

**Dies ist fettgedruckter Text**

**Dies ist fettgedruckter Text**

*Dies ist kursiver Text*

*Dies ist kursiver Text*

~~Durchgestrichen~~

Blockzitate
-----------

> Blockquotes können auch verschachtelt werden...
>
> > ... durch die Verwendung zusätzlicher Größer-als-Zeichen direkt nebeneinander...
> >
> > > ... oder mit Leerzeichen zwischen den Pfeilen.

Listet
------

Nicht eingeordnet

* Erstellen Sie eine Liste, indem Sie eine Zeile mit `+`, `-`oder beginnen `*`
* Unterlisten werden erstellt, indem 2 Leerzeichen eingerückt werden:
  + Änderung des Markierungszeichens erzwingt neuen Listenstart:
    - Rosen sind rot
    - Veilchen sind blau
    - Auch wenn Sie das Symbol ändern
* Es ist immer noch ganz einfach!

Angeordnet

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Sie können fortlaufende Nummern verwenden...
5. ... oder behalten Sie alle Zahlen als `1.`

Nummerierung mit Versatz beginnen:

57. Foo
58. Stab

Code
----

Schritthaltend `code`

Eingerückter Code

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

Blockcode "Zäune"

```
Sample text here...
```

Syntaxhervorhebung

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

Tabellen
--------

| Option | Beschreibung |
| --- | --- |
| Daten | Pfad zu Datendateien, um die Daten bereitzustellen, die an Vorlagen übergeben werden. |
| Motor | -Engine, die für die Verarbeitung von Vorlagen verwendet werden soll. Lenker ist die Standardeinstellung. |
| Extern | Dateiendung, die für DEST-Dateien verwendet werden soll. |

Rechtsbündig ausgerichtete Spalten

| Option | Beschreibung |
| --- | --- |
| Daten | Pfad zu Datendateien, um die Daten bereitzustellen, die an Vorlagen übergeben werden. |
| Motor | -Engine, die für die Verarbeitung von Vorlagen verwendet werden soll. Lenker ist die Standardeinstellung. |
| Extern | Dateiendung, die für DEST-Dateien verwendet werden soll. |

Verknüpfungen
-------------

[Link-Text](http://dev.nodeca.com)

Automatisch konvertierte [Link-https://github.com/nodeca/pica](https://github.com/nodeca/pica) (linkify aktivieren, um zu sehen)

Bilder
------

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [Fußnoten](https://github.com/markdown-it/markdown-it-footnote)

Fußnote 1 Link[[1]](#fn1).

Fußnote 2 Link[[2]](#fn2).

Definition der Inline-Fußnote[[3].](#fn3)

Duplizierte Fußnotenreferenz [[2:1]](#fn2).

---

1. Fußnote **kann Markup haben**

   und mehrere Absätze. [↩︎](#fnref1)
2. Text der Fußnote. [↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. Text der eingebetteten Fußnote [↩︎](#fnref3)