i18n-md-翻译器
===========

一个命令行工具，用于使用 Microsoft Translator API 翻译 Markdown 文件。它保留了 Markdown 结构，包括表格、代码块、列表和脚注。

🛠 安装
----

```bash
pip install i18n-md-translator
```

🚀 用法
----

```bash
i18n-md-translate path/to/file.md -s en -t zh-Hant
```

* `-s` 或 `--source`：源语言(默认值： `en`)
* `-t` 或 `--target`：目标语言 (默认： `yue`)

🧪 例
---

```bash
i18n-md-translate ./README.md -s en -t yue
```

创建： `./yue/README.md`

🌐 支持的语言
-------

请参阅： [语言支持 - 翻译器 - Azure AI 服务](https://learn.microsoft.com/en-us/azure/ai-services/translator/language-support)

🔐 API 密钥
--------

将您的 Translator API 凭证放在一个 `.env` 文件中：

```ini
TRANSLATOR_KEY=your_key_here
TRANSLATOR_REGION=your_region_here
```

📄 许可证
-----

麻省理工学院

引用
--

Markdown 解析器，做得正确。100% CommonMark支持，扩展，语法插件和高速。

* [markdown-it](https://github.com/markdown-it/markdown-it)
* [markdown-it-py](https://github.com/executablebooks/markdown-it-py)

将 HTML 转换为 Markdown，最简单的 markdown 编辑器，内置 cloudinary 图像上传。

* [python-markdownify](https://github.com/matthewwithanm/python-markdownify)
* [Markdownify](https://github.com/tibastral/markdownify)

---