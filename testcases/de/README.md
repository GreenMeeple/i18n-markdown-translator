i18n-md-translator
==================

Ein Befehlszeilentool zum Übersetzen von Markdown-Dateien mithilfe der Microsoft Translator-API. Die Markdown-Struktur, einschließlich Tabellen, Codeblöcke, Listen und Fußnoten, wird beibehalten.

🛠 Installation
--------------

```bash
pip install i18n-md-translator
```

🚀 Verwendung
------------

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` oder `--source`: Ausgangssprache (Standard: `en`)
* `-t` oder `--target`: Zielsprache (Standard: `yue`)

🧪 Beispiel
----------

```bash
i18n-md-translate ./README.md -s en -t yue
```

Erschafft: `./yue/README.md`

🌐 Unterstützte Sprachen
-----------------------

Siehe: [Sprachunterstützung – Übersetzer – Azure AI Services](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 API-Schlüssel
---------------

Fügen Sie Ihre Anmeldeinformationen für die Translator-API in eine `.env` Datei ein:

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 Lizenz
--------

Am MIT (MIT)

Referenzen
----------

Markdown-Parser, richtig gemacht. 100% CommonMark-Unterstützung, Erweiterungen, Syntax-Plugins und hohe Geschwindigkeit.

* [markdown-it](https://github.com/markdown-it/markdown-it)
* [markdown-it-py](https://github.com/executablebooks/markdown-it-py)

Konvertieren Sie HTML in Markdown, den einfachsten Markdown-Editor mit integriertem Cloudinary-Bildupload.

* [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
* [MarkDownify](https://github.com/tibastral/markdownify)

---