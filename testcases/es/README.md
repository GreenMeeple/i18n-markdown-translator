i18n-md-traductor
=================

Una herramienta de línea de comandos para traducir archivos Markdown mediante la API de Microsoft Translator. Conserva la estructura de Markdown, incluidas tablas, bloques de código, listas y notas al pie.

🛠 Instalación
-------------

```bash
pip install i18n-md-translator
```

🚀 Uso
-----

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` o `--source`: Idioma de origen (predeterminado: `en`)
* `-t` o `--target`: Idioma de destino (predeterminado: `yue`)

🧪 Ejemplo
---------

```bash
i18n-md-translate ./README.md -s en -t yue
```

Crea: `./yue/README.md`

🌐 Idiomas admitidos
-------------------

Consulte: [Compatibilidad con idiomas - Traductor - Servicios de Azure AI](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 Clave de API
--------------

Coloque sus credenciales de Translator API en un `.env` archivo:

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 Licencia
----------

MIT

Referencias
-----------

Analizador de Markdown, bien hecho. 100% soporte CommonMark, extensiones, plugins de sintaxis y alta velocidad.

* [rebajas-it](https://github.com/markdown-it/markdown-it)
* [rebaja-it-py](https://github.com/executablebooks/markdown-it-py)

Convertir HTML a Markdown, el editor de markdown más simple con carga de imágenes en la nube incorporada.

* [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
* [Markdownify](https://github.com/tibastral/markdownify)

---