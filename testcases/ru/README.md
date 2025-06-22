i18n-md-транслятор
==================

Средство командной строки для перевода файлов Markdown с помощью API Microsoft Translator. Он сохраняет структуру Markdown, включая таблицы, блоки кода, списки и сноски.

🛠 Установка
-----------

```bash
pip install i18n-md-translator
```

🚀 Употребление
--------------

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` или `--source`: Исходный язык (по умолчанию: `en`)
* `-t` или `--target`: Целевой язык (по умолчанию: `yue`)

🧪 Пример
--------

```bash
i18n-md-translate ./README.md -s en -t yue
```

Создает: `./yue/README.md`

🌐 Поддерживаемые языки
----------------------

См.: [Языковая поддержка - Переводчик - Службы Azure AI](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 Ключ API
----------

Поместите свои учетные данные Translator API в файл:`.env`

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 Лицензия
----------

Массачусетский технологический институт

Ссылки
------

Парсер Markdown, сделан правильно. 100% поддержка CommonMark, расширения, синтаксические плагины и высокая скорость.

* [Markdown-it](https://github.com/markdown-it/markdown-it)
* [Уценка it-py](https://github.com/executablebooks/markdown-it-py)

Конвертация HTML в Markdown, самый простой редактор Markdown со встроенной облачной загрузкой изображений.

* [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
* [Маркдаунифицировать](https://github.com/tibastral/markdownify)

---