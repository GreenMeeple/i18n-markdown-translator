i18n-md-翻譯器
===========

一個命令行工具，用于使用Microsoft Translator API翻譯Markdown文件。 它保留咗Markdown結構，包括表格、代碼塊、清單同腳註。

🛠 安裝.
-----

```bash
pip install i18n-md-translator
```

🚀 用法
----

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` 或 `--source`：源語言(默認值： `en`)
* `-t` 或 `--target`：目標語言(默認： `yue`)

🧪 例
---

```bash
i18n-md-translate ./README.md -s en -t yue
```

創建： `./yue/README.md`

🌐 支持嘅語言
-------

請參閱： [語言支持-翻譯器- Azure AI服務](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 API密鑰
-------

将你嘅Translator API紙放在一個 `.env` 文件中：

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 許可證
-----

蔴省理工學院

引用
--

Markdown解析器，做得正確。 100% CommonMark支持，擴展，語法插件和高速。

* [markdown-it](https://github.com/markdown-it/markdown-it)
* [markdown-it-py](https://github.com/executablebooks/markdown-it-py)

把 HTML轉換為Markdown，最簡單嘅markdown編輯器，內置cloudinary圖像上傳。

* [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
* [Markdownify](https://github.com/tibastral/markdownify)

---
