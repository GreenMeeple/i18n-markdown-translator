# i18n-markdown-translator

A command-line tool to translate Markdown files using the Microsoft Translator API. It preserves Markdown structure, including tables, code blocks, lists, and footnotes.

## 🛠 Installation

```bash
pip install i18n-md-translator
```

## 🚀 Usage

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

- `-s` or ``--source``: Source language (default: `en`)

- `-t` or `--target`: Target language (default: `yue`)

## 🧪 Example

```bash
i18n-md-translate ./README.md -s en -t yue
```

Creates: `./yue/README.md`

## 🌐 Supported Languages

See: [Language support - Translator - Azure AI services](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

## 🔐 API Key

Put your Translator API credentials in a `.env` file:

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

## 📄 License

MIT

## References

Markdown parser, done right. 100% CommonMark support, extensions, syntax plugins & high speed.

- [markdown-it](https://github.com/markdown-it/markdown-it)
- [markdown-it-py](https://github.com/executablebooks/markdown-it-py)

Convert HTML to Markdown, The simplest markdown editor with built in cloudinary image upload.

- [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
- [markdownify](https://github.com/tibastral/markdownify)

---
