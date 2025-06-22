Пример демонстрации для i18n-markdown-translator
================================================

<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center"><img src="https://greenmeeple.github.io/img/logo.png"/></a></p>
<p align="center"> Это тестовый случай. </чел>  
<p align="center"><a href="https://greenmeeple.github.io" align="center">Нажмите здесь, чтобы проверить мой сайт</a></p>
<p align="center"><a href="https://buymeacoffee.com/greenmeeple" align="center">Поддержи меня</a></p>

Реклама от вашего дружелюбного программиста-одиночки
----------------------------------------------------

<таблица align="center"><tr><td valign="top" width="33%">

### Проекты и репозитории

* [МенсаарЛекер](https://github.com/GreenMeeple/MensaarLecker) Полностью автоматизированный парсер и статический веб-сайт для Saarbrücken Mensa, работающий на Python, Selenium, Google Sheets и GitHub Actions.
* [udsfahrplan](https://github.com/GreenMeeple/uds-fahrplan) Легкий Telegram-бот, предназначенный для студентов Саарского университета
* [hafas-bitmask-калькулятор](https://github.com/GreenMeeple/hafas-bitmask-calculator) Простой веб-инструмент, помогающий декодировать и кодировать растровые маски, используемые HAFAS API.
* [гексо-жруби](https://github.com/GreenMeeple/hexo-zhruby) Плагин Hexo Tag, разработанный с использованием Node.js
* [Azul\_Test](https://github.com/xindoo/eng-practices-cn) Программа на языке C++, основанная на настольной игре Azul Майкла Кислинга.
* [Больше проектов](https://github.com/GreenMeeple?tab=repositories)

</тд>
<td valign="top" width="33%">

### Личный блог

* [Опыт разработки python-telegram-бота и заметки](https://greenmeeple.github.io/python/tgbot/)
* [UdS Fahrplan Bot](https://greenmeeple.github.io/projects/udsfahrplan-bot/)
* [🍽 🥨 MensaarLecker -- Любимый инструмент для поиска любимого меню Mensa Ladies с помощью Selenium🥨 🍽](https://greenmeeple.github.io/projects/mensaar/)
* [Журнал разработки MensaarLecker (3) -- Развертывание и интеграция Telegram-бота](https://greenmeeple.github.io/projects/mensaar-log3/)
* [UdS Fahrplan Bot Development Log (5) -- Пояснения к сессиям и запросам бота](https://greenmeeple.github.io/projects/udsfahrplan-log5/)
* [Больше постов](https://greenmeeple.github.io/)

</тд>
</тр></стол>

---

Тестовый кейс из [демо markdown-it](https://markdown-it.github.io/)
===================================================================

h1 Заголовок
============

h2 Заголовок
------------

### h3 Заголовок

#### h4 Заголовок

##### h5 Заголовок

###### h6 Заголовок

Горизонтальные линейки
----------------------

---



---



---

Ударение
--------

**Это жирный текст**

**Это жирный текст**

*Это курсивный текст*

*Это курсивный текст*

~~Зачеркнутый~~

Цитаты
------

> Цитаты также могут быть вложенными...
>
> > ... с помощью дополнительных знаков «больше», расположенных рядом друг с другом...
> >
> > > ... или с пробелами между стрелками.

Списках
-------

Неупорядоченный

* Создайте список, начав строку с `+`, `-`или `*`
* Подсписки делаются путем отступа из 2 пробелов:
  + Изменение символа маркера приводит к началу нового списка:
    - Розы красные
    - Фиалки синие
    - Даже вы меняете символ
* Это по-прежнему легко сделать!

Упорядоченный

1. Lorem ipsum dolor sit amet
2. Consectetur adipiscing elit
3. Integer molestie lorem at massa
4. Вы можете использовать последовательные числа...
5. ... или оставить все номера как `1.`

Начинайте нумерацию со смещением:

57. Фу
58. бар

Код
---

Встроенный `code`

Код с отступом

```
// Some comments
line 1 of code
line 2 of code
line 3 of code

```

Блочный код "заборы"

```
Sample text here...
```

Подсветка синтаксиса

```js
var foo = function (bar) {
  return bar++;
};

console.log(foo(5));
```

Таблицы
-------

| Описание опции |  |
| --- | --- |
| данные | путь к файлам данных для предоставления данных, которые будут переданы в шаблоны. |
| двигатель | движок, который будет использоваться для обработки шаблонов. Руль используется по умолчанию. |
| ext | Расширение для использования в файлах DEST. |

Столбцы с выравниванием по правому краю

| Описание опции |  |
| --- | --- |
| данные | путь к файлам данных для предоставления данных, которые будут переданы в шаблоны. |
| двигатель | движок, который будет использоваться для обработки шаблонов. Руль используется по умолчанию. |
| ext | Расширение для использования в файлах DEST. |

Дюны
----

[Текст ссылки](http://dev.nodeca.com)

Автоматически преобразованные <https://github.com/nodeca/pica> ссылок (включите linkify для просмотра)

Изображения
-----------

![GreenMeeple](https://greenmeeple.github.io/img/avatar.png)
![Logo](https://greenmeeple.github.io/img/logo.png "The GreenMeeple Logo")

### [Сноски](https://github.com/markdown-it/markdown-it-footnote)

Ссылка на сноску 1[[1]](#fn1).

Ссылка на сноску 2[[2]](#fn2).

Определение встроенной сноски[[3]](#fn3) .

Дублирующаяся ссылка на сноску[[2:1]](#fn2).

---

1. Сноска **может иметь разметку**

   и несколько абзацев. [↩︎](#fnref1)
2. Текст сноски. [↩](#fnref2)[↩︎ ︎](#fnref2:1)
3. Текст встроенной сноски [↩︎](#fnref3)